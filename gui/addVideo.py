import tkinter as tk

class AddWindow(tk.Toplevel):
    def __init__(self, parent, videoBase):
        tk.Toplevel.__init__(self, parent)
        self.videoBase = videoBase
        self.geometry(f"400x400")
        