import threading
from logic.info_thread import InfoThread
from logic.yt_thread import ytThread

class YoutubeObject():
    def __init__(self):
        self.id = None
        self.title = None
        self.vidAudio = "video"
        self.fileName = None
        self.URL = None
        self.tags = []

        self.infoLock = threading.Lock()
        self.info = None
        self.infoThread = None

        self.dlThread = None
        self.dlProgress = 0
        self.dlSize = 0
    
    def dlHook(self, d):
        if d["status"] == "downloading":
            self.dlSize = d["total_bytes"]
            self.dlProgress = d["downloaded_bytes"]

    @classmethod
    def fromRecord(cls, record):
        ytObj = YoutubeObject()
        ytObj.id = record[0]
        ytObj.title = record[1]
        ytObj.vidAudio = record[2]
        ytObj.fileName = record[3]
        ytObj.URL = record[4]
        ytObj.tags = []
        for tag in record[5::]:
            ytObj.tags.append(tag)
        return ytObj

    def toRecord(self):
        record = [self.id, self.title, self.vidAudio, self.fileName, self.URL]
        for tag in self.tags:
            record.append(tag)
        return record

    def download(self, options):
        if self.dlThread != None and self.dlThread.is_alive():
            return
        self.dlThread = ytThread(self.URL, options, self.vidAudio)
        self.dlThread.start()
        

    def dlInfo(self, URL):
        if self.infoThread != None and self.infoThread.is_alive():
            return
        self.URL = URL
        self.infoThread = InfoThread(self, URL)
        self.infoThread.start()
        
    def setInfo(self, info):
        with self.infoLock:
            self.info = info
            self.title = self.info["title"]
            self.id = self.info["id"]
            ext = "mp4"
            if self.vidAudio == "audio":
                ext = "mp3"
            self.fileName = f"{self.title} [{self.id}][{self.vidAudio}].{ext}"

    def setVidAudio(self, vidAudio):
        vidAudio = vidAudio.lower()
        if not (vidAudio == "video" or vidAudio == "audio"):
            return
        self.vidAudio = vidAudio
