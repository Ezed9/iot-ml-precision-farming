# Firebase integration

Firebase is the proposed real-time data layer for sensor readings and app updates. Confirm whether the final app uses Realtime Database or Cloud Firestore before implementing production rules.

## Development checklist

1. Create a Firebase project.
2. Register the app and configure the Firebase client SDK.
3. Create a development database.
4. Add authentication before exposing farm data outside a local demo.
5. Add rules that scope data by user and plot.
6. Add a Cloud Function or backend service if server-side validation or ML inference is required.
7. Keep credentials out of Git.

See [`data-schema.md`](data-schema.md) for the proposed schema.

