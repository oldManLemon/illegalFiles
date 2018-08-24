
import settings
import os
import os.path
import log




rootFolder = settings.scanDir
find =  settings.illegals
depth = 0
zips = settings.zips

#print('Scanning', rootFolder)


""" # Scan the Suffix Folders
def scanFolder(folder):
    badFiles = []
    #flag = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        
        for filename in [f for f in filenames if f.endswith(find)]:
            #flag = 1
            
            toLog = (os.path.join(dirpath, filename))
            log.logger(toLog)
            #badFiles.append((dirpath, filename))
            badFiles.append(toLog)
    #print(badFiles)
    if badFiles:
        return badFiles
            
    

#Scan the the main folder ignoring suffixes
def scanFolderIgnore(folder):
    #flag = 0
    badFiles = []   
    for dirpath, dirs, filenames in os.walk(folder,topdown=True):
        dirs[:] = [d for d in dirs if d not in settings.exclude]
        for filename in [f for f in filenames if f.endswith(find)]:
            #flag =1
                
            toLog = (os.path.join(dirpath, filename))
            log.logger(toLog)
            #badFolder = (os.path.join(dirpath))
            
    
            #badFiles.append((dirpath,filename))
            badFiles.append(toLog)
    #print(badFiles)
    if badFiles:
        return badFiles
    
 """


""" Here starts zip search """

# Scan the Suffix Folders
def scanFolderZip(folder):
    folders = []
    
    zipFiles = []
    paths =[]
    
    #flag = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        #print( os.path.basename(os.path.normpath(dirpath)))
        # if dirnames:
        #     print('Folder', dirnames)
        #     folders.append(dirnames)
        folders.append(dirpath)
        for filename in [f for f in filenames if f.endswith(zips)]:
            #flag = 1
            filename = filename.split('.',1)[0]
            toLog = (os.path.join(dirpath, filename))
            #print(toLog)
            #log.logger(toLog)
            #badFiles.append((dirpath, filename))
            zipFiles.append(filename)
            paths.append(toLog)
            #print(filename)
   
    """ Get the paths """
    duplicatedZips = set(paths) & set(folders)

   

    
    for path in duplicatedZips:
        trim = os.path.basename(os.path.normpath(path))
        trimlen = len(trim)
        path = path[:-trimlen]
        print("Please Look in", path, "\n for ", trim, "and ", trim+".zip")
        print("They appear to be extracted zips ie duplicates. Please remove either the folder or the zip or I will remove you!")
    
demo = 'J:\\2014\\14250'   
scanFolderZip(demo)    

#Scan the the main folder ignoring suffixes
""" def scanFolderIgnoreZip(folder):
    #flag = 0
    folders = []   
    zipFiles = []
    for dirpath, dirs, filenames in os.walk(folder,topdown=True):
        dirs[:] = [d for d in dirs if d not in settings.exclude]
        for filename in [f for f in filenames if f.endswith(zips)]:
            #flag =1
                
            toLog = (os.path.join(dirpath, filename))
            log.logger(toLog)
            #badFolder = (os.path.join(dirpath))
            
    
            #badFiles.append((dirpath,filename))
            badFiles.append(toLog)
    #print(badFiles)
    if badFiles:
        return badFiles
     """