import yt_dlp


class YoutubeObject():
    def __init__(self):
        self.URL = None
        self.fileName = None
        self.title = None
        self.id = None
        self.vidAudio = None
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

    def getInfo(self, URL):
        self.URL = URL
        with yt_dlp.YoutubeDL() as ydl:
            self.info = ydl.extract_info(URL, download=False)
        self.title = self.info["title"]
        self.id = self.info["id"]
        self.fileName = f"{self.title} [{self.id}]"
    

    def download(self):
        with yt_dlp.YoutubeDL() as ydl:
            ydl.download(self.URL)
    
    def toRecord(self):
        record = [self.id, self.title, self.vidAudio, self.fileName, self.URL]
        for tag in self.tags:
            record.append(tag)