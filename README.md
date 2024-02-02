# Autoblogger for resume

## Purpose of this repository

The main goal of this repo is to showcase a simple application that incorporates the use of generative nature of ChatGPT. At first, the user provides the URL to a YouTube video that comes with the subtitles, such as music video, vlog etc. and executes prompts chosen by the user. Finally, the response is generated, based on the context of the transcript.

## Using the autoblogger (user path)

In order to start using the application right off the bat, one can simply download the "main" file, which is an pre-compiled, standalone executable. Additionally, there are two things needed for the user to provide: a YouTube video URL and an OpenAI secret API key. While the getting video URL is rather self-explanatory, in the next subsection I will cover the steps of getting the API key.

### OpenAI secret API key

1. Visit the OpenAI website: https://openai.com/
2. Make an account and log in.
3. On the left-hand side, choose the "API keys"

![Screenshot_20240131_083920](https://github.com/grzegorzkoszczal/autoblogger/assets/141007769/8d090640-4bb2-4ac4-b106-7aee89a4df19)

4. Click "create new key". Name it however You want.
5. Copy the generated key somewhere safe. You will need it later to use the application.
6. You are all set!

### Using the app

1. Execute the "main_win.exe" file, if You are on Windows or "main_linux", if You are on Linux. A small GUI window will pop-up.
2. Paste the YouTube video URL (Important! Check beforehand, if the video have the subtitles available, otherwise it will not be possible to get the transcript!)
3. Click the "Download subtitles" button. The subtitle are downloaded, stored and refined by the app.
4. Paste the secret API key in the text field in the lower-right box.
5. Choose the radio button with different prompt, that suits Your needs.
6. Click the "Pass the prompt" button. You may need to wait up to 20 seconds for the answer to come.
7. Enjoy the response!

Below are shown screenshots of the three different answers. All the prompt are based of the lyrics of this music video:
https://youtu.be/ZNVs-dfFUj0?si=XVc1jk_FVE0WOXPO

#### Blog entry
![blog_entry_key](https://github.com/grzegorzkoszczal/autoblogger/assets/141007769/d5b787af-a88f-4656-b189-55afd6db879e)

#### Describe emotions
![emotions_key](https://github.com/grzegorzkoszczal/autoblogger/assets/141007769/eda9a4cf-fa0b-435b-b083-31f8d5b4d8b3)

#### Guess the contents of the video
![guess_key](https://github.com/grzegorzkoszczal/autoblogger/assets/141007769/8f8a6156-6ec5-4f0e-91f7-b6e490e2d56c)

## Using the autoblogger (developer path)

### Downloading the repository

In order to download the entire repo, clone it in the chosen directory
```console
foo@bar:~$ git clone https://github.com/grzegorzkoszczal/autoblogger.git
```

### Installing environment
In order to install all the needed stuff for further development of the code, use the Install.sh script
```console
foo@bar:~/autoblogger$ source install.sh
```
It will automatically create Python virtual environment, activate it and pull all the dependecies required for the development. Modify the project by changing the code in the "main.py" file. After that, follow the steps of the "Using the autoblogger (user path)" subsection in order to create API key.


