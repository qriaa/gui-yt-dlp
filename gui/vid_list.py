import tkinter as tk

from gui.ytobj_element import YtObjElement

class VidList(tk.Frame):

    maxShownElements = 10

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.videoBase = parent.videoBase

        self.currObjList = []
        self.topElementIndex = 0
        self.bind("<MouseWheel>", self.scroll)


    def scroll(self,e):
        if e.delta < 0:
            if self.topElementIndex + 1 < len(self.videoBase.ytObjects):
                self.topElementIndex += 1
                self.showList()
        else:
            if self.topElementIndex - 1 >= 0:
                self.topElementIndex -= 1
                self.showList()
        pass


    def showList(self):
        for child in self.winfo_children():
            child.destroy()
        
        upperRange = self.topElementIndex + self.maxShownElements if self.topElementIndex + self.maxShownElements < len(self.videoBase.ytObjects) else len(self.videoBase.ytObjects)

        for i, rng in enumerate(range(self.topElementIndex, upperRange)):
            ytElem = YtObjElement(self, self.videoBase.ytObjects[rng])
            ytElem.grid(row=i, column=0, sticky=tk.NSEW)
            self.currObjList = []
            self.currObjList.append(ytElem)
