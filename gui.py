import gui
import os
import time
from tkinter import *
from functools import partial

def window():
    # Create GUI window
    window = Tk()
    window.geometry("1280x720")
    window.title("Autoblogger")
    window.config(background="black")


    # Information what to do in app window
    label1 = Label(window,
                  text="Paste the URL of chosen YouTube video",
                  font=("Arial", 20, "bold"),
                  fg="white",
                  bg="black")
    label1.pack(pady=10)


    # Text field - paste the URL
    entry = Entry(window,
                    width="40",
                    font=("Arial", 10))
    entry.pack(pady=10)


    # Button - confirm download of subtitles from URL
    button_download = Button(window,
                             text="Download subtitles",
                             font=("Arial", 20, "bold"),
                             fg="black",
                             bg="white",
                             width=30
                    )
    button_download.pack(pady=10)

    answer = Text(window,
                  name="text field",
                  background="white",
                  height=15,
                  width=100,)
    
    # Button - pass the prompt
    button_prompt = Button(window,
                           text="Pass the prompt",
                           command=partial(prompt, answer),
                           font=("Arial", 20, "bold"),
                           fg="black",
                           bg="white",
                           width=30
                    )
    button_prompt.pack(pady=30)


    answer.pack()

    window.mainloop()


def prompt(answer):
    text_ans = "ChatGPT wisdom"
    answer.insert(END, text_ans)
    return text_ans


window()