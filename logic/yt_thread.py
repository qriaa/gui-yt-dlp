import threading
import yt_dlp
import copy

class ytThread(threading.Thread):
    """This class is a thread which downloads videos."""
    def __init__(self, URL, options, vidAudio):
        threading.Thread.__init__(self)
        self.URL = URL
        self.options = copy.copy(options)
        self.vidAudio = vidAudio

    def run(self):
        self.download()
        return

    def download(self):
        if self.vidAudio == "audio":
            self.options["postprocessors"] = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}]
            #self.options["keepvideo"] = True
            self.options["outtmpl"] = '%(title)s [%(id)s][audio].%(ext)s'
        with yt_dlp.YoutubeDL(self.options) as ydl:
            ydl.download(self.URL)