from twitter import *
import tkinter as Tk   

def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(master, text=line1 + "\n" + line2 + "\n\n")
        w.pack()

def getTweets():

    x = t.statuses.home_timeline(screen_name="putscreennamehere")
    return x


def tweet():

    global entryWidget

    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0,END)
        print("working")

t = Twitter(
    auth=OAuth('929752297340534786-pXd0olkpF6dBDfDK5mL2oY9j5ugKPUU', 'HemetwwLBwamM6pt4CWgk2IV2TtUfuGEnS40U7v9jiMyt',
               '5NswPby3STpD7PpODiBrPSRGlqFhOCKgGq0Vwj72CpUzWbQDiE', '2v6nkOKXqUG7mAUKMDOXkkrey'))

numberOfTweets = 10



master = Tk()
showTweets(getTweets(), numberOfTweets)

master.title("Tkinter Entry Widget")
master["padx"] = 40
master["pady"] = 20
#text frame to hold the text Label and the Entry widget
textFrame = Frame(master)
#Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Make a new Tweet:"
entryLabel.pack(side=LEFT)
# the Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(master, text="Submit", command=tweet)
button.pack()

master.mainloop()