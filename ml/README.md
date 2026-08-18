# Machine-learning modules

These are reproducible starter modules for the ML layer described in the project presentation. They are intentionally dataset-agnostic: the team must verify and document the dataset before training.

## Modules

- `src/crop_recommendation.py`: XGBoost crop classifier with a scikit-learn fallback.
- `src/irrigation.py`: transparent irrigation decision baseline.
- `src/pest_detection.py`: MLP classifier for precomputed audio features.

## Dataset contracts

### Crop recommendation CSV

Required feature columns: `nitrogen`, `phosphorus`, `potassium`, `temperature`, `humidity`, `ph`, `rainfall`. Target column: `label`.

### Pest feature CSV

Required numeric feature columns can be MFCC, spectral, energy, and zero-crossing features. Target column: `label`.

### Irrigation input

The rule baseline expects current moisture, crop target minimum/maximum moisture, and an optional rain forecast.

## Example commands

```bash
python -m src.crop_recommendation --train-csv data/crop.csv --model-out models/crop-xgb.joblib
python -m src.pest_detection --train-csv data/pest_features.csv --model-out models/pest-mlp.joblib
```

Model artifacts are ignored by Git. Store release artifacts in an approved model registry or attach them to a versioned release after reviewing size and privacy constraints.

