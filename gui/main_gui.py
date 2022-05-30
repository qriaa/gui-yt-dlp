import tkinter as tk
import tkinter.messagebox

class MainGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.geometry = "1000x500+100+100"
        self.parent.geometry(self.geometry)
        self.pack(fill="both", expand=True)
        self.parent.protocol("WM_DELETE_WINDOW", self.quit)
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
        #TODO: open videobase folder and handle its exceptions
    
    def quit(self):
        reply = tkinter.messagebox.askyesno("Quitting...", "Are you sure you want to quit?", parent=self.parent)
        if reply:
            #TODO: save and quit
            self.parent.destroy()
            pass