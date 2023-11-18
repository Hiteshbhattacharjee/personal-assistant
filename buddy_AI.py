#this code is property of Hitesh Bhattacharhjee
import speech_recognition as sr
import pyttsx3#type:ignore
import datetime
        
        
from turtle import * #type:ignore
import webbrowser
import pywhatkit#type:ignore
import wikipedia

time = int(datetime.datetime.now().hour)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        r.energy_threshold = 1000 # Adjust the energy threshold   
        print("listening....")
        audio = r.listen(source)
        
        r.pause_threshold = 1
    try:
        print("recognising....")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except:
        print(e)
        query = ""
        print("voice not recognised ...... please try again!")

    return str(query)


def say(str):
    engine.say(str)
    engine.runAndWait()


def wishme():
    if time > 4 and time < 12:
        say("Good morning user!")
    elif time >= 12 and time < 17:
        say("Good Afternoon User!")
    elif time >= 17 and time < 24:
        say("Good evening ")


if __name__ == '__main__':
    wishme()
    # say(wishme)
    say("I am BUDDY AI made by HITESH Bhattacharjee how may I help you?")

    query = str(listen()).lower()
    # print(query)
    if "open youtube" == query:
        webbrowser.open("www.youtube.com")
    elif "flipkart" in query:
        webbrowser.open("www.flipkart.com")
    elif "instagram" in query:
        webbrowser.open("www.instagram.com")
    elif "facebook" in query:
        webbrowser.open("www.facebook.com")
    elif "open google" == query:
        webbrowser.open("www.google.com")
    elif "stackoverflow" in query:
        webbrowser.open("www.stackoverflow.com")
    elif "github" in query:
        webbrowser.open("www.github.com")
    elif "microsoft" in query:
        webbrowser.open("www.microsoft.com")
    elif "chatgpt" in query:
        webbrowser.open("https://chat.openai.com/")
    elif "smart ai" == query:
        webbrowser.open("https://bard.google.com/chat")
    elif "take notes" in query:
        webbrowser.open("https://keep.google.com/u/0/")
    elif "send" in query and "whatsapp" in query:
        try:
            number = "+91"
            say("enter the number I have to send message")
            number += str(listen())
            say("okay, now what should I send?")
            msg = listen()
            minute = int(datetime.datetime.now().strftime("%M"))+1

            pywhatkit.sendwhatmsg(number, msg, time, minute, 10) # type: ignore
        except Exception as e:
            print(e)
            say("I can't send that")
    elif "mail" in query or "email" in query:
        say("please enter sender's email address in terminal")
        sender = input()
        say("enter your password in terminal , it is needed, dont worry it is safe")
        password = input()
        say("please tell the subject of email")
        sub = listen()
        say("please speak the message")
        content = listen()
        say("please enter reciever's email in terminal")
        reciever = input()
        pywhatkit.send_mail(sender, password, str(sub), str(content), reciever) #type: ignore
    elif "tell me" in query:
        query = query.replace("on wikipedia","")
        query = query.replace("wikipedia","")
        query = query.replace("search","")
        say(f"searching {query} on wikipedia")
        # (f"searching {query} on wikipedia")
        # say(f"just give me a second")

        results = wikipedia.summary(query,sentences = 2)
        say("here are the results")
        print(results)
        say(results)
    elif "play" in query and "youtube" in query :
        query = query.replace("play","")
        query = query.replace("on youtube","")
        query = query.replace("youtube","")
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

    elif "play" in query and "spotify" in query :
        query = query.replace("play","")
        query = query.replace("on spotify","")
        query = query.replace("spotify","")
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"
        webbrowser.open(f"https://open.spotify.com/search")
    
    # webbrowser.open("https://lms.bennett.edu.in/my/")
 

    elif "search" in query and "smart ai" in query: 
        query = query.replace("search","")
        query = query.replace("on smart ai","")
        query = query.replace("smart ai","")
        string = query.split()
        search = ""
        for i in string:
            search += i
            search += "+"
        webbrowser.open(f"https://bard.google.com/results?search_query={search}")

    elif "search " in query and "chatgpt" in query: 
        query = query.replace("search","")
        query = query.replace("on chatgpt","")
        query = query.replace("chatgpt","")
        string = query.split()
        search = ""
        for i in string:
            search += i
            search += "+"
        webbrowser.open(f"https://chat.openai.com/results?search_query={search}")

    elif "search" in query and "google" in query:
        query = query.replace("search","")
        query = query.replace("on google","")
        query = query.replace("google","")
        string = query.split()
        search = ""
        for i in string:
            search += i
            search += "+"
        webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")

    
    
    elif "notes "in query:
        webbrowser.open("https://keep.google.com/u/0/")


    elif "calendar" in query:
        webbrowser.open("calendar.google.com")

    # elif "recommend" in query:
    #     str(input(""))
        # webbrowser.open("https://pickamovieforme.com/")

    elif "calculator" in query:
        webbrowser.open("https://www.google.com/search?q=calculator&oq=calculator&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDINCAEQABiDARixAxiABDIHCAIQABiABDIHCAMQABiABDIKCAQQABixAxiABDIHCAUQABiABDIKCAYQABixAxiABDIKCAcQABixAxiABDIGCAgQRRhA0gEHNDY1ajBqMagCALACAA&sourceid=chrome&ie=UTF-8")
    # Define a dictionary with movie recommendations based on moods
    elif "recommend" in query:

        movie_recommendations = {
            'happy': ['The Secret Life of Walter Mitty', 'Up', 'The Intouchables', 'La La Land'],
            'sad': ['The Green Mile', 'Schindler\'s List', 'Atonement', 'Manchester by the Sea'],
            'action': ['Mad Max: Fury Road', 'John Wick', 'Avengers: Endgame', 'Mission: Impossible - Fallout'],
            'romantic': ['Pride and Prejudice', 'Before Sunrise', 'The Notebook', 'Eternal Sunshine of the Spotless Mind'],
            'thriller': ['Inception', 'Gone Girl', 'Shutter Island', 'The Silence of the Lambs']
        }

        # Function to recommend movies based on mood
        def recommend_movie(mood):
            mood = mood.lower()
            if mood in movie_recommendations:
                print(f"Here are some {mood} movies you might enjoy:")
                for movie in movie_recommendations[mood]:
                    print(movie)
            else:
                print("Sorry, we don't have recommendations for that mood.")

        # Asking user for input and providing recommendations
        # user_mood = input
        say("Enter your mood (happy, sad, action, romantic, thriller): ")
        user_mood = str(listen())
        (recommend_movie(user_mood))

    #  elif "open code" == query or "vs code" in query:
    #     path = "path of app"
	#path = path.replace("\","/")
	#webbrowser.open(path)
    else:
        string = query.split()
        search = ""
        for i in string:
            search += i
    
            search += "+"

        webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")
#copyright© Hitesh Bhattacharjee
