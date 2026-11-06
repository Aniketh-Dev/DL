"""
Model training, evaluation, metrics plotting, and intent inference.
"""

from pathlib import Path
from typing import Tuple, Optional
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

from .tokenizer import TextPreprocessor
from .model import IntentClassifier


def train_model(
    model: IntentClassifier,
    preprocessor: TextPreprocessor,
    results_dir: Path,
    epochs: int = 200,
    lr: float = 0.01,
    test_size: float = 0.2,
    random_state: int = 0,
    verbose: bool = True,
) -> Tuple[list, list, list]:
    """
    Train the IntentClassifier model and save diagnostic graphs to results_dir.
    """
    results_dir = Path(results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)

    X_data, y_data = preprocessor.build_dataset()
    X = torch.tensor(X_data, dtype=torch.float32)
    y = torch.tensor(y_data, dtype=torch.long)

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    losses, train_acc, test_acc = [], [], []

    for epoch in range(1, epochs + 1):
        model.train()
        logits = model(X_tr)
        loss = loss_fn(logits, y_tr)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        model.eval()
        with torch.no_grad():
            tr_acc = (model(X_tr).argmax(1) == y_tr).float().mean().item()
            te_acc = (model(X_te).argmax(1) == y_te).float().mean().item()
            train_acc.append(tr_acc)
            test_acc.append(te_acc)

        losses.append(loss.item())

        if verbose and epoch % 50 == 0:
            print(
                f"Epoch {epoch:3d} | loss {loss.item():.4f} | "
                f"train acc {train_acc[-1]:.2f} | test acc {test_acc[-1]:.2f}"
            )

    # Graph 1: Loss & Accuracy curves
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].plot(losses)
    ax[0].set_title("Training Loss")
    ax[0].set_xlabel("Epoch")

    ax[1].plot(train_acc, label="train")
    ax[1].plot(test_acc, label="test")
    ax[1].set_title("Accuracy")
    ax[1].set_xlabel("Epoch")
    ax[1].legend()

    plt.tight_layout()
    plt.savefig(results_dir / "training_curves.png")
    plt.close()

    # Graph 2: Confusion matrix on test set
    with torch.no_grad():
        pred = model(X_te).argmax(1).numpy()

    cm = confusion_matrix(y_te.numpy(), pred, labels=range(preprocessor.num_classes))
    ConfusionMatrixDisplay(cm, display_labels=preprocessor.labels).plot(xticks_rotation=45)
    plt.tight_layout()
    plt.savefig(results_dir / "confusion_matrix.png")
    plt.close()

    if verbose:
        print("\nClassification report (test set):")
        print(
            classification_report(
                y_te.numpy(),
                pred,
                labels=range(preprocessor.num_classes),
                target_names=preprocessor.labels,
                zero_division=0,
            )
        )
        print(f"Graphs saved in the '{results_dir}' folder.\n")

    return losses, train_acc, test_acc


def predict_intent(
    model: IntentClassifier,
    text: str,
    preprocessor: TextPreprocessor,
) -> Tuple[Optional[str], float]:
    """
    Predict intent name and model confidence.
    Returns (None, 0.0) if no known vocabulary words are detected in the input.
    """
    vec = preprocessor.bag_of_words(text)
    if vec.sum() == 0:
        return None, 0.0

    model.eval()
    with torch.no_grad():
        logits = model(torch.tensor(vec).unsqueeze(0))
        probs = torch.softmax(logits, dim=1)[0]

    conf, idx = torch.max(probs, 0)
    return preprocessor.labels[idx.item()], conf.item()
