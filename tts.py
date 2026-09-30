import pyttsx3


# Initialize TTS once
tts_engine = pyttsx3.init()


def speak(text):
    print("JARVIS is speaking...")

    tts_engine.say(text)
    tts_engine.runAndWait()