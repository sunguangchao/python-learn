import re,os,sys,subprocess,shutil
rootDir = r"C:\workspace\SDK_2.0_FRDM-K28F1"
enableParallelBuilding = False

warningList = []
errorList = []

fileNameExtension = {'iar':'.ewp','keil':'.uvprojx','armgcc':'CMakeLists.txt','kds':'.cproject','atl':'.cproject'}
environmentVariable = {'iar':'IAR_WORKBENCH','keil':'KEIL','kds':'KDS_WORKBENCH','atl':'ATL_WORKBENCH'}

sectionLine = "*" * 79
startInfo = "    Build start"
endInfo = "    Build finish"
script_dir, script_name = os.path.split(os.path.abspath(sys.argv[0]))

def searchToolChainBinPath(toolchain):
	try:
		workbenchPath = os.environ[environmentVariable[toolchain]]
		print workbenchPath
	except KeyError:
		raise RuntimeError(environmentVariable[toolchain]+" environment variable is not set.")
	else:
		if toolchain == 'iar':
			return os.path.normpath(os.path.join(workbenchPath, "common","bin","Iarbuild.exe"))
		elif toolchain == 'keil':
			return os.path.normpath(os.path.join(workbenchPath, "UV4.exe"))
		else:
			return workbenchPath

def getProjectName(path):
	with open(path) as fd:
		for line in fd:
			m = re.match(r'<name>(\S+)</name>',line.strip())
			if m:
				projectName = m.group(1)
				break
	return projectName

def iarProjectBuilder(iar_path, project_file, target_version):
	target_version = target_version.capitalize()
	project_path = os.path.dirname(project_file)
	print(sectionLine + "\n" + startInfo + project_path + " --" + target_version + "\n")

	p = subprocess.Popen([iar_path, project_file, '-make', target_version, '-log', 'info', '-parallel', '4'],
		stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0)
	build_log, err = p.communicate()

	if p.returncode != 0:
		errorList.append((project_path, target_version, build_log))
		print "** Build failed."
	else:
		if build_log.find('License check failed') >= 0:
			print 'License check failed!'
			return
		m = re.search(r'Total number of warnings: (\d+)', build_log)
		if m and int(m.group(1)) > 0:
			warningList.append((project_path, target_version, build_log))
		else:
			print "    Build succeed!"
	print('\n' + endInfo + project_path + " --" + target_version + '\n')



def generateProjectList(toolchain, rootdir):
	project_list = []
	for parents,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			project_file = os.path.join(parents,filename)
			if not 'boards' in project_file:
				continue
			if toolchain == 'atl' and not 'atl' in project_file:
				continue
			if toolchain == 'kds' and not 'kds' in project_file:
				continue
			if project_file.endswith(fileNameExtension[toolchain]):
				project_list.append(project_file)
	return project_list

def main():

	targetVersion = ''
	projectBuilder = {'iar':iarProjectBuilder}
	argvLength = len(sys.argv)
	if argvLength == 1:
		print "Usage:"
		exit(0)
	elif argvLength == 2:
		toolChain = sys.argv[1].lower()
	else:
		toolChain = sys.argv[1].lower()

	project_List = generateProjectList(toolChain,rootDir)# ?

	if toolChain == 'armgcc':
		toolChainBinPath = ''
	else:
		toolChainBinPath = searchToolChainBinPath(toolChain)
	try:
		for item in project_List:
			if not targetVersion == '':
				projectBuilder[toolChain](toolChainBinPath, item, targetVersion)#{}
			else:
				if toolChain == 'kds' or toolChain == 'atl':
					projectBuilder[toolChain](toolChainBinPath, item, 'debug|release')
				else:
					projectBuilder[toolChain](toolChainBinPath, item, 'debug')
					projectBuilder[toolChain](toolChainBinPath, item, 'release')
	except KeyboardInterrupt:
		dumpLog(toolChain)
		sys.exit()
	print sectionLine
	print "  %s  BUILD FINISH" %toolChain.upper()
	print sectionLine

	if warningList:
		print "Projects with warnings:"
		print
		for proj in warningList:
			print proj[0] + " --" + proj[1]
			print 59*'-'
	else:
		print "** No warnings detected."

	if errorList > 0:
		print len(errorList), "builds failed:"
		print
		for failed_project in errorList:
			print failed_project[0] + " --" + failed_project[1]
			print 59*'-'

		print sectionLine
	else:
		print "** all builds succeeded."
		print sectionLine
	dumpLog(toolChain)

def dumpLog(toolchain):
	with open(script_dir + os.sep + toolchain + '_build_log.txt','w') as f:
		print >> f, sectionLine
		print >> f, "          %s   BUILD   FINISH" %toolchain.upper()
		print >> f, sectionLine

		if errorList > 0:
			print >>f,len(errorList),"builds failed:\n"
			for failed_project in errorList:
				print >>f, failed_project[0] + " --" + failed_project[1]
				print >>f, failed_project[2]
				print >>f, 59*'-'

			print >>f, sectionLine
		else:
			print >>f, "** all builds succeeded."
			print >>f, sectionLine

		if warningList:
			print >>f, "Projects with warnings:"
		
			for proj in warningList:
				print >>f, proj[0] + " --" + proj[1]
				print >>f, proj[2]
				print >>f, 59*'-'
		else:
			print >>f, "** No warnings detected."

	print "Check the %s_build_log.txt for warning and error which loacated in %s" %(toolchain,script_dir)

if __name__ == '__main__':
	main()



