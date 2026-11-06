"""
Training dataset for intent classification and conversational responses.
"""

INTENTS = {
    "greeting": [
        "hello", "hello jarvis", "hi", "hi there", "hey jarvis", "good morning",
        "good evening", "hey", "howdy", "greetings"
    ],
    "time": [
        "what time is it", "tell me the time", "current time", "what is the time now",
        "time please", "can you tell me the time", "what's the time", "show me the time",
        "do you know the time"
    ],
    "date": [
        "what is the date today", "tell me the date", "today's date", "what day is it today",
        "which date is today", "current date", "what is today's date", "date please",
        "can you tell me the date"
    ],
    "open_youtube": [
        "open youtube", "launch youtube", "go to youtube", "start youtube",
        "take me to youtube", "i want to watch videos on youtube", "youtube please",
        "open you tube", "play youtube"
    ],
    "open_google": [
        "open google", "launch google", "go to google", "start google",
        "take me to google", "open the google website", "google please",
        "open google search", "run google"
    ],
    "search_web": [
        "search python tutorials", "search for machine learning", "google deep learning",
        "look up neural networks", "find information about space", "search cats",
        "search for best laptops", "look up weather forecast", "search how to cook pasta",
        "find news about india"
    ],
    "joke": [
        "tell me a joke", "say something funny", "make me laugh", "joke please",
        "i want to hear a joke", "do you know any jokes", "tell a joke", "crack a joke",
        "got any jokes"
    ],
    "exit": [
        "exit", "quit", "goodbye", "bye jarvis", "close the assistant", "stop jarvis",
        "see you later", "shut down", "bye", "that is all"
    ],
    "who_are_you": [
        "who are you", "what are you", "what is your name", "introduce yourself",
        "tell me about yourself", "are you jarvis", "what can you do",
        "who made you", "what's your name"
    ],
    "open_app": [
        "open calculator", "launch calculator", "start calculator", "open notepad",
        "launch notepad", "start notepad", "open paint", "open command prompt",
        "open file explorer", "launch task manager", "open chrome", "open edge",
        "start the calculator app", "run notepad", "open settings app"
    ],
    "open_website": [
        "open instagram", "open github", "open facebook", "open gmail",
        "go to amazon", "open wikipedia", "open linkedin", "open twitter",
        "launch whatsapp web", "open netflix", "take me to stackoverflow",
        "open the chatgpt website", "go to reddit", "open spotify website",
        "open flipkart"
    ],
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the neural network go to school? To improve its learning rate.",
    "I told my computer I needed a break, and it went to sleep.",
]
