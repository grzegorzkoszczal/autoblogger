# Autoblogger for resume

# What to do:
# 1. Parse the URL to a YouTube video as a user input
#    I) Check for user input validation
#    II) Create a really simple GUI for a URL parsing
# 2. Download the subtitles from the video and save them as a text file.
#    I) Show the subtitles taken from a video.
# 3. Parse the wall-of-text to the ChatGPT and ask it to create a post on
#    a blog based on that
# 4. Check the error handling, correct code writing conventions, comments,
#    and nice set up of the project on the GitHub
#    I) A good idea would be a script that automatically creates Python
#    virtual environment and pulls the dependencies.

# Test case below:
# Ozzy Osbourne - A Thousand Shades
# https://www.youtube.com/watch?v=ZNVs-dfFUj0




# README.md 
# 1. Explain the project

# download subtitles function - explain what it does
# provide screenshots on how does the raw transcript looks like

# manage subtitles function - explain what it does
# provide screenshots on how does the prepared input looks like




import gui
import os
import time
import re
import openai
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from tkinter import *
from tkinter import messagebox
from functools import partial

# Preferably, hide the variable below:
with open(".api_key", "r") as f:
    for line in f:
        key = line

print(key)

# This function downloads the subtitles of a video, based on the
# input of a URL done by the user, and saves it in "subtitles.txt" file
def download_subtitles(youtube_url):
    try:
        youtube_id = youtube_url.split("https://www.youtube.com/watch?v=", 1)[1]
        output_file = "subtitles.txt"
        # assigning srt variable with the list 
        # of dictionaries obtained by the get_transcript() function
        srt = YouTubeTranscriptApi.get_transcript(youtube_id,
                                                    languages=['en'])
        

        # creating or overwriting a file "subtitles.txt" with 
        # the info inside the context manager
        with open("subtitles.txt", "w") as f:
        
            # iterating through each element of list srt
            for i in srt:
                # writing each element of srt on a new line
                f.write("{}\n".format(i))

            print(f'Subtitles downloaded successfully and saved to {output_file}')
        manage_subtitles()
    except Exception as e:
        print(f'An error occurred: {e}')


# This function prepares downloaded subtitles to be easier to read as an input
# for a prompt, that will be used for ChatGPT
def manage_subtitles():
    delimiters = "{\'text\': \'", "{'text': \"", "', 'start'", "\", 'start'"
    regex_pattern = '|'.join(map(re.escape, delimiters))

    input = open("input.txt", "w")

    with open("subtitles.txt", "r") as f:
        for line in f:
            result = re.split(regex_pattern, line)[1]
            result = result.replace("♪ ","")
            result = result.replace(" ♪","")
            result = result.replace("\\n"," ")
            input.write(result+". ")
            print(result)

    input.close()
    # chatgpt()


def prompt():
    answer.get
    print("Here You pass the subtitles to ChatGPT")


def chatgpt():
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

    # while True: 
    message = input("User : ") 
    if message: 
        messages.append({"role": "user", "content": message},)
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) 
        
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})


# Here is created a simple graphical layout of an application
def window():
    def submit_url():
        youtube_url = entry.get()
        print("URL entered: ", youtube_url)
        download_subtitles(youtube_url)

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
                             command=submit_url,
                             font=("Arial", 20, "bold"),
                             fg="black",
                             bg="white",
                             width=30
                    )
    button_download.pack(pady=10)

    # Blog entry based on subtitles
    # Explain emotions in song lyrics
    # Guess what is this video about

    radio_button_x = IntVar()
    radio_button_requests = [
        "Blog entry based on subtitles",
        "Explain emotions in song lyrics",
        "Guess what is this video about"
    ]

    # radio_button_requests = [
    #     "Based on the subtitles of the video, write a short blog entry about the topic of a video: ",
    #     "Describe the emotion that are shown in lyrics of this song: ",
    #     "Given the subtitles of a video, guess what is the topic of it: "
    # ]


    # Text that suggests You to choose the task You want to give to ChatGPT
    label2 = Label(window,
                  text="Choose the prompt",
                  font=("Arial", 20, "bold"),
                  fg="white",
                  bg="black")
    label2.pack(pady=10)


    # List of possible tasks
    for index in range(len(radio_button_requests)):
        radio_button = Radiobutton(window,
                                   text=radio_button_requests[index],
                                   variable=radio_button_x,
                                   value=index,
                                   font=("Arial", 12, "bold"),
                                   fg="black",
                                   bg="white",
                                   width=30,
                                   command=partial(choose_prompt, radio_button_x))
        radio_button.pack(pady=5, anchor=CENTER)


    # Button - pass the prompt
    button_prompt = Button(window,
                           text="Pass the prompt",
                           command=prompt,
                           font=("Arial", 20, "bold"),
                           fg="black",
                           bg="white",
                           width=30
                    )
    button_prompt.pack(pady=30)

    
    # A field with an answer given back by ChatGPT
    answer = Text(window,
                  name="text field",
                  background="white",
                  height=15,
                  width=100,)
    answer.pack()
    answer.insert(END,"test")

#     Text(
#     master: Misc | None = None,
#     cnf: dict[str, Any] | None = {},
#     *,
#     autoseparators: bool = ...,
#     background: str = ...,
#     bd: _ScreenUnits = ...,
#     bg: str = ...,
#     blockcursor: bool = ...,
#     border: _ScreenUnits = ...,
#     borderwidth: _ScreenUnits = ...,
#     cursor: _Cursor = ...,
#     endline: int | Literal[''] = ...,
#     exportselection: bool = ...,
#     fg: str = ...,
#     font: _FontDescription = ...,
#     foreground: str = ...,
#     height: _ScreenUnits = ...,
#     highlightbackground: str = ...,
#     highlightcolor: str = ...,
#     highlightthickness: _ScreenUnits = ...,
#     inactiveselectbackground: str = ...,
#     insertbackground: str = ...,
#     insertborderwidth: _ScreenUnits = ...,
#     insertofftime: int = ...,
#     insertontime: int = ...,
#     insertunfocussed: Literal['none', 'hollow', 'solid'] = ...,
#     insertwidth: _ScreenUnits = ...,
#     maxundo: int = ...,
#     name: str = ...,
#     padx: _ScreenUnits = ...,
#     pady: _ScreenUnits = ...,
#     relief: _Relief = ...,
#     selectbackground: str = ...,
#     selectborderwidth: _ScreenUnits = ...,
#     selectforeground: str = ...,
#     setgrid: bool = ...,
#     spacing1: _ScreenUnits = ...,
#     spacing2: _ScreenUnits = ...,
#     spacing3: _ScreenUnits = ...,
#     startline: int | Literal[''] = ...,
#     state: Literal['normal', 'disabled'] = ...,
#     tabs: _ScreenUnits | tuple[_ScreenUnits, ...] = ...,
#     tabstyle: Literal['tabular', 'wordprocessor'] = ...,
#     takefocus: _TakeFocusValue = ...,
#     undo: bool = ...,
#     width: int = ...,
#     wrap: Literal['none', 'char', 'word'] = ...,
#     xscrollcommand: _XYScrollCommand = ...,
#     yscrollcommand: _XYScrollCommand = ...
# )

    window.mainloop()

def choose_prompt(radio_button_x):
    if(radio_button_x.get()==0):
        print("Blog entry based on subtitles")
    elif(radio_button_x.get()==1):
        print("Explain emotions in song lyrics")
    elif(radio_button_x.get()==2):
        print("Guess what is this video about")
    else:
        print("No prompt has been chosen")

def main():
    window()

if __name__ == "__main__":
    # Open app GUI
    main()