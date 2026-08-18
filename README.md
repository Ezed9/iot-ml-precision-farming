# IoT-ML Precision Farming

An IoT-enabled precision-farming platform for real-time soil monitoring and data-driven farming recommendations.

> ReGen Hackathon 2025 · NIT Silchar · Team Chicken Legs

## Project overview

The system combines an ESP32 and agricultural sensors with a real-time cloud backend and a farmer-facing application. It is designed to collect soil and environmental data, display farm conditions, recommend suitable crops, provide irrigation guidance, and support early pest-risk detection from sound data.

The repository is organized so the existing app can be added by the teammate while the ML work can be developed independently and integrated through a documented data contract.

## Current status

- App concept and screen flow documented from the team demo.
- Firebase real-time data integration documented; credentials are intentionally excluded.
- ML starter modules added for crop recommendation, irrigation baseline, and pest-sound classification.
- Model training requires a verified dataset, feature schema, and measured evaluation results.
- ESP32 firmware and final app source are to be added by the respective contributors.

## Repository structure

```text
app/                  Existing mobile/web app (teammate contribution)
firmware/             ESP32 firmware and sensor integrations
ml/                   Training and inference modules
backend/              Firebase functions/API integration, if applicable
firebase/             Firebase setup and data-contract documentation
data/                 Dataset documentation; private/raw data is ignored
docs/                 Architecture, report, and presentation plan
assets/               Screenshots, diagrams, and demo media
```

## Quick start: ML workspace

```bash
cd ml
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The modules accept CSV files with documented column names. Do not commit private or unlicensed datasets. See [`ml/README.md`](ml/README.md) before training.

## Firebase setup

1. Create or select a Firebase project.
2. Enable Realtime Database or Firestore according to the app implementation.
3. Configure the Android/web app using Firebase's generated client configuration.
4. Add database rules appropriate for development and production.
5. Never commit service-account JSON files, API keys intended to be secret, or `.env` files.

The proposed sensor record schema is documented in [`firebase/data-schema.md`](firebase/data-schema.md).

## Integration contract

The app should consume predictions through a stable response containing:

```json
{
  "model_version": "crop-xgb-v1",
  "prediction_type": "crop_recommendation",
  "plot_id": "plot-001",
  "timestamp": "2025-03-25T10:30:00Z",
  "result": [{"label": "chickpea", "score": 0.82}],
  "confidence": 0.82,
  "explanation": ["soil nitrogen is within the training range"]
}
```

Predictions must be distinguishable from raw sensor readings and rule-based advice.

## Resume note

Add measured metrics only after training and evaluation. Avoid describing proposed models as production features until the dataset, code, integration, and results are reproducible.

## Documentation

- [`docs/project-report.md`](docs/project-report.md)
- [`docs/slides.md`](docs/slides.md)
- [`docs/architecture.md`](docs/architecture.md)
- [`ml/README.md`](ml/README.md)
- [`firebase/README.md`](firebase/README.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

