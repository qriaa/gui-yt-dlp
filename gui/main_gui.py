from pathlib import Path
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from gui.toolbar import Toolbar

import logic.video_base

class MainGUI(tk.Frame):
    def __init__(self, parent, vbase):
        tk.Frame.__init__(self, parent)
        self.videoBase = vbase
        self.parent = parent
        self.geometry = "1000x500+100+100"
        self.parent.geometry(self.geometry)
        self.pack(fill="both", expand=True)
        self.parent.protocol("WM_DELETE_WINDOW", self.quit)

        self.createMenu()

        self.toolbar = Toolbar(self)
        self.toolbar.pack(side=tk.TOP, fill="x")
        pass

    def createMenu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Open Folder", self.openFolder, "Ctrl + O", "<Control-o>"),
                ("Quit", self.quit, "Ctrl + Q", "<Control-q>")
            ):
            fileMenu.add_command(label=label, command=command, accelerator=shortcut_text)
            self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=fileMenu)
    
    def openFolder(self):
        dirPath = tkinter.filedialog.askdirectory(title="Choose a video database folder", parent=self.parent)
        try:
            self.videoBase.openFolder(Path(dirPath))
        except logic.video_base.VideoBase.newFolderException:
            reply = tkinter.messagebox.askyesno(title="New folder initialisation", message="This folder has never been a video library. Do you want to make it one?")
            if reply:
                self.videoBase.createVideoBaseFile(Path(dirPath))
                self.videoBase.openFolder(Path(dirPath))
        except logic.video_base.VideoBase.nonEmptyDir:
            reply = tkinter.messagebox.askyesno(title="New folder initialisation", message="This folder has never been a video library and has some files present. Do you want to make it a library?")
            if reply:
                self.videoBase.createVideoBaseFile(Path(dirPath))
                self.videoBase.openFolder(Path(dirPath))

    def quit(self):
        reply = tkinter.messagebox.askyesno("Quitting...", "Are you sure you want to quit?", parent=self.parent)
        if reply:
            if self.videoBase.loadedFolder:
                self.videoBase.saveFolder()
            self.parent.destroy()
            pass