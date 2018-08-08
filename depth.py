import glob
import settings

rootFolder = settings.scanDir
find =  settings.illegals
depth = 0

for filename in glob.iglob(rootFolder+'/*/', recursive=True): #Finds the outside jobnumber eg 14079
    print(filename)
    for suffix in glob.iglob(filename+'/_*/', recursive=True): # Takes Jobnumber and searches for a suffix and returns full path eg J:\2014\14011\_B\
        print(suffix)