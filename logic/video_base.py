from pathlib import Path
import threading
import csv
from logic.yt_thread import ytThread
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

        self.dlThreads = []
        self.dlSemaphore = threading.Semaphore()
        self.infoThreads = []
        self.infoSemaphore = threading.Semaphore()


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
            self.fileBase = []
            for row in reader:
                if row == []:
                    continue
                self.fileBase.append(YoutubeObject.fromRecord(row))
        self.loadedFolder = True


    def saveFolder(self):
        self.loadedFolderCheck()
        with open(self.dirPath / VideoBase.cfgFile, 'w', newline='') as file:
            file.truncate()
            writer = csv.writer(file)
            for ytObj in self.fileBase:
                writer.writerow(ytObj.toRecord())


    def createVideoBaseFile(self, dirPath):
        (dirPath / VideoBase.cfgFile).touch()


    def addYtObject(self, ytObj):
        self.loadedFolderCheck()
        if self.getYtObject(ytObj.id, ytObj.vidAudio) == None:
            self.fileBase.append(ytObj)
        pass
    
    def downloadYtObject(self, index):
        self.loadedFolderCheck()
        ytObj = self.fileBase[index]
        with self.dlSemaphore:
            thread = ytThread(ytObj.URL, self.dlOptions, ytObj.vidAudio)
            self.dlThreads.append(thread)
        thread.start()
        with self.dlSemaphore:
            self.dlThreads.remove(thread)

    def getYtObject(self, id, vidAudio):
        for i, ytobj in enumerate(self.fileBase):
            if ytobj.id == id and ytobj.vidAudio == vidAudio:
                return i
        return None

    def loadedFolderCheck(self):
        if not self.loadedFolder:
            raise VideoBase.folderNotLoaded()

    pass