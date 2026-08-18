"""Train an MLP classifier on precomputed pest-sound features."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler


def train_model(csv_path: Path, model_path: Path) -> dict[str, Any]:
    data = pd.read_csv(csv_path).dropna()
    if "label" not in data.columns:
        raise ValueError("The pest CSV must contain a label column")
    features = [column for column in data.columns if column != "label"]
    if not features:
        raise ValueError("The pest CSV must contain at least one feature column")
    encoder = LabelEncoder()
    x = StandardScaler().fit_transform(data[features])
    y = encoder.fit_transform(data["label"].astype(str))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
    model = MLPClassifier(hidden_layer_sizes=(128, 64), early_stopping=True, random_state=42, max_iter=500)
    model.fit(x_train, y_train)
    report = classification_report(y_test, model.predict(x_test), target_names=encoder.classes_, output_dict=True)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "encoder": encoder, "features": features}, model_path)
    return {"model_path": str(model_path), "report": report}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-csv", type=Path, required=True)
    parser.add_argument("--model-out", type=Path, required=True)
    args = parser.parse_args()
    print(train_model(args.train_csv, args.model_out))


if __name__ == "__main__":
    main()

