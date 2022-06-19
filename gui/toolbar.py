import os
import tkinter as tk
import tkinter.messagebox

class Toolbar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.toolbarImages = []
        self.buttons = []
        for image, command in (("images/add.png", self.addVideo),):
            self.addButton(image, command)

    def addButton(self, image, command):
        image = os.path.join(os.path.dirname(__file__), image)
        try:
            image = tk.PhotoImage(file=image)
            self.toolbarImages.append(image)
            button = tk.Button(self, image=image, command=command)
            button.grid(row=0, column=len(self.toolbarImages)-1)
            self.buttons.append(button)
        except tk.TclError as err:
            print(err)
    
    def addVideo(self):
        pass