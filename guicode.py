from tkinter import *
from skimage import filters, measure, io, transform

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Digit recogniser")
        self.root.geometry("500x300")
        self.leftFrame = Frame(self.root)
        self.leftFrame.pack(side=LEFT)
        self.rightFrame = Frame(self.root)
        self.rightFrame.pack(side=RIGHT)
        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack(side=BOTTOM)
        self.authorLabel = Label(self.bottomFrame, text="Created by Dominik and Julia", fg="white", bg="black")
        self.authorLabel.pack(fill=X)
        self.processButton = Button(self.rightFrame, text="Process", fg="purple", bg="black", command=self.process)
        self.processButton.pack(side=TOP)
        self.processReset = Button(self.rightFrame, text="Reset", fg="purple", bg="black", command=self.reset)
        self.processReset.pack(side=TOP)
        self.answerNum = Label(self.rightFrame)
        self.answerNum.pack(side=BOTTOM)
        self.answer = Label(self.rightFrame, text="Recognised number:")
        self.answer.pack(side=BOTTOM)
        self.drawHere = Label(self.leftFrame, text="Please write here:")
        self.drawHere.pack(side=LEFT)
        self.canvas = Canvas(self.leftFrame, width=65, height=65)
        self.canvas.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.reset()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.root.mainloop()

    def process(self):
        self.answerNum["text"] = "Num"
        self.canvas.postscript(file="Num.eps",height=55,width=55,x=4,y=4)


    def reset(self):
        self.canvas.create_rectangle(3, 3, 67, 67, fill="white")

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_rectangle([x1, y1, x2, y2], fill="black")


if __name__ == "__main__":
    gui = GUI()
