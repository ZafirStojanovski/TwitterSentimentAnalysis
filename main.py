from tkinter import *
import tkinter
from PIL import Image, ImageTk
import statistics
import sentiment_analysis
import pie
#import led_manager

res = None

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)            
        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("Twitter Sentiment Analysis")
        self.pack(fill=BOTH, expand=1)


def getRoot():
    root = Tk()
    root.grid_rowconfigure(1, minsize=235)
    root.grid_rowconfigure(3, minsize=10)
    root.grid_columnconfigure(0, weight=1)
    root.resizable(False,False)
    root.update()    
    root.geometry('{}x{}'.format(640, 427)) 

    return root 

def getFrame():
    frame = Example(root)
    frame.grid(row=0)
    return frame

def setUpUI(root):
    #Image
    im = Image.open('rb-new.jpg')
    tkimage = ImageTk.PhotoImage(im)
    myvar=tkinter.Label(root, image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)

    #TextBox
    phrase = StringVar()
    entry = Entry(root, textvariable=phrase)
    entry.grid(row=2)

    #Button
    button = tkinter.Button(root, text=u"Search", command=OnButtonClick)
    button.grid(row=4)

    
    global res
    res = phrase
   
    root.mainloop()

def loadGraph(phrase, sentimentResult):
    dataDictionary = sentimentResult.singleTweetSentiment
        
    positives = dataDictionary[sentimentResult.POSITIVE]
    negatives = dataDictionary[sentimentResult.NEGATIVE]
    neutrals = dataDictionary[sentimentResult.NEUTRAL]

    data = []
    data.append(positives)
    data.append(negatives)
    data.append(neutrals)

    graph = pie.Graph()
    graph.setData(data)
    graph.plotData(phrase, positives, negatives, neutrals, sentimentResult.mean, sentimentResult.variance) 


def lightUpRaspberry(sentimentAnalysis, sentimentResult):
    ledManager = led_manager.LEDManager()

    finalResult = sentimentAnalysis.classify(sentimentResult.mean)
    if finalResult == sentimentResult.POSITIVE:
        ledManager.turnOnGreen()
    elif finalResult == sentimentResult.NEGATIVE:
        ledManager.turnOnRed()
    else:
        ledManager.turnOnRed()

    print(finalResult)


def OnButtonClick():
    phrase = res.get()

    if phrase != "":
        sentimentAnalysis = sentiment_analysis.SentimentAnalysis()
        sentimentResult = sentimentAnalysis.getSentiment(phrase)
        
        #lightUpRaspberry(sentimentAnalysis, sentimentResult)
        loadGraph(phrase, sentimentResult)

if __name__ == "__main__":
    root = getRoot()
    frame = getFrame()
    setUpUI(root)