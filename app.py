from tkinter import *
import webbrowser

myframe = Tk()


def myfonction():
    webbrowser.open("https://www.youtube.com/watch?v=kPOm5OqHqWM&t=184s")


myframe.title("my App")  # we changed the name from Tk to my App
myframe.geometry("500x300")

mylabel = Label(myframe, text="web browser", font="Helvatica 20 bold")
mylabel.pack(pady=30)

myButton = Button(myframe, text="click me", fg="blue", bg="red", font="Helvatica 20 bold",
                  command=myfonction)  # fg change color of the text and bg change color of the button

myButton.pack(side=LEFT)
myframe.mainloop()