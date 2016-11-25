import os
path = 'C:\workspace\workspace for python\mine\0006'
for file in os.listdir(path):
	if os.path.isfile(os.path.join(path,file)) == True:
		newname = file.replace("0","x")
		os.rename(os.path.join(path,file),os.path.join(path,newname))
		print file
