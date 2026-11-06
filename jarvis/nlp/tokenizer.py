"""
Text tokenization and Bag-of-Words feature extraction.
"""

import re
from typing import List, Dict, Tuple
import numpy as np


def tokenize(sentence: str) -> List[str]:
    """
    Lowercase the sentence and extract words matching [a-z']+.
    """
    return re.findall(r"[a-z']+", sentence.lower())


class TextPreprocessor:
    """
    Handles vocabulary creation, dataset encoding, and Bag-of-Words vectorization.
    """
    def __init__(self, intents: Dict[str, List[str]]):
        self.intents = intents
        self.labels = list(intents.keys())
        self.sentences = [s for intent in self.labels for s in intents[intent]]
        self.targets = [i for i, intent in enumerate(self.labels) for _ in intents[intent]]

        # Vocabulary: all unique words across the dataset
        self.vocab = sorted({w for s in self.sentences for w in tokenize(s)})
        self.word_to_index = {w: i for i, w in enumerate(self.vocab)}

    @property
    def vocab_size(self) -> int:
        return len(self.vocab)

    @property
    def num_classes(self) -> int:
        return len(self.labels)

    def bag_of_words(self, sentence: str) -> np.ndarray:
        """
        Convert a sentence into a binary vector of size len(vocab):
        1.0 if the word appears in the sentence, 0.0 otherwise.
        """
        vec = np.zeros(self.vocab_size, dtype=np.float32)
        for w in tokenize(sentence):
            if w in self.word_to_index:
                vec[self.word_to_index[w]] = 1.0
        return vec

    def build_dataset(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Build feature matrix X and label vector y for training.
        """
        X = np.array([self.bag_of_words(s) for s in self.sentences])
        y = np.array(self.targets)
        return X, y
