"""
JARVIS - Mini Voice Assistant using Deep Learning
Main entry point for running the assistant.
"""

import sys
from jarvis.config import (
    setup_environment,
    RESULTS_DIR,
    HIDDEN_DIM,
    LEARNING_RATE,
    NUM_EPOCHS,
    WHISPER_MODEL_NAME,
    WHISPER_DEVICE,
    WHISPER_COMPUTE_TYPE,
    DEFAULT_RECORD_SECONDS,
    SAMPLE_RATE,
    CONFIDENCE_THRESHOLD,
)
from jarvis.data.intents import INTENTS
from jarvis.nlp.tokenizer import TextPreprocessor
from jarvis.nlp.model import IntentClassifier
from jarvis.nlp.trainer import train_model, predict_intent
from jarvis.audio.speech_to_text import load_whisper, listen
from jarvis.audio.text_to_speech import speak
from jarvis.actions.handler import run_action


def main():
    # 1. Initialize environment (UTF-8, ANSI terminal colors, seeds, dirs)
    setup_environment()

    # 2. Prepare preprocessor & neural network
    preprocessor = TextPreprocessor(INTENTS)
    model = IntentClassifier(
        input_dim=preprocessor.vocab_size,
        hidden_dim=HIDDEN_DIM,
        output_dim=preprocessor.num_classes,
    )

    # 3. Train intent classifier & save diagnostic curves
    print("Training the intent classifier...\n")
    train_model(
        model=model,
        preprocessor=preprocessor,
        results_dir=RESULTS_DIR,
        epochs=NUM_EPOCHS,
        lr=LEARNING_RATE,
    )

    # 4. Initialize Whisper ASR
    whisper_model = load_whisper(
        model_name=WHISPER_MODEL_NAME,
        device=WHISPER_DEVICE,
        compute_type=WHISPER_COMPUTE_TYPE,
    )

    # 5. JARVIS ready notification
    speak("Jarvis is ready.")

    # 6. Main interaction loop
    running = True
    try:
        while running:
            choice = input("\nPress Enter to speak, or type a command ('q' to quit): ").strip()
            if choice.lower() == "q":
                break

            # Audio voice input or typed fallback
            text = (
                listen(whisper_model, seconds=DEFAULT_RECORD_SECONDS, sample_rate=SAMPLE_RATE)
                if choice == ""
                else choice
            )

            if not text:
                if choice == "":
                    print("No speech detected.")
                continue

            intent, conf = predict_intent(model, text, preprocessor)
            print(f"You said : {text}")
            print(f"Intent   : {intent}  |  Confidence: {conf * 100:.1f}%")

            if intent is None or conf < CONFIDENCE_THRESHOLD:
                speak("Sorry, I did not understand.")
                continue

            running = run_action(intent, text)

    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
