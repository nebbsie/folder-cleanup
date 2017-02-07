import sys, os
from os.path import isfile, join
from os import listdir, walk
import shutil

moveAll = False
moveFilms = False

movieFormats = ('.avi', '.mp4', '.mkv', '.wav')

# Check if the user has entered a location folder if not it exits the program
if len(sys.argv) < 2:
    print("Enter the folder to cleanup. python cleanup.py <DIR LOCATION>")
    exit()
else:
    if sys.argv[1] == "all":
        moveAll = True
    elif sys.argv[1] == "films":
        moveFilms = True


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size


# Gets the base folder location from the arguments
location = sys.argv[2]
print("Searching for folders in location '" + location + "'.")

# List to hold the folders found
folders = []

# Looks for all folders in the base folder
for root, dirs, files in walk(location):
    if len(dirs) > 0:
        folders.append(dirs)

# Reset the folders to remove the multi-dimensional array
folders = folders[0]

# List to hold the folder with the files inside
files = []
movedFiles = 0
movedFilesSize = 0

# Loop through all of the folders
for x in range(0, len(folders)):
    # Set the location
    loc = location + '\\' + folders[x]

    # Get all files in the location folder
    files = [f for f in listdir(loc) if isfile(join(loc, f))]

    # Check if there are files in the folder
    if len(files) > 0:
        # Check through all files
        for i in files:
            # Set the location inside a folder with the file name
            fileLoc = str(loc + '\\' + i)
            # Check what the user input was and do the correct function
            if moveAll:
                movedFilesSize += file_size(fileLoc)
                shutil.move(fileLoc, location)
                movedFiles += 1
            elif moveFilms:
                # Checks if it is a valid movie format
                if fileLoc.endswith(movieFormats):
                    if file_size(fileLoc) > 400000000:
                        movedFilesSize += file_size(fileLoc)
                        shutil.move(fileLoc, location)
                        movedFiles += 1


if movedFiles > 0:
    print("Moved " + str(movedFiles) + " files." + "Size Of: " + convert_bytes(movedFilesSize))
else:
    print("Found no files in the subdirectories of " + location)


