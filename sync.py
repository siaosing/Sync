#! /usr/local/bin/python3

import os
import re
import shutil
import hashlib

tFolderList = []
tFolderList2 = []
md5dict = {}
deltaList = []

t2Path = "/Users/villan/Desktop/Python/Queue2/"
tPath = "/Users/villan/Desktop/Python/Queue/"
pathFinder = r"(.*/)(.*)$"
thoroughScan = True

print("")

def md5hash(fname, switch):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    x = hash.hexdigest()
    return x

def hash_check(file):
	completeName = tPath + file
	completeName2 = t2Path + file
	if completeName2 in md5dict['Destination']:
		if not md5dict['Source'][completeName] == md5dict['Destination'][completeName2]:
			print('MD5 Mismatch: ' + file)
			deltaList.append(file)

def folder_capture(path, switch):
	folderList = []

	if thoroughScan == True:
		md5dict.setdefault(switch, {})

	for root, dirs, files in os.walk(path):
	
		for i in files:
			tv = root + "/" + i
			result = tv[len(path):]
			if ".DS_Store" in i:
				continue
			folderList.append(result)

			if thoroughScan == True:
				md5dict[switch][tv] = md5hash(tv, switch)
			
	if not folderList:
		if switch == "Source":
			print('\nSource directory not available: ' + path + '\n')
		elif switch == "Desination":
			print('\nDestination directory is empty: ' + path + '\n')
	else:
		print(switch + " Directory: " + str(len(folderList)) + " files")	
	
	return folderList

# TV Folder capture

tFolderList = folder_capture(tPath, "Source")


# TV2 folder capture

tFolderList2 = folder_capture(t2Path, "Destination")
				
print("")

# Compare folder capture

for file in tFolderList:
	if not file in tFolderList2:
		deltaList.append(file)
	
	if thoroughScan == True:
		hash_check(file)


if not deltaList:
	print('\nDirectories are in sync.' + '\n')
else:
	print("Delta between folders: " + str(len(deltaList)))
	print("")

	for newFile in deltaList:
		m = re.search(pathFinder, newFile)
		if m:
			newFolder = t2Path + m.group(1) 
			if not os.path.exists(newFolder):
				os.makedirs(newFolder)
			
			new = tPath + newFile
			shutil.copy(new, newFolder)
			print("Copying: " + newFile + " -> " + m.group(1))

	print('\n***** Directories are now in sync. *****' + '\n')
	print("")

print("")

#print(md5dict)
