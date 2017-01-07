import os
import time

source = [r'C:\workspace\K28F',r'C:\workspace\cmd_markdown_win64']

target_dir = r'C:\workspace\test'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.7z'
#because I use 7zip, I change the command 
#first you should add the dir of 7zip in system path vairable

zip_command = "7z a %s %s" %(target, ' '.join(source))

print(zip_command)
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
