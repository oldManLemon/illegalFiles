import settings
import os
import os.path

rootFolder = settings.scanDir

print('Scanning', rootFolder)
def scanFolder():
    for dirpath, dirnames, filenames in os.walk(rootFolder):
     for filename in [f for f in filenames if f.endswith(".log")]:
        print (os.path.join(dirpath, filename))


scanFolder()