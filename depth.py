import glob
import settings
import folderScan as scan

rootFolder = settings.scanDir
find =  settings.illegals
depth = 0
# See https://docs.python.org/3/library/glob.html for Documentation of patterns and glob(Strange name greate module)

# Exists to check if the folder is a job number. If not it will print the name of the folder that is not normal
def checkIfNormal(filepath):
    try:
      int(filepath[8]) #8th char is the the beginning of the job number. 
      #print(filepath)
    except ValueError:
        print("Abnormal Folder Found: ",filepath)
   
def jobDiscovery():
    for filename in glob.iglob(rootFolder+'/*/', recursive=True): #Finds the outside jobnumber eg 14079
        checkIfNormal(filename)
        scan.scanFolderIgnore(filename)
        for suffix in glob.iglob(filename+'/_?/', recursive=True): # Takes Jobnumber and searches for a suffix and returns full path eg J:\2014\14011\_B\
            print('Sacnning', suffix)
            #scan.scanFolder(suffix)
    