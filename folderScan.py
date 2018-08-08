
import settings
import os
import os.path



rootFolder = settings.scanDir
find =  settings.illegals
depth = 0

print('Scanning', rootFolder)



def scanFolder():
    for dirpath, dirnames, filenames in os.walk(rootFolder):
     for filename in [f for f in filenames if f.endswith(find)]:
        print (os.path.join(dirpath, filename))


