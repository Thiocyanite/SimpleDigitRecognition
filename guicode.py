from tkinter import *
import skimage.io as ski_io

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras import regularizers
from tensorflow.keras.datasets import mnist
from tensorflow.keras import backend as K
from tensorflow.keras.models import model_from_json
import cv2
import numpy as np

class Application:
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
        self.canvas = Canvas(self.leftFrame, width=31, height=31)
        self.canvas.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.reset()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.load_neural_network()
        self.root.mainloop()

    def load_neural_network(self):
        # load json and create model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.neural_network = model_from_json(loaded_model_json)
        # load weights into new model
        self.neural_network.load_weights("model.h5")
        print("Loaded model from disk")

    def process(self):
        self.canvas.postscript(file="Num.eps",height=27,width=27,x=4,y=4)
        # read the postscript data
        data = ski_io.imread("Num.eps")
        # write a rasterized png file
        ski_io.imsave("Num.png", data)
        img = cv2.imread("Num.png")
        kernel = np.ones((5, 5), np.float32) / 25
        img = cv2.filter2D(img, -1, kernel)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (28, 28))
        img = np.reshape(img, [1, 28, 28, 1])
        print(img.shape)
        classes = self.neural_network.predict_classes(img)
        self.answerNum["text"] = classes

    def reset(self):
        self.canvas.create_rectangle(3, 3, 33, 33, fill="white")

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black")


if __name__ == "__main__":
    gui = Application()
