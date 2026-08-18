# Proposed Firebase data schema

```text
farms/{farm_id}/plots/{plot_id}/readings/{reading_id}
  timestamp: ISO-8601 UTC string
  device_id: string
  soil_moisture_percent: number
  soil_temperature_c: number
  air_temperature_c: number
  humidity_percent: number
  ph: number|null
  nitrogen_mg_kg: number|null
  phosphorus_mg_kg: number|null
  potassium_mg_kg: number|null
  gas_level: number|null
  sound_level: number|null
  quality: "valid"|"suspect"|"missing"

farms/{farm_id}/plots/{plot_id}/predictions/{prediction_id}
  timestamp: ISO-8601 UTC string
  model_version: string
  prediction_type: string
  result: object|array
  confidence: number|null
  explanation: array<string>
```

Store timestamps in UTC, include units in field names, and validate ranges server-side.

