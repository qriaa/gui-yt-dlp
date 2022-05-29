from pathlib import Path
import csv
import yt_dlp

class VideoBase:

    class folderNotLoaded(Exception):
        pass

    class newFolderException(Exception):
        pass

    class nonEmptyDir(Exception):
        pass

    cfgFile = Path(".videobase.csv")

    def __init__(self):
        dirPath = None
        fileBase = None
        loadedFolder = False

    def openFolder(self, dirPath):
        nonEmptyFolder = False
        noVideoBase = False

        if not (dirPath / VideoBase.cfgFile).exists():
            noVideoBase = True

        for child in dirPath.iterdir():
            nonEmptyFolder = True
            break
            
        if nonEmptyFolder and noVideoBase:
            raise VideoBase.nonEmptyDir("Chosen directory is not empty")
        elif noVideoBase:
            raise VideoBase.newFolderException("Folder has never been a videobase")

        self.dirPath = dirPath

        with open(dirPath / VideoBase.cfgFile, 'r') as file:
            reader = csv.reader(file)
            self.fileBase = []
            for row in reader:
                self.fileBase.append(row)
        self.loadedFolder = True


    def saveFolder(self):
        self.loadedFolderCheck()
        with open(self.dirPath / VideoBase.cfgFile, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.fileBase)


    def createVideoBaseFile(self, dirPath):
        (dirPath / VideoBase.cfgFile).touch()


    def createRecord(self, fileName, title, vidAudio, tags):
        self.loadedFolderCheck()
        record = [fileName, title, vidAudio]
        for tag in tags:
            record.append(tag)

        self.fileBase.append(record)
        pass



    def loadedFolderCheck(self):
        if not self.loadedFolder:
            raise VideoBase.folderNotLoaded()

    pass