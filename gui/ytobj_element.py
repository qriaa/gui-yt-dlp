import os
import subprocess
import tkinter as tk
from tkinter import ttk

class YtObjElement(tk.Frame):
    def __init__(self, parent, ytObj):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.ytObj = ytObj
        self.titleLabel = tk.Label(self, text=self.ytObj.title)
        icon = "images/vid.png" if self.ytObj.vidAudio == "video" else "images/audio.png"
        icon = os.path.join(os.path.dirname(__file__), icon)
        self.vidAudioIcon = tk.PhotoImage(file=icon)
        self.vidAudioLabel = tk.Label(self, image=self.vidAudioIcon)
        self.idLabel = tk.Label(self, text=self.ytObj.id)
        self.status = ttk.Progressbar(self, mode="determinate")

        self.titleLabel.grid(row=0, column=0)
        self.vidAudioLabel.grid(row=0, column=1)
        self.idLabel.grid(row=0, column=2)
        self.status.grid(row=0, column=3)

        self.popupMenu = tk.Menu(self, tearoff=0)
        self.popupMenu.add_command(label="Download", command=self.download)


        self.bindTags(self.titleLabel)
        self.bindTags(self.vidAudioLabel)
        self.bindTags(self.idLabel)
        self.bindTags(self.status)


    
    def bindTags(self, widget):
        # https://stackoverflow.com/questions/32771369/how-to-pass-an-event-to-parent-tkinter-widget
        bindtags = list(widget.bindtags())
        bindtags.insert(1, self)
        widget.bindtags(tuple(bindtags))

        widget.bind("<1>", self.selectRow)
        widget.bind("<Double-Button-1>", self.openFolder)
        widget.bind("<3>", self.popup)

    def selectRow(self):
        print(f"halo {self.ytObj.id}")
    
    def openFolder(self, e):
        self.parent.videoBase.showFileInExplorer(self.ytObj)

    def popup(self, e):
        try:
            self.popupMenu.tk_popup(e.x_root, e.y_root, 0)
        finally:
            self.popupMenu.grab_release()

    def download(self):
        self.parent.videoBase.downloadYtObject(self.parent.videoBase.getYtObjectIndex(self.ytObj))
        self.progressVariable = tk.Variable(self, value=0)