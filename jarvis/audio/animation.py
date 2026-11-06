"""
Terminal animation displaying a sci-fi audio soundwave and spinner.
"""

import sys
import time
import math
import threading
import numpy as np


class ListeningAnimation:
    """Animates a sci-fi audio soundwave and spinner in the terminal while JARVIS listens."""
    def __init__(self, duration: float = 5.0, audio_buffer=None, sample_rate: int = 16000):
        self.duration = float(duration)
        self.audio_buffer = audio_buffer
        self.sample_rate = sample_rate
        self.stop_event = threading.Event()
        self.thread = None
        self.mode = "listening"  # "listening" or "processing"

    def _animate(self):
        spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        bars = [' ', '▂', '▃', '▄', '▅', '▆', '▇', '█']
        start_time = time.time()
        frame = 0

        while not self.stop_event.is_set():
            frame += 1
            spin = spinners[frame % len(spinners)]

            if self.mode == "listening":
                elapsed = time.time() - start_time

                # Detect microphone volume from the live audio recording buffer
                rms = 0.0
                if self.audio_buffer is not None:
                    curr_sample = int(elapsed * self.sample_rate)
                    chunk = self.audio_buffer[max(0, curr_sample - 800):curr_sample]
                    if len(chunk) > 0:
                        rms = float(np.sqrt(np.mean(chunk**2)))

                # Voice boost scales wave height when user speaks
                voice_boost = min(1.0, rms * 18.0)
                num_bars = 12
                chars = []
                for i in range(num_bars):
                    dist = abs(i - (num_bars - 1) / 2.0)
                    center_bias = 1.0 - (dist / (num_bars / 2.0)) * 0.35
                    w1 = math.sin(elapsed * 7.0 + i * 0.6)
                    w2 = math.cos(elapsed * 4.0 - i * 0.4)
                    wave = (w1 + w2 + 2.0) / 4.0
                    val = wave * center_bias * (0.35 + 0.65 * voice_boost)
                    idx = min(len(bars) - 1, max(0, int(val * len(bars))))
                    chars.append(bars[idx])
                wave_str = " ".join(chars)

                curr_sec = min(elapsed, self.duration)
                time_str = f"{curr_sec:.1f}s / {self.duration:.1f}s"
                line = (
                    f"\r\033[1;36m🎙️  [JARVIS LISTENING]\033[0m "
                    f"\033[1;33m{spin}\033[0m  "
                    f"\033[1;36m{wave_str}\033[0m "
                    f"\033[90m(Speak now... {time_str})\033[0m\033[K"
                )
            else:  # processing / transcribing audio
                dots = "." * ((frame // 3) % 4)
                line = (
                    f"\r\033[1;35m⚡ [JARVIS PROCESSING]\033[0m "
                    f"\033[1;33m{spin}\033[0m  "
                    f"\033[95m░▒▓█▓▒░\033[0m  "
                    f"\033[97mTranscribing voice{dots:<3}\033[0m\033[K"
                )

            try:
                sys.stdout.write(line)
                sys.stdout.flush()
            except Exception:
                pass
            time.sleep(0.08)

        # Cleanly erase the animation line when finished
        try:
            sys.stdout.write("\r\033[K")
            sys.stdout.flush()
        except Exception:
            pass

    def start(self):
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._animate, daemon=True)
        self.thread.start()

    def set_processing(self):
        self.mode = "processing"

    def stop(self):
        self.stop_event.set()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=0.5)
