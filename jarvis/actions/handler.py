"""
Action dispatcher and command parsing for predicted intents.
"""

import random
import datetime
import webbrowser
from urllib.parse import quote_plus

from jarvis.data.intents import JOKES
from jarvis.nlp.tokenizer import tokenize
from jarvis.audio.text_to_speech import speak
from .app_launcher import open_target


def extract_query(text: str) -> str:
    """
    Remove common command words to isolate the core search query.
    """
    stop_words = {
        "search", "for", "google", "look", "up", "find",
        "information", "about", "news"
    }
    words = [w for w in tokenize(text) if w not in stop_words]
    return " ".join(words) if words else text


def run_action(intent: str, text: str) -> bool:
    """
    Execute action corresponding to the predicted intent.
    Returns False when JARVIS receives the 'exit' command, True otherwise.
    """
    if intent == "greeting":
        speak("Hello! How can I help you?")

    elif intent == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif intent == "date":
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {current_date}")

    elif intent == "open_youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif intent == "open_google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif intent == "search_web":
        query = extract_query(text)
        speak(f"Searching for {query}")
        webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))

    elif intent == "joke":
        speak(random.choice(JOKES))

    elif intent == "who_are_you":
        speak(
            "I am Jarvis, a voice assistant. Whisper understands my ears, "
            "and a neural network trained by my creator understands my commands."
        )

    elif intent in ("open_app", "open_website"):
        open_target(text)

    elif intent == "exit":
        speak("Goodbye!")
        return False

    return True
