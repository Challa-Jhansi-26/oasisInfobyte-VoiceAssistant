import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"User said: {command}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return listen_command()
    except sr.RequestError:
        speak("Sorry, my speech service is down")
        return None
    return command

# Function to respond to the command
def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What would you like to search for?")
        search_query = listen_command()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
    """else:
        speak("I am sorry, I don't know that command.")"""

# Main loop to keep the assistant running
def voice_assistant():
    speak("I am your voice assistant. How can I assist you?")
    while True:
        command = listen_command()
        if command:
            respond(command)
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    voice_assistant()