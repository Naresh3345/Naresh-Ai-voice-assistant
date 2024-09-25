import speech_recognition as sr

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.............")
            text = r.recognize_google(audio, language='en-us')
            print(f"User Said: {text}\n")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Unable to recognize your voice")

while True:
    try:
        command()
    except KeyboardInterrupt:
        print("Program terminated by user.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
