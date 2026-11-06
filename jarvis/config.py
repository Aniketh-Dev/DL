"""
Configuration and constants for JARVIS.
"""

import os
import sys
import random
from pathlib import Path
import torch

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"

# Audio Settings
SAMPLE_RATE = 16000          # Whisper sample rate (16 kHz)
DEFAULT_RECORD_SECONDS = 5   # Default audio listening window
WHISPER_MODEL_NAME = "tiny"
WHISPER_DEVICE = "cpu"
WHISPER_COMPUTE_TYPE = "int8"

# Model Hyperparameters
HIDDEN_DIM = 16
LEARNING_RATE = 0.01
NUM_EPOCHS = 200
TEST_SIZE = 0.2
RANDOM_SEED = 0
CONFIDENCE_THRESHOLD = 0.6

# Desktop Applications Mapping (Spoken Name -> Windows Command)
APPS = {
    "calculator": "calc",
    "notepad": "notepad",
    "paint": "mspaint",
    "command prompt": "cmd",
    "file explorer": "explorer",
    "explorer": "explorer",
    "task manager": "taskmgr",
    "chrome": "chrome",
    "edge": "msedge",
    "settings": "ms-settings:",
}

# Websites Mapping (Spoken Name -> Domain)
SITES = {
    "instagram": "instagram.com",
    "github": "github.com",
    "facebook": "facebook.com",
    "gmail": "mail.google.com",
    "amazon": "amazon.in",
    "wikipedia": "wikipedia.org",
    "linkedin": "linkedin.com",
    "twitter": "x.com",
    "netflix": "netflix.com",
    "stackoverflow": "stackoverflow.com",
    "reddit": "reddit.com",
    "flipkart": "flipkart.com",
    "chatgpt": "chatgpt.com",
    "whatsapp": "web.whatsapp.com",
    "spotify": "open.spotify.com",
}


def setup_environment():
    """Enable ANSI escape colors, UTF-8 symbols, set seeds, and ensure results directory exists."""
    os.system('')
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    torch.manual_seed(RANDOM_SEED)
    random.seed(RANDOM_SEED)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
