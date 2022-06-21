import threading
import yt_dlp

class InfoThread(threading.Thread):
    """This class is a thread which downloads information about a video."""
    def __init__(self,  parent, URL):
        threading.Thread.__init__(self)
        self.parent = parent
        self.URL = URL

    def run(self):
        self.download()
        return

    def download(self):
        with yt_dlp.YoutubeDL() as ydl:
            self.info = ydl.extract_info(self.URL, download=False)
        
        self.parent.setInfo(self.info)