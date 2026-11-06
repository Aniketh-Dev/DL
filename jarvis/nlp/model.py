"""
PyTorch Neural Network for Intent Classification.
"""

import torch.nn as nn


class IntentClassifier(nn.Module):
    """
    Feedforward Neural Network for Intent Classification.
    Structure: Input (vocab size) -> Linear -> ReLU -> Linear -> Output (intents count)
    """
    def __init__(self, input_dim: int, hidden_dim: int = 16, output_dim: int = 11):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.network(x)
