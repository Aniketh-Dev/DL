"""
Application and website launcher for JARVIS.
"""

import subprocess
import webbrowser
from typing import Dict, Optional

from jarvis.config import APPS, SITES
from jarvis.nlp.tokenizer import tokenize
from jarvis.audio.text_to_speech import speak


def open_target(
    text: str,
    apps: Optional[Dict[str, str]] = None,
    sites: Optional[Dict[str, str]] = None,
):
    """
    Open an application or website based on the user's spoken command.
    Checks desktop applications first, then maps known websites (or falls back to domain.com).
    """
    if apps is None:
        apps = APPS
    if sites is None:
        sites = SITES

    clean = " ".join(tokenize(text))

    # 1. Match known desktop application
    for name, command in apps.items():
        if name in clean:
            speak("Opening " + name)
            try:
                subprocess.Popen(f'start "" "{command}"', shell=True)  # Windows shell command
            except Exception as e:
                speak("Sorry, I could not open " + name)
            return

    # 2. Extract website query
    skip = {
        "open", "launch", "start", "run", "go", "to", "the", "website",
        "app", "please", "take", "me", "web", "site"
    }
    words = [w for w in tokenize(text) if w not in skip]
    if not words:
        speak("What should I open?")
        return

    name = "".join(words)  # e.g., "stack overflow" -> "stackoverflow"
    address = sites.get(name, f"{name}.com")

    speak("Opening " + name)
    webbrowser.open("https://" + address)
