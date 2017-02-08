'''
This simple python program shows step by step how to backup files and folders in a computer as a zip file
'''
import os
import time
source = ['C:\\books\\'] #now we are going to set the data source location.This is windows type path you can use linux path here

target_dir = 'E:\\backups' #Now we are going to set the target directory

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') +'.zip' #Now we are going to make the zip file
                                                                     #zipfile name will be created from the current system time

#if the backup directory is not present then create it
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target,' '.join(source)) #zip file creation  command to zip the backup files
                                                               #Running the Zip Command
print('The Zip Command is: ',zip_command)
print('Running.........')
if os.system(zip_command) == 0:
    print('Successful backup to: ',target)
else:
    print('backup failed!!!!')
