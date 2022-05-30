from pathlib import Path
from logic.video_base import VideoBase
from logic.youtube_object import YoutubeObject


if __name__ == "__main__":
    vbase = VideoBase()
    vbase.openFolder(Path("test"))
    ytobj = YoutubeObject()
    ytobj.getInfo("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ytobj.setVidAudio("video")
    vbase.addYtObject(ytobj)
    vbase.downloadYtObject(0)
    vbase.saveFolder()
    pass