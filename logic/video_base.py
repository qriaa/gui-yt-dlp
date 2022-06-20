from copy import copy
import subprocess
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
        self.ytObjects = None
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
        
        self.dlOptions["paths"] = {"home": str(self.dirPath), "temp": "temp"}
        self.dlOptions["format"] = "mp4"
        self.dlOptions["outtmpl"] = '%(title)s [%(id)s][video].%(ext)s'

        with open(dirPath / VideoBase.cfgFile, 'r') as file:
            reader = csv.reader(file)
            self.ytObjects = []
            for row in reader:
                if row == []:
                    continue
                self.ytObjects.append(YoutubeObject.fromRecord(row))
        self.loadedFolder = True


    def saveFolder(self):
        self.loadedFolderCheck()
        for ytObj in self.ytObjects:
            if ytObj.infoThread != None:
                ytObj.infoThread.join()
        with open(self.dirPath / VideoBase.cfgFile, 'w', newline='') as file:
            file.truncate()
            writer = csv.writer(file)
            for ytObj in self.ytObjects:
                writer.writerow(ytObj.toRecord())


    def createVideoBaseFile(self, dirPath):
        (dirPath / VideoBase.cfgFile).touch()


    def addYtObject(self, ytObj):
        self.loadedFolderCheck()
        ytObj.infoThread.join()
        if self.getYtObject(ytObj.id, ytObj.vidAudio) == None:
            self.ytObjects.append(ytObj)
        pass
    
    def downloadYtObject(self, index):
        self.loadedFolderCheck()
        ytObj = self.ytObjects[index]
        ytObj.download(self.dlOptions)
    
    def downloadYtObjectOptions(self, index, options):
        self.loadedFolderCheck()
        ytObj = self.ytObjects[index]
        optcopy = copy(self.dlOptions)
        optcopy.update(options)
        ytObj.download(optcopy)

    def getYtObject(self, id, vidAudio):
        for i, ytobj in enumerate(self.ytObjects):
            if ytobj.id == id and ytobj.vidAudio == vidAudio:
                return i
        return None
    
    def getYtObjectIndex(self, ytObj):
        for i, ytobj in enumerate(self.ytObjects):
            if ytobj.id == ytObj.id and ytobj.vidAudio == ytObj.vidAudio:
                return i
        return None

    def showFileInExplorer(self, ytObj):
        subprocess.Popen(f"explorer /select, \"{self.dirPath / self.ytObjects[self.getYtObjectIndex(ytObj)].fileName}\"")

    def loadedFolderCheck(self):
        if not self.loadedFolder:
            raise VideoBase.folderNotLoaded()


    pass