from pathlib import Path
import csv
from logic.youtube_object import YoutubeObject

class VideoBase:

    class folderNotLoaded(Exception):
        pass

    class newFolderException(Exception):
        pass

    class nonEmptyDir(Exception):
        pass

    cfgFile = Path(".videobase.csv")

    def __init__(self):
        self.dirPath = None
        self.fileBase = None
        self.loadedFolder = False
        self.dlOptions = {}

    def openFolder(self, dirPath):
        nonEmptyFolder = False
        noVideoBase = False

        if not (dirPath / VideoBase.cfgFile).exists():
            noVideoBase = True

        for _ in dirPath.iterdir():
            nonEmptyFolder = True
            break
            
        if nonEmptyFolder and noVideoBase:
            raise VideoBase.nonEmptyDir("Chosen directory is not empty")
        elif noVideoBase:
            raise VideoBase.newFolderException("Folder has never been a videobase")

        self.dirPath = dirPath
        
        self.dlOptions["paths"] = {"home": str(self.dirPath), "temp": "."}

        with open(dirPath / VideoBase.cfgFile, 'r') as file:
            reader = csv.reader(file)
            self.fileBase = []
            for row in reader:
                if row == []:
                    continue
                self.fileBase.append(YoutubeObject.fromRecord(row))
        self.loadedFolder = True


    def saveFolder(self):
        self.loadedFolderCheck()
        with open(self.dirPath / VideoBase.cfgFile, 'w') as file:
            writer = csv.writer(file)
            for ytObj in self.fileBase:
                writer.writerow(ytObj.toRecord())


    def createVideoBaseFile(self, dirPath):
        (dirPath / VideoBase.cfgFile).touch()


    def addYtObject(self, ytObj):
        self.loadedFolderCheck()
        self.fileBase.append(ytObj)
        pass
    
    def downloadYtObject(self, index):
        self.loadedFolderCheck()
        self.fileBase[index].download(self.dlOptions)

    def loadedFolderCheck(self):
        if not self.loadedFolder:
            raise VideoBase.folderNotLoaded()

    pass