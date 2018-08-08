
import settings
import os
import os.path



rootFolder = settings.scanDir
find =  settings.illegals
depth = 0

print('Scanning', rootFolder)



def scanFolder(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
     for filename in [f for f in filenames if f.endswith(find)]:
        print (os.path.join(dirpath, filename))


def scanFolderIgnore(folder):

    for dirpath, dirs, filenames in os.walk(folder,topdown=True):
        dirs[:] = [d for d in dirs if d not in settings.exclude]
        for filename in [f for f in filenames if f.endswith(find)]:
            print (os.path.join(dirpath, filename))        


