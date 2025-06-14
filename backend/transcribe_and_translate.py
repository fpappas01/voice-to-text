def create_response(client, audio_file):

    translation = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file,
    )

    response = client.chat.completions.create(model="gpt-4",
    messages=[
    {"role": "system", "content": "You are an assistant that answers in English"},
        {"role": "user", "content": "Describe shortly what the following text is about: " + translation.text}
    ])

    return response.choices[0].message.content

