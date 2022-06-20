import tkinter as tk
from gui.vid_list import VidList

from gui.ytobj_element import YtObjElement

class WorkWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.videoBase = parent.videoBase

        self.vidList = VidList(self)
        self.vidList.pack(fill="both", expand=True)

    def onOpenFolder(self):
        self.vidList.showList()