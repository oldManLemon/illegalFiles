
import settings
import os
import os.path
import log




rootFolder = settings.scanDir
find =  settings.illegals
depth = 0

#print('Scanning', rootFolder)


# Scan the Suffix Folders
def scanFolder(folder):
    flag = 0
    for dirpath, dirnames, filenames in os.walk(folder):
     for filename in [f for f in filenames if f.endswith(find)]:
        flag = 1
        #print (os.path.join(dirpath, filename))
        toLog = (os.path.join(dirpath, filename))
        log.logger(toLog)
        print(dirnames)
    

#Scan the the main folder ignoring suffixes
def scanFolderIgnore(folder):
    flag = 0
    for dirpath, dirs, filenames in os.walk(folder,topdown=True):
        dirs[:] = [d for d in dirs if d not in settings.exclude]
        for filename in [f for f in filenames if f.endswith(find)]:
            flag =1
            #print (os.path.join(dirpath, filename))        
            toLog = (os.path.join(dirpath, filename))
            log.logger(toLog)
            print(dirs)
    

