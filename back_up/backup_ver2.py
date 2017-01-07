import os
import time

source = [r'C:\workspace\K28F',r'C:\workspace\cmd_markdown_win64']

target_dir = r'C:\workspace\test'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory',today

target = today + os.sep + now + '.7z'

zip_command = "7z a %s %s" %(target,' '.join(source)) #' '

if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
