from tkinter import *
class window:
    def __init__(self,title = "DefaultWin"):
        self.name = title
        self.gui = Tk(className = self.name)
    def set_size(self,x):
        self.gui.geometry(x)
    def run(self):
        self.gui.mainloop()

if __name__ == "__main__":
    win1 = window("Main window")
    win2 = window("2nd Window")
    win2.set_size("600x600")
    win1.set_size("500x500")
    win1.run()
    win2.run()