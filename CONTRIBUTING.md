# Contributing

## Branches

Use focused branches such as `app-integration`, `firebase-schema`, `ml-crop-recommendation`, or `esp32-firmware`.

## Pull requests

Each pull request should include:

- What changed and why.
- How it was tested.
- Screenshots for UI changes.
- Dataset and model version details for ML changes.
- Any Firebase schema or security-rule changes.

## Secrets and data

Do not commit credentials, Firebase service-account files, private user data, or raw datasets with unclear licenses. Use `.env.example` and documented setup steps instead.

## ML quality bar

Every model change should document the dataset source, feature schema, train/test split, baseline, metrics, model version, and known limitations. A prediction endpoint should return confidence and model metadata.

