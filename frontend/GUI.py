import tkinter as tk
from tkinter import filedialog
import os
from dotenv import load_dotenv
import openai
from backend import transcribe_and_translate

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.mp4 *.wav *.m4a")]
    )
    if file_path:
        result_text.set("Processing the file...")
        root.update()
        audio_file = open(file_path, "rb")
        result = transcribe_and_translate.create_response(client, audio_file)
        result_text.set(result)



root = tk.Tk()
root.title("Audio Transcriber with OpenAI Whisper")
root.geometry("600x400")

tk.Label(root, text="Audio to Text", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Open file", command=select_file).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=550, justify="left").pack(padx=20, pady=20)

root.mainloop()