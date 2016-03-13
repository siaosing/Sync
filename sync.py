#! /usr/local/bin/python3

import os
import re
import shutil

tvFolderList = []
tvFolderList2 = []
deltaList = []

tv2Path = "/Users/villan/Desktop/Python/Queue2/"
tvPath = "/Users/villan/Desktop/Python/Queue/"
pathFinder = r"(.*/)(.*)$"

print("")

def folder_capture(path, switch):
	folderList = []

	for root, dirs, files in os.walk(path):
	
		for i in files:
			tv = root + "/" + i
			result = tv[len(path):]
			if ".DS_Store" in i:
				continue
			folderList.append(result)
			
	if not folderList:
		if switch == "Source":
			print('\nSource directory not available: ' + path + '\n')
		elif switch == "Desination":
			print('\nDestination directory is empty: ' + path + '\n')
	else:
		print(switch + " Directory: " + str(len(folderList)) + " files")	
	
	return folderList

# TV Folder capture

tvFolderList = folder_capture(tvPath, "Source")


# TV2 folder capture

tvFolderList2 = folder_capture(tv2Path, "Destination")
				
print("")

# Compare folder capture

for file in tvFolderList:
	if not file in tvFolderList2:
		deltaList.append(file)

if not deltaList:
	print('\nDirectories are in sync.' + '\n')
else:
	print("Delta between folders: ")
	print(deltaList)
	print("")

	for newFile in deltaList:
		m = re.search(pathFinder, newFile)
		if m:
			newFolder = tv2Path + m.group(1) 
			if not os.path.exists(newFolder):
				os.makedirs(newFolder)
			
			new = tvPath + newFile
			shutil.copy(new, newFolder)
			print("Copying: " + newFile + " -> " + m.group(1))

	print('\n***** Directories are now in sync. *****' + '\n')
	print("")

print("")
