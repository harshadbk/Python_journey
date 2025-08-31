import speech_recognition as sr
from googletrans import Translator

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_and_translate():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            # Translate the recognized text
            translated_text = translate(text, source_language="en", target_language="fr")
            print("Translated:", translated_text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")

def translate(text, source_language, target_language):
    translator = Translator()
    translated = translator.translate(text, src=source_language, dest=target_language)
    return translated.text

if __name__ == "__main__":
    listen_and_translate()
