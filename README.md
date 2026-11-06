# 🎙️ JARVIS - Mini Voice Assistant using Deep Learning

An intelligent, modular voice assistant powered by **Faster-Whisper** and a custom **PyTorch Neural Network** for real-time speech recognition, intent classification, and system automation.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Whisper](https://img.shields.io/badge/ASR-Faster--Whisper-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🧠 Deep Learning Architecture

JARVIS utilizes deep learning in two key stages:

```
[Voice Input via Microphone]
          │
          ▼
   (Faster-Whisper)          <-- Pretrained Transformer ASR
          │
      Text Query
          │
          ▼
  (IntentClassifier)         <-- Custom PyTorch Neural Network (Trained on startup)
          │
   Predicted Intent + Confidence
          │
          ▼
   [Action Dispatcher]       <-- Web search, system app launcher, TTS speech reply
```

1. **Speech-to-Text (ASR)**: Uses OpenAI's **Whisper** (via `faster-whisper`), an advanced Transformer sequence-to-sequence model quantized to int8 for rapid CPU inference.
2. **Intent Classification (NLP)**: A custom PyTorch feedforward neural network that converts sentences into Bag-of-Words representations and classifies user queries into executable actions.

---

## 📁 Repository Structure

```
split-files-jarvis/
├── jarvis/
│   ├── __init__.py            # Package initialization
│   ├── config.py              # System configuration, apps, websites, hyperparameters
│   ├── data/
│   │   ├── __init__.py
│   │   └── intents.py         # Intent categories, training sentences, and jokes
│   ├── nlp/
│   │   ├── __init__.py
│   │   ├── tokenizer.py       # Tokenization, vocabulary, and Bag-of-Words builder
│   │   ├── model.py           # PyTorch IntentClassifier neural network architecture
│   │   └── trainer.py         # Training loop, evaluation metrics, and inference logic
│   ├── audio/
│   │   ├── __init__.py
│   │   ├── animation.py       # Real-time sci-fi terminal waveform & audio visualizer
│   │   ├── speech_to_text.py  # Faster-Whisper model loading and microphone recording
│   │   └── text_to_speech.py  # pyttsx3 voice response engine
│   └── actions/
│       ├── __init__.py
│       ├── app_launcher.py    # Desktop applications and website launcher
│       └── handler.py         # Intent action dispatcher and query extraction
├── results/                   # Auto-generated loss curves and confusion matrix
│   └── .gitkeep
├── main.py                    # Main application runner
├── jarvis.py                  # Entrypoint alias (`python jarvis.py`)
├── requirements.txt           # Project dependencies
├── .gitignore                 # Standard Python gitignore rules
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

---

## ⚡ Features & Supported Intents

| Intent | Example Commands | Action Performed |
|---|---|---|
| `greeting` | *"Hello", "Hi Jarvis", "Good morning"* | Speaks friendly greeting |
| `time` | *"What time is it?", "Current time"* | Speaks current system time |
| `date` | *"What is the date today?", "Today's date"* | Speaks current date |
| `open_youtube` | *"Open YouTube", "Launch YouTube"* | Opens YouTube in default browser |
| `open_google` | *"Open Google", "Launch Google"* | Opens Google search homepage |
| `search_web` | *"Search machine learning", "Google Python tutorials"* | Strips stop words and searches Google |
| `joke` | *"Tell me a joke", "Make me laugh"* | Tells a programming / AI joke |
| `who_are_you` | *"Who are you?", "Introduce yourself"* | Explains assistant identity |
| `open_app` | *"Open calculator", "Launch notepad", "Start paint"* | Launches native Windows desktop app |
| `open_website` | *"Open github", "Open chatgpt", "Go to reddit"* | Opens matching website domain |
| `exit` | *"Exit", "Quit", "Goodbye", "Bye Jarvis"* | Says goodbye and safely exits |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage

### Quick Start (Windows One-Click Launcher)
Simply double-click **`run_jarvis.bat`** in File Explorer! It automatically checks Python, activates your virtual environment, verifies dependencies, and starts JARVIS.

---

### Command Line
You can also run directly from any terminal:

```bash
python main.py
```
*or*
```bash
python jarvis.py
```

### Interacting with JARVIS:
- **Voice Mode**: Press **Enter** to speak into your microphone for 5 seconds. You will see a live ASCII audio wave reacting to your voice volume.
- **Text Mode**: Type your command directly into the prompt (useful when no microphone is connected).
- **Quit**: Type `q` or press `Ctrl + C` anytime to exit.

---

## 📊 Training & Evaluation Graphs

When JARVIS launches, the neural network automatically trains on the intent dataset and outputs:
- **Training Loss & Accuracy Curves**: Saved to `results/training_curves.png`.
- **Confusion Matrix & Classification Report**: Saved to `results/confusion_matrix.png`.

---

## 🛠️ Customization

- **Add New Intents**: Open `jarvis/data/intents.py` and add entries to the `INTENTS` dictionary.
- **Add Desktop Apps**: Open `jarvis/config.py` and map new app names to commands in the `APPS` dictionary.
- **Add Websites**: Add domains to the `SITES` dictionary in `jarvis/config.py`.

---

## 📜 License

This project is open-source and licensed under the [MIT License](LICENSE).
