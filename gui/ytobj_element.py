import tkinter as tk
from tkinter import ttk

class YtObjElement(tk.Frame):
    def __init__(self, parent, record):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.record = record
        self.titleLabel = tk.Label(self, text=self.record.title)
        self.idLabel = tk.Label(self, text=self.record.id)
        self.status = ttk.Progressbar(self, mode="determinate")