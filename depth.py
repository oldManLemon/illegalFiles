import glob
import settings
import folderScan as scan
import log

rootFolder = settings.scanDir
find =  settings.illegals
depth = 0
flag = 0
# See https://docs.python.org/3/library/glob.html for Documentation of patterns and glob(Strange name greate module)

# Exists to check if the folder is a job number. If not it will print the name of the folder that is not normal
def checkIfNormal(filepath):
    try:
      int(filepath[8]) #8th char is the the beginning of the job number. 
    except ValueError:
        log.logger(f"Abnormal Folder Found: {filepath}")
        
   
def jobDiscovery():
    for filename in glob.iglob(rootFolder+'/*/', recursive=True): #Finds the outside jobnumber eg 14079
        checkIfNormal(filename)
        #log.logger(f"Job: {filename}")
        bad = scan.scanFolderIgnore(filename)
        #print('Filename: '+filename[8:13])
        jobID = filename[8:13]
        #print(folderSerached)
        if bad != None:
            print(jobID)
            print(bad)
   
        

        for suffix in glob.iglob(filename+'/_?/', recursive=True): # Takes Jobnumber and searches for a suffix and returns full path eg J:\2014\14011\_B\
           # log.logger(f'Sacnning {suffix}')
            bad = scan.scanFolder(suffix)
            suffixID = suffix[15]
            #print(suffixFullName)
            if bad != None:
                print(jobID+suffixID)
                print(bad)

    