from os.path import isfile, join
from os import listdir, walk
import shutil
import Utils


class Films:
    # Format of the all the files the program will move.
    movieFormats = ('.avi', '.mp4', '.mkv', '.wav')

    # Constructor.
    def __init__(self, directory, size):
        self.directory = directory
        self.size = size

    # Function to move files.
    def moveFiles(self):
        # Print out action
        print("Searching for folders in location '" + self.directory + "'.")

        # List to hold the folders found
        folders = []

        # Looks for all folders in the base folder
        for root, dirs, files in walk(self.directory):
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
            loc = self.directory + '\\' + folders[x]

            # Get all files in the location folder
            files = [f for f in listdir(loc) if isfile(join(loc, f))]

            # Check if there are files in the folder
            if len(files) > 0:
                # Check through all files
                for i in files:
                    # Set the location inside a folder with the file name
                    fileLoc = str(loc + '\\' + i)
                    # Checks if it is a valid movie format
                    if fileLoc.endswith(self.movieFormats):
                        if Utils.file_size(fileLoc) > 400000000:
                            movedFilesSize += Utils.file_size(fileLoc)
                            shutil.move(fileLoc, self.directory)
                            movedFiles += 1

        if movedFiles > 0:
            return "Moved " + str(movedFiles) + " file/s. " + "Size Of: " + Utils.convert_bytes(movedFilesSize)
        else:
            return "Found no files in the subdirectories of " + self.directory