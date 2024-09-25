import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()

while True:
    text = input("Naresh")  # Corrected the input function
    say(text)  # Pass the variable text to the say function

