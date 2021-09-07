from tkinter import Label, mainloop
class window:
    def __init__(self,title = "DefaultWin"):
        self.name = title
        Label(text = self.name).pack()
    def run(self):
        mainloop()

win1 = window()
win1.run()

