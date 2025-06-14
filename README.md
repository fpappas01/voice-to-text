# Audio Summarizer 

This is a Python desktop application that takes an **audio file** (`.mp3`, `.mp4`, `.wav`, `.m4a`) as input and returns a **short description** of its content.

It uses the **OpenAI Whisper API** to transcribe and translate the audio into English (if necessary), and then passes the result through a second language model to generate a meaningful summary.

---

## Features

- Accepts various audio formats
- Translates non-English audio to English
- Generates a concise summary of the audio content
- Simple graphical user interface (Tkinter)
- Modular code structure

---

## Requirements

- Python 3.12+
- An OpenAI platform API key (not free)

Install dependencies:

```bash
pip install openai python-dotenv
