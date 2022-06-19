from pathlib import Path
import tkinter as tk
from gui.main_gui import MainGUI
from logic.video_base import VideoBase
from logic.youtube_object import YoutubeObject


if __name__ == "__main__":
    root = tk.Tk()
    root.title("gui-yt-dlp")
    vbase = VideoBase()
    app = MainGUI(root, vbase)
    app.mainloop()
    pass