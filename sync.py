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

# TV Folder capture

for root, dirs, files in os.walk(tvPath):
	
	for i in files:
		tv = root + "/" + i
		result = tv[len(tvPath):]
		if ".DS_Store" in i:
			continue
		tvFolderList.append(result)
		
if not tvFolderList:
	print('\nSource directory not available: ' + tvPath + '\n')
	exit()
else:
	print("Source Directory: " + str(len(tvFolderList)) + " files")	

# TV2 folder capture
				
for root, dirs, files in os.walk(tv2Path):
	
	for i in files:
		tv2 = root + "/" + i
		result2 = tv2[len(tv2Path):]
		if ".DS_Store" in i:
			continue
		tvFolderList2.append(result2)

if not tvFolderList2:
	print('\nDestination directory empty: ' + tv2Path + '\n')

else:
	print("Destination Directory: " + str(len(tvFolderList2)) + " files")
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
			print("Copying: " + new + " -> " + newFolder)

	print('\nDirectories are now in sync.' + '\n')
	print("")

print("")
