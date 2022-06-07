import yt_dlp


class YoutubeObject():
    def __init__(self):
        self.id = None
        self.title = None
        self.vidAudio = "video"
        self.fileName = None
        self.URL = None
        self.tags = []
        self.info = None
    
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

    def getInfo(self, URL):
        self.URL = URL
        with yt_dlp.YoutubeDL() as ydl:
            self.info = ydl.extract_info(URL, download=False)
        self.title = self.info["title"]
        self.id = self.info["id"]
        self.fileName = f"{self.title} [{self.id}][{self.vidAudio}].mp4"
    
    def setVidAudio(self, vidAudio):
        vidAudio = vidAudio.lower()
        if not (vidAudio == "video" or vidAudio == "audio"):
            return
        self.vidAudio = vidAudio

    
    