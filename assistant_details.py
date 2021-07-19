name = "Drake"

def speak(query):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    engine.say(query)
    engine.runAndWait()
    