from pathlib import Path
from logic.video_base import VideoBase
from logic.youtube_object import YoutubeObject


if __name__ == "__main__":
    vbase = VideoBase()
    vbase.openFolder(Path("test"))
    ytobj = YoutubeObject()
    ytobj.getInfo("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ytobj.setVidAudio("video")
    ytobj2 = YoutubeObject()
    ytobj2.getInfo("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ytobj2.setVidAudio("audio")
    vbase.addYtObject(ytobj)
    vbase.addYtObject(ytobj2)
    vbase.downloadYtObject(vbase.getYtObject(ytobj.id, ytobj.vidAudio))
    vbase.downloadYtObject(vbase.getYtObject(ytobj2.id, ytobj2.vidAudio))
    vbase.saveFolder()
    pass