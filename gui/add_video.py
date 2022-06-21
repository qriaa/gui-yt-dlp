import re
import tkinter as tk
from tkinter import messagebox

from logic.youtube_object import YoutubeObject

class AddWindow(tk.Toplevel):
    """This class is a prompt for the user to input their desired new entry in the video base.
    It requires the user to provide a link to a youtube video and choose his desired form of download."""
    def __init__(self, parent, videoBase):
        tk.Toplevel.__init__(self, parent)
        self.resizable(False, False)
        self.parent = parent
        self.videoBase = videoBase
        self.geometry(f"300x100")
        self.mainFrame = tk.Frame(self)
        self.mainFrame.pack(fill="both", expand=True)

        self.linkLabel = tk.Label(self.mainFrame, text="Paste your youtube link here:")
        self.linkEntry = tk.Entry(self.mainFrame, width=45)

        self.choice = tk.StringVar(self.mainFrame, value="video")
        self.videoRadio = tk.Radiobutton(self.mainFrame, text="Video", variable=self.choice, value="video")
        self.audioRadio = tk.Radiobutton(self.mainFrame, text="Audio", variable=self.choice, value="audio")

        self.cancelButton = tk.Button(self.mainFrame, text="Cancel", command=self.cancel)
        self.okButton = tk.Button(self.mainFrame, text="Ok", command=self.ok)

        self.linkLabel.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)
        self.linkEntry.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
        self.videoRadio.grid(row=2, column=0)
        self.audioRadio.grid(row=2, column=1)
        self.cancelButton.grid(row=3, column=0)
        self.okButton.grid(row=3, column=1)
    
    def cancel(self):
        self.destroy()

    def ok(self):
        #yt link regex
        linkResult = re.fullmatch("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$",self.linkEntry.get())
        if linkResult == None:
            messagebox.showwarning("Incorrect link", "This youtube link is incorrect. Input a correct youtube link.")
            return
        newObj = YoutubeObject()
        newObj.dlInfo(self.linkEntry.get())
        newObj.setVidAudio(self.choice.get())
        self.videoBase.addYtObject(newObj)
        self.parent.workWindow.vidList.showList()
        self.destroy()