"""
Generates a modern, high-resolution architecture and workflow diagram for JARVIS.
Saves to results/architecture_diagram.png.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ensure results directory exists
results_dir = Path(__file__).resolve().parent / "results"
results_dir.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
fig.patch.set_facecolor("#0b0f19")
ax.set_facecolor("#0b0f19")
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis("off")

# Helper function to create stylish rounded cards
def draw_card(ax, x, y, w, h, title, subtitle, icon="◈", border_color="#38bdf8", fill_color="#131c31"):
    # Shadow / Glow
    glow = patches.FancyBboxPatch(
        (x - 0.05, y - 0.05), w + 0.1, h + 0.1,
        boxstyle="round,pad=0.12",
        ec=border_color, fc=fill_color, alpha=0.3, lw=2.5, zorder=2
    )
    ax.add_patch(glow)
    
    # Main Box
    card = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.1",
        ec=border_color, fc=fill_color, lw=1.6, zorder=3
    )
    ax.add_patch(card)
    
    # Header & Text
    ax.text(x + 0.3, y + h - 0.45, f"{icon}  {title}", fontsize=11, fontweight="bold", color="#f8fafc", zorder=4)
    ax.text(x + 0.3, y + h - 0.85, subtitle, fontsize=8.5, color="#94a3b8", zorder=4, linespacing=1.4)

# Helper function for stylish arrows
def draw_flow_arrow(ax, x1, y1, x2, y2, label=""):
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color="#00f2fe", lw=2.2),
        zorder=5
    )
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y + 0.25, label, fontsize=8, color="#38bdf8", ha="center", fontweight="semibold", zorder=6)

# Title Header
ax.text(7, 8.4, "JARVIS SYSTEM ARCHITECTURE & WORKFLOW", fontsize=16, fontweight="bold", color="#00f2fe", ha="center")
ax.text(7, 8.0, "Deep Learning Voice Assistant Pipeline: Speech -> Whisper ASR -> PyTorch NLP -> System Automation",
        fontsize=9.5, color="#94a3b8", ha="center")

# Row 1: Pipeline Flow (Left to Right)
# 1. Microphone Input
draw_card(ax, 0.8, 4.8, 3.4, 2.2, "Voice Input & Visualizer",
          "• sounddevice (16 kHz mono)\n• Real-time RMS audio volume\n• Dynamic ASCII waveform visualizer\n[jarvis/audio/animation.py]",
          icon="[MIC]", border_color="#38bdf8")

# 2. Faster-Whisper ASR
draw_card(ax, 5.3, 4.8, 3.4, 2.2, "Speech-to-Text (ASR)",
          "• Faster-Whisper Transformer ('tiny')\n• 8-bit quantization (int8 CPU)\n• Audio frames -> Text string\n[jarvis/audio/speech_to_text.py]",
          icon="[ASR]", border_color="#818cf8")

# 3. NLP Preprocessing
draw_card(ax, 9.8, 4.8, 3.4, 2.2, "NLP Feature Extractor",
          "• Regex Tokenizer: [a-z']+\n• Vocabulary builder (unique words)\n• Bag-of-Words binary encoding\n[jarvis/nlp/tokenizer.py]",
          icon="[NLP]", border_color="#c084fc")

# Arrows for Row 1
draw_flow_arrow(ax, 4.2, 5.9, 5.3, 5.9, label="Audio Buffer")
draw_flow_arrow(ax, 8.7, 5.9, 9.8, 5.9, label="Text String")

# Arrow from Row 1 to Row 2
draw_flow_arrow(ax, 11.5, 4.8, 11.5, 3.7, label="Vector [0, 1, 0...]")

# Row 2: Inference & Actions
# 4. PyTorch Intent Classifier
draw_card(ax, 9.8, 1.4, 3.4, 2.3, "PyTorch Deep Learning",
          "• Input Layer (Vocab Size)\n• Linear Layer (16 Neurons) + ReLU\n• Output Layer (11 Intent Classes)\n• Softmax Confidence Probabilities\n[jarvis/nlp/model.py]",
          icon="[DNN]", border_color="#f43f5e")

# 5. Action Dispatcher
draw_card(ax, 5.3, 1.4, 3.4, 2.3, "Action Dispatcher",
          "• Confidence Gate (Threshold >= 60%)\n• Native App Launcher (calc, notepad)\n• Web Browser Search & URL resolver\n• System Date / Time / Jokes\n[jarvis/actions/handler.py]",
          icon="[ACT]", border_color="#34d399")

# 6. Text-to-Speech Output
draw_card(ax, 0.8, 1.4, 3.4, 2.3, "Spoken Reply & Feedback",
          "• pyttsx3 offline TTS speech engine\n• Real-time speech synthesis\n• Terminal response output\n• Loop restart for next command\n[jarvis/audio/text_to_speech.py]",
          icon="[TTS]", border_color="#fbbf24")

# Arrows for Row 2 (Right to Left)
draw_flow_arrow(ax, 9.8, 2.5, 8.7, 2.5, label="Intent & Conf")
draw_flow_arrow(ax, 5.3, 2.5, 4.2, 2.5, label="Voice String")

# Arrow returning back to listening
ax.annotate(
    "", xy=(2.5, 4.8), xytext=(2.5, 3.7),
    arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color="#00f2fe", lw=2.0, linestyle="dashed"),
    zorder=5
)
ax.text(2.6, 4.25, "Continuous Loop", fontsize=8, color="#38bdf8", va="center", fontweight="semibold")

plt.tight_layout()
output_path = results_dir / "architecture_diagram.png"
plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()
print(f"Architecture diagram generated successfully: {output_path}")
