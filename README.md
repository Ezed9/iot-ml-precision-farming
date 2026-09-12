# IoT-ML Precision Farming

**An IoT-enabled precision-farming platform for real-time soil monitoring, intelligent crop recommendations, irrigation guidance, and early pest-risk detection.**

> **ReGen Hackathon 2025 · NIT Silchar · Team Chicken Legs**

## Overview

IoT-ML Precision Farming combines **ESP32-based sensing, cloud connectivity, machine learning, and a farmer-facing application** to support data-driven agricultural decisions.

The system collects soil and environmental parameters from sensors, sends them to a cloud backend, and uses the collected data to provide actionable insights such as:

* **Crop recommendation** based on soil and environmental conditions
* **Irrigation guidance** using soil-moisture data
* **Pest-risk detection** using agricultural sound data
* **Real-time farm monitoring** through the application
* **Cloud-based data synchronization** using Firebase

The project is structured to allow the **ML pipeline, firmware, backend, and application** to be developed independently and integrated through defined interfaces.

---

## System Architecture

```text
        ┌─────────────────────┐
        │   Agricultural      │
        │      Sensors        │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │       ESP32         │
        │ Sensor Acquisition  │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Firebase / Cloud   │
        │   Real-time Data     │
        └──────────┬──────────┘
                   │
          ┌────────┴─────────┐
          ▼                  ▼
 ┌─────────────────┐  ┌─────────────────┐
 │   ML Pipeline   │  │  Farmer App     │
 │                 │  │                 │
 │ Crop Prediction │  │ Monitoring      │
 │ Irrigation      │  │ Recommendations │
 │ Pest Detection  │  │ Alerts          │
 └────────┬────────┘  └─────────────────┘
          │
          ▼
 ┌─────────────────────┐
 │  Farming Insights   │
 │ & Recommendations   │
 └─────────────────────┘
```

---

## Features

### Crop Recommendation

The ML pipeline uses soil and environmental parameters to recommend crops suited to the observed conditions.

Example inputs may include:

* Soil nitrogen
* Soil phosphorus
* Soil potassium
* Soil pH
* Temperature
* Humidity
* Rainfall

The model interface is designed to support multiple candidate crops with confidence scores.

### Irrigation Guidance

Soil-moisture measurements can be used to determine whether irrigation may be required.

The initial implementation provides a **baseline irrigation model/rule system**, which can later be replaced or extended with a trained ML model once sufficient field data is available.

### Pest-Sound Classification

The project includes a starter pipeline for classifying agricultural sound recordings.

The intended workflow is:

```text
Audio
  ↓
Pre-processing
  ↓
Feature Extraction
  ↓
ML Classifier
  ↓
Pest / Non-pest or Pest Class
```

Model performance should only be reported after training and evaluation on a verified dataset.

### Real-Time Monitoring

The application can consume sensor data from the Firebase backend and present farm conditions to the user.

Raw sensor measurements and ML-generated predictions are kept conceptually separate.

---

## Repository Structure

```text
IoT-ML-Precision-Farming/
│
├── app/                  # Farmer-facing application
├── firmware/             # ESP32 firmware and sensor integration
├── ml/                   # ML training and inference
├── backend/              # Backend/API integration
├── firebase/             # Firebase configuration & data contracts
├── data/                 # Dataset documentation
├── docs/                 # Architecture, report & presentation
├── assets/               # Screenshots, diagrams & demo media
│
├── README.md
└── CONTRIBUTING.md
```

Private/raw datasets and credentials should **not** be committed to the repository.

---

## ML Workspace

### Setup

```bash
cd ml

python3 -m venv .venv
```

Activate the environment:

**Linux/macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

See [`ml/README.md`](ml/README.md) for dataset requirements, feature schemas, training instructions, and inference details.

### ML Modules

| Module              | Purpose                                                   |
| ------------------- | --------------------------------------------------------- |
| Crop Recommendation | Predict suitable crops from soil/environmental features   |
| Irrigation          | Provide irrigation guidance from soil-moisture conditions |
| Pest Detection      | Classify agricultural sounds for pest-risk detection      |

