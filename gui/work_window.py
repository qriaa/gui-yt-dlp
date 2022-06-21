import tkinter as tk
from gui.vid_list import VidList

from gui.ytobj_element import YtObjElement

class WorkWindow(tk.Frame):
    """This class manages the workspace. It has been created to easily swap the contents of itself in case of new screens."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.videoBase = parent.videoBase

        self.vidList = VidList(self)
        self.vidList.pack(fill="both", expand=True)

    def onOpenFolder(self):
        self.vidList.showList()