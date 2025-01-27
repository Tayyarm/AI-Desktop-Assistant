import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()     # Initializes the TTS engine
    # Gets current speaking rate
    rate = engine.getProperty('rate') 
    # Sets new speaking rate
    engine.setProperty('rate', rate-70)
    engine.say(text)  # Converts text to speech
    engine.runAndWait() # Plays the speech