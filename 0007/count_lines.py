import os
def get_file(path):
	filepath = os.listdir(path) #list all path
	files = [] #list
	for fp in filepath:
		fppath = path + '/' + fp #full path
		if(os.path.isfile(fppath)):
			files.append(fppath)
		elif(os.path.isdir(fppath)):
			files += get_file(fppath) #iteration
	return files

def count_lines(files):
	line,blank,note = 0, 0, 0
	for filename in files:
		f = open(filename,'rb')
		for l in f:
			l = l.strip() #??
			line += 1
			if l == '':
				blank += 1
			elif l[0] == '#' or l[0] == '/':
				note += 1
		f.close()
	return(line,blank,note)

if __name__ == '__main__':
	files = get_file('.') #current path?
	print files
	lines = count_lines(files)
	print 'Line(s): %d,black line(s): %d,note line(s): %d' %(lines[0],lines[1],lines[2])
