#------------------------------------------------------ALL IMPORTED MODULES---------------------------------------------------------------#
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import pywhatkit as kit
#-----------------------------------------------------------COMPUTERS VOICE---------------------------------------------------------------#
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# voices[0] for MALE VOICE voices[1] for FEMALE VOICE


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#-----------------------------------------------------FUNCTION TO WISH AND TAKE FIRST COMMAND---------------------------------------------#
def wishMe():
    print("\n------------------------------------------- 009 by OG ----------------------------------------------------")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I M 009 virtual assisstent, HOW MAY I HELP YOU SIR")

#-----------------------------------------------FUNCTION TO VOICE AS INPUT AND RETURN STRING AS OUPUT-------------------------------------#
def takeCommand():
    r = sr.Recognizer()  # Recognize audio
    with sr.Microphone() as source:
        print("\nI am listening sir, Please give me some command......")
        # if you take a gap of upto 1 second while speaking , it will not complete your phase.
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing your command sir......")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        print("Sorry sir can you say that again...")
        return "None"
    return query

#------------------------------------------------------------------MAIN FUNCTION---------------------------------------------------------#
if __name__ == "__main__":
    wishMe()
    while True:
            query = takeCommand().lower()
            #----------------------------------------------------------NORMAL GREETING------------------------------------------------------#                   
            if 'how are you' in query:
                speak("I am fine sir, thanks for asking")
            #----------------------------------------------------------WIKIPEDIA------------------------------------------------------------#
            elif 'wikipedia' in query:
                try:
                    speak('OK wait sir i am Searching Wikipedia for you...')
                    print(".....")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=5)
                    speak("So according to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry sir but there is no such specific wikipedia page, Please try with something else...")

            #----------------------------------------------------------GOOGLE SEARCH------------------------------------------------------#        
            elif 'google search' in query:
                r1 = sr.Recognizer()  # Recognize audio
                with sr.Microphone() as source:
                    speak("\nI am listening sir, what do you want to search on google")
                    print(".....")
                    r1.pause_threshold = 1
                    audio = r1.listen(source)
                    url = "https://www.google.co.in/search?q="
                try:
                    get = r1.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url+get)
                except Exception as e:
                    speak("Sorry sir there might be an audio issue")
                    
            #----------------------------------------------------------YOUTUBE SEARCH------------------------------------------------------#
            elif 'youtube search' in query:
                r2 = sr.Recognizer()  # Recognize audio
                with sr.Microphone() as source:
                    speak("\nI am listening sir, what do you want to search on youtube")
                    print(".....")
                    r2.pause_threshold = 1
                    audio = r2.listen(source)
                    url = "https://www.youtube.com/results?search_query="
                try:
                    get = r2.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url+get)
                except Exception as e:
                    speak("Sorry sir there might be an audio issue")
            #----------------------------------------------------------YOUTUBE PLAY--------------------------------------------------------#
            elif 'play video'in query:
                r4 = sr.Recognizer()  # Recognize audio
                with sr.Microphone() as source:
                    speak("\nI am listening sir, what do you want to play on youtube")
                    print(".....")
                    r4.pause_threshold = 1
                    audio = r4.listen(source)
                try:
                    get = r4.recognize_google(audio)
                    print(get)
                    kit.playonyt(get)
                except Exception as e:
                    speak("Sorry sir there might be an audio issue")                
                    
            #----------------------------------------------------------SPOTIFY SEARCH------------------------------------------------------#
            elif 'play music' in query:
                r3 = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("\nI am listening sir, which song or artist do you want to hear")
                    print(".....")
                    r3.pause_threshold = 1
                    audio = r3.listen(source)
                    url = "https://open.spotify.com/search/"
                try:
                    get = r3.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url+get)
                except Exception as e:
                    speak("Sorry sir there might be an audio issue")
            #----------------------------------------------------------Whatsapp message--------------------------------------------------------#
            elif 'send message' in query:
                r5 = sr.Recognizer()  # Recognize audio
                with sr.Microphone() as source:
                    speak("\nI am listening sir, what message do you want to send")
                    print(".....")
                    r5.pause_threshold = 1
                    audio = r5.listen(source)
                try:
                    get = r5.recognize_google(audio)
                    kit.sendwhatmsg("+918178858705",get,0,0)
                except Exception as e:
                    speak("Sorry sir there might be an audio issue")
                
                    
            #----------------------------------------------------------SEARCH TIME--------------------------------------------------------#
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            #----------------------------------------------------------OFFLINE SONGS------------------------------------------------------#
            elif'offline song' in query:
                music_dir='C:\\009s\\songs'
                songs =os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))

            #--------------------------------------------------------------EXIT-----------------------------------------------------------#           
            elif "goodbye" in query:
                speak("009 signing off sir")
                exit()

            #----------------------------------------------------------END---------------------------------------------------------------#
 

        




                                                                                         


