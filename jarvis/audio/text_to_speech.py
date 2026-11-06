"""
Text-to-speech output module using pyttsx3.
"""


def speak(text: str):
    """
    Print the reply to the terminal and pronounce it aloud using pyttsx3.
    """
    print("JARVIS:", text)
    try:
        import pyttsx3
        engine = pyttsx3.init()  # Initializing a fresh engine each time avoids pyttsx3 re-run bugs
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass  # If speech synthesis fails, printed text is sufficient