> **Note:** Model names, accuracy, precision, recall, F1-score, and other metrics should only be added after reproducible training and evaluation.

---

## Firebase

Firebase is used as the proposed cloud layer for synchronizing sensor data and application data.

### Setup

1. Create or select a Firebase project.
2. Enable **Realtime Database or Firestore**, depending on the application implementation.
3. Configure the Android/web application using the generated Firebase configuration.
4. Configure appropriate development and production database rules.
5. Keep credentials and environment-specific configuration outside version control.

The proposed sensor data contract is documented in:

[`firebase/data-schema.md`](firebase/data-schema.md)

### Security

**Never commit:**

```text
.env
service-account.json
google-services.json*   # when it contains environment-specific secrets/configuration
private datasets
private API credentials
```

Use environment variables or an appropriate secret-management mechanism for sensitive configuration.

---

## ML Integration Contract

ML predictions are exposed through a stable response structure so that the application can consume predictions independently of the underlying model.

Example:

```json
{
  "model_version": "crop-xgb-v1",
  "prediction_type": "crop_recommendation",
  "plot_id": "plot-001",
  "timestamp": "2025-03-25T10:30:00Z",
  "result": [
    {
      "label": "chickpea",
      "score": 0.82
    }
  ],
  "confidence": 0.82,
  "explanation": [
    "soil nitrogen is within the training range"
  ]
}
```

### Prediction fields

| Field             | Description                                    |
| ----------------- | ---------------------------------------------- |
| `model_version`   | Version of the model generating the prediction |
| `prediction_type` | Type of ML prediction                          |
| `plot_id`         | Identifier of the monitored plot               |
| `timestamp`       | Prediction timestamp                           |
| `result`          | Predicted class/classes and scores             |
| `confidence`      | Overall prediction confidence                  |
| `explanation`     | Human-readable reasoning where available       |

ML predictions must remain distinguishable from:

* Raw sensor readings
* Rule-based recommendations
* System alerts

This allows the application to evolve without tightly coupling it to a particular ML implementation.

---

## Development Status

| Component                 | Status                     |
| ------------------------- | -------------------------- |
| Project architecture      | 🟢 Defined                 |
| Application concept       | 🟢 Defined                 |
| Firebase data integration | 🟡 In development          |
| ESP32 firmware            | 🟡 In development          |
| Crop recommendation       | 🟡 ML starter pipeline     |
| Irrigation guidance       | 🟡 Baseline implementation |
| Pest-sound classification | 🟡 ML starter pipeline     |
| Verified ML dataset       | 🔴 Required                |
| Model evaluation          | 🔴 Pending                 |
| Full system integration   | 🔴 Pending                 |

The project is under active development. Some components represent **proposed or starter implementations** rather than production-ready functionality.

---

## Documentation

* [`docs/project-report.md`](docs/project-report.md) — Project report
* [`docs/slides.md`](docs/slides.md) — Presentation outline
* [`docs/architecture.md`](docs/architecture.md) — System architecture
* [`ml/README.md`](ml/README.md) — ML pipeline documentation
* [`firebase/README.md`](firebase/README.md) — Firebase setup
* [`CONTRIBUTING.md`](CONTRIBUTING.md) — Contribution guidelines

---

## Team

**Team Chicken Legs**
ReGen Hackathon 2025 · NIT Silchar

---

## Disclaimer

This project is a **prototype/research-oriented precision-farming system** developed for the ReGen Hackathon.

ML recommendations depend on the quality, coverage, and representativeness of the training data. Predictions should therefore be treated as decision-support information rather than a replacement for professional agricultural expertise.

---

## Resume / Portfolio Note

When describing this project on a resume or portfolio, use **measured results** rather than proposed capabilities.

For example:

> **IoT-ML Precision Farming** — Developed an ESP32-based precision-farming prototype integrating agricultural sensors, Firebase cloud synchronization, and ML pipelines for crop recommendation, irrigation guidance, and pest-sound classification.

Add model architecture and evaluation metrics only after the corresponding experiments have been completed and are reproducible.
