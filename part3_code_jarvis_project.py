# import necessary libraries
import pyttsx3  # library for text-to-speech conversion
import speech_recognition as sr  # library for speech recognition

# Initialize 
engine = pyttsx3.init()# Initialize the pyttsx3 engine
r = sr.Recognizer()# Initialize the speech recognizer

# Define a function to make the Jarvis assistant speak
def Jarvis_Speak(text):
    rate=100  # Set the speaking rate to 100
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[0].id)  # Set the voice to the first available one
    engine.setProperty('rate', rate+50)  # Increase the speaking rate by 50
    engine.say(text)  # Make Jarvis speak the given text
    engine.runAndWait()  # Wait for Jarvis to finish speaking

# Define a function to handle user responses
def Response(text_receive):
    if "hi" in text_receive or "hello" in text_receive:  # If user says "hi" or "hello"
        Jarvis_Speak("Hi!")  # Respond with "Hi"
    elif "how are you" in text_receive:  # If user says "how are you"
        Jarvis_Speak("I'm fine, thanks for asking.")  # Respond with "I'm fine"
    elif "introduction" in text_receive:  # If user says "introduction"
        Jarvis_Speak("Hi there, I'm Jarvis.")  # Introduce Jarvis
    else:  # If none of the previous conditions are met
        Jarvis_Speak("I'm sorry, I didn't understand your question. Could you please repeat it?")  # Ask user to repeat their question

Jarvis_Speak("I'm sorry, I didn't understand your question. Could you please repeat it?")
# Use the default microphone as the source of audio
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)  # Adjust for ambient noise

    while True:
        # Listen for audio input from the user
        print("Say anything: ")
        audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)  # Recognize the user's speech
            print("You said: " + text)  # Print what the user said
            Response(text.lower())  # Pass the user's speech to the Response function
        except sr.UnknownValueError:  # If the user's speech cannot be recognized
            print("Cannot recognize audio")  # Print an error message