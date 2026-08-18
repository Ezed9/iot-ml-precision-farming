# System architecture

```text
Sensors → ESP32 → Wi-Fi/MQTT → Firebase real-time backend
                         ↓
                validation and feature preparation
                         ↓
           ML/rule services: crop, irrigation, pest
                         ↓
              mobile app and web dashboard
                         ↓
                   farmer action
```

## Implementation boundary

- **App:** existing teammate work; add under `app/`.
- **Firebase:** real-time sensor storage and app synchronization; credentials and rules must be configured per environment.
- **ML:** this repository includes starter training modules. Production claims require verified datasets, evaluation, and integration tests.
- **Firmware:** add ESP32 code under `firmware/` after the sensor wiring and communication protocol are confirmed.

