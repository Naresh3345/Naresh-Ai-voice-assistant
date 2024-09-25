import speech_recognition as sr
import pyttsx3
import pyjokes

assis_name = "Naresh"
boss_name = "Naresh Kumar"

def say(text):
    """Function to speak the given text."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    """Function to listen to the user's voice and return the text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..............")
            text = r.recognize_google(audio, language='en-in')
            print(f"user said: {text}\n")
        except sr.UnknownValueError:
            print("Could not understand the audio")
            say("Sorry, I did not understand what you said. Could you please repeat?")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            say("There seems to be an issue with the speech recognition service.")
            return "None"
        except Exception as e:
            print(f"An error occurred: {e}")
            say("Sorry, something went wrong.")
            return "None"
        return text

def tell_joke():
    """Function to get a random joke."""
    joke = pyjokes.get_joke()
    return joke

def respond(text):
    """Function to respond based on the user input."""
    if 'hi' in text.lower():
        say("Hi Sir!")
    elif "who are you" in text.lower():
        say(f"My name is {assis_name}")
    elif "good morning" in text.lower():
        say(f"A warm {text}")
        say(f"How are you, {boss_name}?")
    elif "i am fine" in text.lower():
        say("Oh really good")
    elif "who am i" in text.lower():
        say("If you talk then definitely you're human.")
    elif "who are you" in text.lower():
        say(f"My name is {assis_name}! My Boss's name is {boss_name}.")
    elif "where am i" in text.lower():
        say("You are in a comfortable place, I hope!")
    elif 'thank you so much' in text.lower():
        say("It's my pleasure!")
    elif 'fine' in text.lower() or "good" in text.lower():
        say("It's good to know that you're fine.")
    elif 'tell me a joke' in text.lower():
        engine2 = pyttsx3.init()
        engine2.setProperty('rate', 100)
        engine2.say(tell_joke())
        engine2.runAndWait()

if __name__ == "__main__":
    while True:
        text = takecommand()
        if text != "None":
            respond(text)
