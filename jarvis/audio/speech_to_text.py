"""
Speech-to-text transcription module using Faster-Whisper.
"""

from typing import Optional
from .animation import ListeningAnimation


def load_whisper(
    model_name: str = "tiny",
    device: str = "cpu",
    compute_type: str = "int8"
):
    """
    Load the Faster-Whisper model. Downloads the weights on the first run.
    """
    try:
        from faster_whisper import WhisperModel
        print("Loading Whisper (first run downloads the model)...")
        return WhisperModel(model_name, device=device, compute_type=compute_type)
    except Exception as e:
        print("Whisper not available, you can still type commands.", e)
        return None


def listen(
    whisper_model,
    seconds: float = 5.0,
    sample_rate: int = 16000
) -> str:
    """
    Record audio from the microphone with dynamic animation and transcribe using Whisper.
    """
    if whisper_model is None:
        print("Whisper is not available. Please type your command instead.")
        return ""

    anim = None
    try:
        import sounddevice as sd
        # Start recording in background buffer
        audio = sd.rec(
            int(seconds * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="float32",
        )

        # Launch terminal soundwave animation
        anim = ListeningAnimation(duration=seconds, audio_buffer=audio, sample_rate=sample_rate)
        anim.start()

        # Wait until recording duration completes
        sd.wait()

        # Switch animation to transcription status
        anim.set_processing()
        segments, _ = whisper_model.transcribe(audio.flatten(), language="en")
        return " ".join(seg.text for seg in segments).strip()
    except KeyboardInterrupt:
        return ""
    except Exception as e:
        print("\nMicrophone or Whisper problem:", e)
        return ""
    finally:
        if anim:
            anim.stop()
