# Autoblogger for resume

from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from tkinter import *
from functools import partial

# Test case below:
# Ozzy Osbourne - A Thousand Shades
# https://www.youtube.com/watch?v=ZNVs-dfFUj0

# Useful links:
# Quickstart guide: https://platform.openai.com/docs/quickstart?context=python
# API-keys: https://platform.openai.com/api-keys
# Retrieve the personal secret OpenAI API key

# This function takes the user input (YouTube video URL), downloads the
# subtitles of a video, and saves it in "subtitles" global variable
def download_subtitles(entry):
    try:
        url = entry.get()
        youtube_id = url.split("https://www.youtube.com/watch?v=", 1)[1]
        # assigning srt variable with the list 
        # of dictionaries obtained by the get_transcript() function
        srt = YouTubeTranscriptApi.get_transcript(youtube_id,
                                                    languages=['en'])
        
        global subtitles
        subtitles = str()

        for key in srt:
            subtitles = subtitles + key["text"]
            subtitles = subtitles.replace("♪ ","")
            subtitles = subtitles.replace(" ♪","")
            subtitles = subtitles.replace("\\n","")
            subtitles = subtitles + ". "

    except Exception as e:
        print(f'An error occurred while downloading the subtitles: {e}')


def chatgpt(window, radio_button_x, answer_box, entry_key):
    if answer_box.compare("end-1c", "!=", "1.0"):
        answer_box.delete("1.0", END)

    answer_box.insert(END,"Thinking...")
    window.update()

    which_prompt = radio_button_x.get()
    prompts = {
        0: "Write a blog entry based on video subtitles, presented in double quotation marks: ",
        1: "Explain emotions in song lyrics, presented in double quotation marks: ",
        2: "Guess what is this video about, based on these subtitles presented in double quotation marks: "
    }
    user_command = prompts.get(which_prompt)
    user_command = "User: "+user_command+"\""+subtitles+"\""

    # Implementing responses from ChatGPT
    client = OpenAI(api_key=entry_key.get())
    MODEL = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_command},
        ],
        temperature=0,
    )
    final_message_from_ChatGPT = response.choices[0].message.content
    answer_box.delete("1.0", END)
    answer_box.insert(END,final_message_from_ChatGPT)


# Here is created a simple graphical layout of an application
def main():


    # Create GUI window
    window = Tk()
    window.geometry("800x800")
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
                    width=44,
                    font=("Arial", 10))
    entry.pack(pady=10)


    # Button - confirm download of subtitles from URL
    button_download = Button(window,
                             text="Download subtitles",
                             command=partial(download_subtitles, entry),
                             font=("Arial", 20, "bold"),
                             fg="black",
                             bg="white",
                             width=20
                    )
    button_download.pack(pady=10)
    

    # Labels of prompts to choose
    radio_button_x = IntVar()
    radio_button_requests = [
        "Blog entry based on subtitles",
        "Explain emotions in song lyrics",
        "Guess what is this video about"
    ]


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
                                   width=30)
        radio_button.pack(pady=5, anchor=CENTER)


    # A field with an answer given back by ChatGPT
    answer_box = Text(window,
                  name="text field",
                  background="white",
                  height=22,
                  width=100,)


    # Text field - paste the ChatGPT secret API key
    entry_key = Entry(window,
                    width=200,
                    font=("Arial", 10))
    

    # Button - ask ChatGPT
    button_prompt = Button(window,
                           text="Pass the prompt",
                           command=partial(chatgpt, window, radio_button_x, answer_box, entry_key),
                           font=("Arial", 20, "bold"),
                           fg="black",
                           bg="white",
                           width=20
                    )
    button_prompt.pack(pady=30)
    answer_box.pack()


    # Text that indicates place to put ChatGPT secret API key
    label3 = Label(window,
                   anchor=W,
                   justify=LEFT,
                   text="Pass the ChatGPT secret API key: ",
                   font=("Arial", 10, "bold"),
                   fg="white",
                   bg="black")
    label3.pack(padx=50, side=LEFT)
    entry_key.pack(padx=50, side=RIGHT)

    window.mainloop()


if __name__ == "__main__":
    # Open app GUI
    main()
