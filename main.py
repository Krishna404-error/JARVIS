from speech import listen
from llm import ask_jarvis
from tts import speak
from database import create_database, save_conversation


def main():

    # Create database when JARVIS starts
    create_database()

    print("JARVIS is ready.")
    print("Hold SPACE to speak.")
    print("Say 'goodbye jarvis' to exit.\n")

    while True:

        # Listen
        text = listen()

        if not text:
            print("I didn't hear anything.")
            continue

        print("You:", text)

        # Exit command
        if "goodbye jarvis" in text.lower():
            goodbye = "Goodbye. I'll be here when you need me."

            print("JARVIS:", goodbye)

            speak(goodbye)

            break

        # Ask the AI
        reply = ask_jarvis(text)

        print("JARVIS:", reply)

        # Save conversation
        save_conversation(text, reply)

        # Speak response
        speak(reply)

        print()


if __name__ == "__main__":
    main()