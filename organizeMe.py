################################################################################
# Name    : organizeMe.py                                                      #
# Author  : Ibrahim Musayev                                                    #
# Purpose : Script does generate new directories for each file type.           #
# History : 28-07-22 : creation                                                #
################################################################################

import os 
import pathlib as Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDir(value):
    for cat, suffs in SUBDIRECTORIES.items():
        for suff in suffs:
            if suff == value:
                return cat
    return 'MISC'

def organizeDir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path.WindowsPath(item)
        filetype = filePath.suffix.lower()
        directory = pickDir(filetype)
        directoryPath = Path.WindowsPath(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

if __name__ == '__main__':
    organizeDir()
    