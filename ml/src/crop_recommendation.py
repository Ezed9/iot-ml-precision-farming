"""Train and run a crop recommendation classifier."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from xgboost import XGBClassifier

FEATURES = ["nitrogen", "phosphorus", "potassium", "temperature", "humidity", "ph", "rainfall"]
TARGET = "label"


def train_model(csv_path: Path, model_path: Path) -> dict[str, Any]:
    data = pd.read_csv(csv_path)
    missing = sorted(set(FEATURES + [TARGET]) - set(data.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    data = data.dropna(subset=FEATURES + [TARGET])
    encoder = LabelEncoder()
    labels = encoder.fit_transform(data[TARGET].astype(str))
    x_train, x_test, y_train, y_test = train_test_split(
        data[FEATURES], labels, test_size=0.2, random_state=42, stratify=labels
    )
    model = XGBClassifier(n_estimators=250, max_depth=5, learning_rate=0.05, eval_metric="mlogloss")
    model.fit(x_train, y_train)
    report = classification_report(y_test, model.predict(x_test), target_names=encoder.classes_, output_dict=True)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "encoder": encoder, "features": FEATURES}, model_path)
    return {"model_path": str(model_path), "report": report}


def predict(model_path: Path, values: dict[str, float], top_k: int = 3) -> list[dict[str, float | str]]:
    bundle = joblib.load(model_path)
    frame = pd.DataFrame([[values[name] for name in bundle["features"]]], columns=bundle["features"])
    probabilities = bundle["model"].predict_proba(frame)[0]
    indices = probabilities.argsort()[::-1][:top_k]
    return [{"label": str(bundle["encoder"].inverse_transform([index])[0]), "score": float(probabilities[index])} for index in indices]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-csv", type=Path, required=True)
    parser.add_argument("--model-out", type=Path, required=True)
    args = parser.parse_args()
    result = train_model(args.train_csv, args.model_out)
    print(result)


if __name__ == "__main__":
    main()

