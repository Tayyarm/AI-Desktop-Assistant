import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()    #convert to lowercase
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return "My name is Virtual Assistant"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hello! How can I help you?")
        return "Hello! How can I help you?"
        
        
    elif "goodmorning" in user_data:
        text_to_speech.text_to_speech("Good morning! How can I help you?")
        return "Good morning! How can I help you?"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        time = (str)(current_time) + "Hour :" , (str)(current_time.minute) + "Minute :" , (str)(current_time.second) + "Second :"
        text_to_speech.text_to_speech(time)
        return time
        
    elif "shut down" in user_data:
        text_to_speech.text_to_speech("Ok sir")
        return "Ok sir"
        
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is now ready for you")
        return "Spotify is now ready for you"
        
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"
        
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"
        
    elif "open facebook" in user_data:
        webbrowser.open("https://facebook.com/")
        text_to_speech.text_to_speech("facebook.com is now ready for you")
        return "facebook.com is now ready for you"
        
    elif "open instagram" in user_data:
        webbrowser.open("https://instagram.com/")
        text_to_speech.text_to_speech("instagram.com is now ready for you")
        return "instagram.com is now ready for you"
        
    elif "open x" in user_data:
        webbrowser.open("https://x.com/")
        text_to_speech.text_to_speech("x.com is now ready for you")
        return "x.com is now ready for you"
        
    elif "open linkedin" in user_data:
        webbrowser.open("https://linkedin.com/")
        text_to_speech.text_to_speech("linkedin.com is now ready for you")
        return "linkedin.com is now ready for you"
        
    elif "open github" in user_data:
        webbrowser.open("https://github.com/")
        text_to_speech.text_to_speech("github.com is now ready for you")
        return "github.com is now ready for you"
        
    elif "open stackoverflow" in user_data:
        webbrowser.open("https://stackoverflow.com/")
        text_to_speech.text_to_speech("stackoverflow.com is now ready for you")
        return "stackoverflow.com is now ready for you"
        
    elif "open whatsapp" in user_data:
        webbrowser.open("https://web.whatsapp.com/")
        text_to_speech.text_to_speech("whatsapp.com is now ready for you")
        return "whatsapp.com is now ready for you"
        
    elif "open telegram" in user_data:
        webbrowser.open("https://telegram.org/")
        text_to_speech.text_to_speech("telegram.org is now ready for you")
        return "telegram.org is now ready for you"
        
    elif "open discord" in user_data:
        webbrowser.open("https://discord.com/")
        text_to_speech.text_to_speech("discord.com is now ready for you")
        return "discord.com is now ready for you"
        
    elif "open zoom" in user_data:
        webbrowser.open("https://zoom.us/")
        text_to_speech.text_to_speech("zoom.us is now ready for you")
        return "zoom.us is now ready for you"
        
    elif "open netflix" in user_data:
        webbrowser.open("https://www.netflix.com/")
        text_to_speech.text_to_speech("netflix.com is now ready for you")
        return "netflix.com is now ready for you"
        
    elif "open amazon" in user_data:
        webbrowser.open("https://www.amazon.com/")
        text_to_speech.text_to_speech("amazon.com is now ready for you")
        return "amazon.com is now ready for you"
         
    elif "open google classroom" in user_data:
        webbrowser.open("https://classroom.google.com/u/0/")
        text_to_speech.text_to_speech("classroom.google.com is now ready for you")
        return "classroom.google.com is now ready for you"
            
    elif "open google meet" in user_data:
        webbrowser.open("https://meet.google.com/")
        text_to_speech.text_to_speech("meet.google.com is now ready for you")
        return "meet.google.com is now ready for you"
        
    elif "open google docs" in user_data:
        webbrowser.open("https://docs.google.com/")
        text_to_speech.text_to_speech("docs.google.com is now ready for you")
        return "docs.google.com is now ready for you"
        
    elif "open google slides" in user_data:
        webbrowser.open("https://docs.google.com/presentation/")
        text_to_speech.text_to_speech("docs.google.com/presentation is now ready for you")
        return "docs.google.com/presentation is now ready for you"
        
    elif "open google forms" in user_data:
        webbrowser.open("https://docs.google.com/forms/")
        text_to_speech.text_to_speech("docs.google.com/forms is now ready for you")
        return "docs.google.com/forms is now ready for you"
        
    elif "open google sheets" in user_data:
        webbrowser.open("https://docs.google.com/spreadsheets/")
        text_to_speech.text_to_speech("docs.google.com/spreadsheets is now ready for you")
        return "docs.google.com/spreadsheets is now ready for you"
        
    elif "open drive" in user_data:
        webbrowser.open("https://drive.google.com/")
        text_to_speech.text_to_speech("drive.google.com is now ready for you")
        return "drive.google.com is now ready for you"
        
    elif "open google calendar" in user_data:
        webbrowser.open("https://calendar.google.com/")
        text_to_speech.text_to_speech("calendar.google.com is now ready for you")
        return "calendar.google.com is now ready for you"
        
    elif "open google maps" in user_data:
        webbrowser.open("https://maps.google.com/")
        text_to_speech.text_to_speech("maps.google.com is now ready for you")
        return "maps.google.com is now ready for you"
        
    elif "open google translate" in user_data:
        webbrowser.open("https://translate.google.com/")
        text_to_speech.text_to_speech("translate.google.com is now ready for you")
        return "translate.google.com is now ready for you"
        
    elif "open google news" in user_data:
        webbrowser.open("https://news.google.com/")
        text_to_speech.text_to_speech("news.google.com is now ready for you")
        return "news.google.com is now ready for you"
        
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
        
        
    else:
        text_to_speech.text_to_speech("I'm sorry, I don't understand that command")
        return "I'm sorry, I don't understand that command"
        
    
    
    