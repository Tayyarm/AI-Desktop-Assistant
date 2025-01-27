import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()  # Creates a recognizer object to detect speech

    with sr.Microphone() as source:      # Opens your microphone as an audio source     
        audio = r.listen(source)         # Listens for audio input and records it

    try: 
        voice_data = ""    # Creates empty string to store the text
        voice_data = r.recognize_google(audio)  # Converts speech to text using Google's API
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("RequestError") 
        