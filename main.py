import speech_recognition as sr
from gtts import gTTS
import openai
import os
import time

r = sr.Recognizer()

def SpeakText(command):
    # Initialize the engine
    tts = gTTS(text=command, lang='cs')
    tts.save("speak.mp3")
    time.sleep(2)
    os.system(".\\mpg123\\mpg123.exe" + " speak.mp3")


openai.api_key = "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"
while (1):

    try:
        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            query = r.recognize_google(audio2, language="cs-CZ")
            query = query.lower()

            print("Did you say ", query)
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.6,
            )
            print(response["choices"][0]["text"])
            SpeakText(response["choices"][0]["text"])

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
