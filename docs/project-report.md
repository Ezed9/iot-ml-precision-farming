# IoT-Enabled AI/ML Precision Farming System

## NITM IoT Hackathon / ReGen Hackathon 2025

**Team:** Chicken Legs  
**Institution:** NIT Silchar  
**Problem statement:** Design an IoT system to monitor soil conditions and recommend optimal farming practices.

## 1. Executive summary

This project proposes a smart-farming platform that combines IoT sensing, cloud data storage, machine learning, and a farmer-oriented mobile application. The system collects soil and environmental measurements in near real time, transmits them through an ESP32-based device, stores the readings in a cloud backend, and presents actionable information through an app and dashboard.

The intended outcomes are better irrigation decisions, improved crop selection, earlier pest awareness, reduced resource waste, and more accessible farm monitoring. The supplied presentation shows a working app walkthrough with a splash screen, onboarding screens, a home dashboard, crop recommendations, and irrigation advice. The ML layer is described in the presentation as a planned or proposed extension; it should be implemented and evaluated separately before being claimed as a completed feature.

## 2. Problem and motivation

Farmers often make decisions using experience and periodic observation rather than continuous measurements. This creates several practical problems:

- Soil moisture and temperature can change between manual checks.
- Irrigation may be applied too early, too late, or in excessive quantities.
- Crop selection may not account for soil nutrients and local weather conditions.
- Pest activity may be noticed only after visible crop damage.
- Unexpected weather can disrupt irrigation, fertilization, planting, and harvesting schedules.

The project addresses these problems by making field conditions measurable and turning measurements into understandable recommendations.

## 3. Proposed solution

The proposed solution has five layers:

1. **Sensing layer:** soil moisture, soil temperature, humidity, air temperature, pH, NPK/nutrient, gas, and sound sensing.
2. **Edge/device layer:** an ESP32 collects readings and provides wireless communication. MQTT, Wi-Fi, or LoRa/LoRaWAN are discussed in the supplied material as communication options.
3. **Cloud/data layer:** sensor data is transmitted to a cloud backend. Firebase is used in the app-oriented architecture, while Google Cloud services are described as an alternative or expanded data platform in the architecture material.
4. **Analytics/ML layer:** sensor and weather data are processed to estimate irrigation needs, recommend crops, and detect pest-related sound patterns.
5. **Application layer:** farmers receive real-time readings, alerts, recommendations, and irrigation guidance through a mobile app and web dashboard.

## 4. Existing app demonstrated in the screenshots

The supplied images show the following application flow:

### 4.1 Splash and onboarding

The app opens with a branded splash screen for the team and project. Onboarding screens introduce the precision-farming system and guide the user into the application.

### 4.2 Home dashboard

The home page presents a consolidated view of live or sample farm readings. The screenshots show cards or fields for nitrogen, phosphorus, potassium, gas level, sound level, soil moisture, humidity, temperature, and weekly weather.

### 4.3 Crop recommendation

The app includes a crop recommendation view showing candidate crops such as pomegranate, jute, pigeon pea, coffee, moth bean, chickpea, and watermelon. The intended recommendation engine uses soil nutrients, moisture, temperature, humidity, and weather-related factors to rank suitable crops.

### 4.4 Irrigation advice

The app includes an irrigation-advice screen. The demonstrated message interprets soil-moisture status and indicates when moisture is optimal, reducing unnecessary watering. A production version should make the crop, growth stage, target moisture range, timestamp, and confidence visible.

### 4.5 Remote monitoring and alerts

The project concept allows farmers to monitor their fields remotely. If a parameter crosses a defined threshold, the system can issue an alert and provide a recommended action.

## 5. Hardware and sensing design

The presentation identifies or proposes the following components:

| Component | Role in the system |
|---|---|
| ESP32 | Reads sensors, performs edge-side processing, and communicates with the cloud. |
| Capacitive soil-moisture sensor | Measures soil moisture with better long-term durability than resistive probes. |
| DS18B20 soil-temperature sensor | Measures soil temperature using the 1-Wire protocol. |
| DHT11 | Measures ambient temperature and humidity. |
| pH sensor / glass-electrode sensor | Estimates soil acidity or alkalinity. |
| NPK sensor | Measures or simulates nitrogen, phosphorus, and potassium values. |
| MQ135 gas sensor | Detects selected gases as an environmental/pollution indicator. |
| Sound sensor | Captures sound patterns for proposed pest detection and monitoring. |
| Li-Po battery | Provides portable power for field deployment. |
| MQTT / Wi-Fi / LoRa option | Supports transmission from the device to the cloud. |

The proposed PCB would consolidate the ESP32, power regulation, sensor headers, status LEDs, connectors, and reset controls into a field-ready unit. This PCB and field deployment should be described as future engineering work unless a physical prototype has already been built and tested.

## 6. Data flow and architecture

```text
Sensors → ESP32 → Wireless/MQTT transport → Cloud database
       → validation and preprocessing → ML/rule-based analytics
       → recommendations and alerts → mobile app/web dashboard → farmer action
```

The app-oriented slides describe Firebase for real-time storage and updates. Other slides outline a Google Cloud architecture using Pub/Sub, Cloud Storage, BigQuery, Dataflow, BigQuery ML, and Vertex AI/AutoML. These should be presented as architecture alternatives until the implemented backend is confirmed.

## 7. Machine-learning work plan

This section is the strongest place for your individual contribution. The deck identifies three analytics tasks, but the code, training data, evaluation results, and deployment status still need to be completed.

### 7.1 Crop recommendation model

**Goal:** Recommend crops suited to a plot’s soil and environmental conditions.

**Candidate inputs:** nitrogen, phosphorus, potassium, pH, soil moisture, temperature, humidity, rainfall, wind, and season or location.

**Candidate model:** XGBoost multiclass classifier or ranking model.

**Implementation steps:**

1. Select and document a public agricultural dataset.
2. Align units and feature names with the IoT schema.
3. Handle missing values, outliers, and class imbalance.
4. Split data into training, validation, and test sets without leakage.
5. Train a baseline model before tuning XGBoost.
6. Evaluate accuracy, macro-F1, per-class recall, and confusion matrix.
7. Add feature importance or SHAP-based explanations.
8. Export the model and expose a prediction endpoint or inference module.

### 7.2 Pest detection from sound

**Goal:** Detect likely pest activity from sound-sensor signals.

**Candidate model:** MLP classifier, as proposed in the deck; a CNN on spectrograms is a stronger follow-up if sufficient data is available.

**Implementation steps:**

1. Confirm the source and license of the pest-sound dataset.
2. Convert audio into consistent windows.
3. Extract MFCC, spectral, zero-crossing, and energy features, or generate mel spectrograms.
4. Separate farm background noise from pest-related patterns.
5. Evaluate precision, recall, macro-F1, false-alarm rate, and latency.
6. Return a probability and an “insufficient confidence” state rather than forcing every sound into a pest class.

### 7.3 Irrigation recommendation

**Goal:** Recommend whether and when irrigation is required.

**Initial approach:** A transparent rule-based baseline comparing current soil moisture with the target range for the selected crop and growth stage.

**ML extension:** Predict near-future soil moisture or irrigation need using time-series readings, weather forecasts, crop type, and recent irrigation events.

**Evaluation:** Compare recommendations with agronomic target ranges and, where available, expert labels or measured crop outcomes. Track water saved, missed-irrigation events, and unnecessary-irrigation events.

## 8. Data and model governance

The report should identify the source, license, date, units, and limitations of every dataset. IoT readings should include a device ID, plot ID, timestamp, sensor values, unit, calibration status, and data-quality flag. Training and test data should be separated by farm, plot, or time period where possible to avoid overstating generalization.

The system should record model version, input schema version, prediction timestamp, confidence, and recommendation rationale. Farmers should be able to distinguish a measured value, a rule-based suggestion, and an ML prediction.

## 9. Technology stack

The supplied material mentions ESP32 and sensors on the hardware side; Firebase, Arduino IDE, Kotlin, Python, and TensorFlow in the software ecosystem; and XGBoost for prediction. It also discusses MQTT, Google Cloud services, Flutter, Figma, and Ethereum/blockchain as proposed technologies. The final GitHub README should list only technologies present in the actual code and tested deployment, with a separate “planned” section for the rest.

## 10. Impact and benefits

- **Water conservation:** irrigation advice can reduce overwatering and support more precise scheduling.
- **Lower manual effort:** remote monitoring reduces the need for repeated field checks.
- **Earlier intervention:** alerts and sound-based pest signals may help farmers act before severe damage.
- **Better crop selection:** soil and weather features can make crop choice more evidence-based.
- **Accessibility:** a mobile-first interface, simple visuals, local-language support, and offline capability can make the system useful to farmers with limited technical experience.
- **Scalability:** a modular sensor and cloud architecture can support small demonstration plots and larger deployments.

## 11. Challenges and limitations

The project material identifies farmer awareness and cost efficiency as challenges. Additional technical risks include sensor calibration, sensor drift, missing network connectivity, noisy sound data, regional variation in soil conditions, limited labeled datasets, cloud costs, and false alerts. The system should be validated in real farms across multiple soil types and seasons before making claims about yield improvement.

## 12. Future scope

The presentation proposes automated IoT-controlled pumps, solar power, a regional-language voice assistant, broader sensor integration, and blockchain-backed data integrity. These are useful extensions, but they should remain future scope until implemented and tested. A practical next milestone is to finish the ML pipeline and connect one prediction endpoint to the existing app using a documented JSON contract.

## 13. Suggested contribution statement

Use the following wording only after you complete the corresponding work:

> Contributed to the development of an IoT-enabled precision-farming platform by designing and implementing machine-learning pipelines for crop recommendation, irrigation decision support, and pest-sound classification; prepared sensor data for model training, evaluated model performance, and integrated prediction outputs with the farmer-facing application.

For the current state, a safer statement is:

> Worked as part of a team on an IoT-based precision-farming application concept and app demonstration; responsible for extending the project with the machine-learning pipeline and evaluation layer.

## 14. Resume-ready project description

**IoT-Enabled AI/ML Precision Farming System — ReGen Hackathon 2025, NIT Silchar**  
Designed a smart-farming system that combines ESP32-based soil and environmental sensing, cloud data storage, and a farmer-facing mobile application to provide real-time monitoring, crop recommendations, irrigation guidance, and proposed pest detection. Developing the ML layer using sensor, weather, and audio features, with XGBoost/MLP model candidates and evaluation focused on recommendation quality, false alerts, and water-use efficiency.

### Resume bullet options after implementation

- Built a sensor-to-cloud pipeline using ESP32 and Firebase to collect and visualize soil moisture, temperature, humidity, gas, sound, pH, and nutrient data.
- Trained and evaluated an XGBoost crop-recommendation model using soil and weather features, reporting macro-F1, confusion matrix, and feature-importance results.
- Developed a pest-sound classification pipeline using audio features/spectrograms and reported precision, recall, false-alarm rate, and inference latency.
- Integrated model outputs into a mobile dashboard that provides crop suggestions, irrigation advice, alerts, confidence values, and recommendation explanations.

Do not include metrics until you have measured them.

## 15. GitHub repository recommendation

```text
precision-farming-iot-ml/
├── README.md
├── app/                    # Existing mobile/web application
├── firmware/               # ESP32 firmware and sensor integrations
├── ml/
│   ├── crop_recommendation/
│   ├── pest_detection/
│   ├── irrigation/
│   ├── notebooks/
│   └── requirements.txt
├── data/README.md          # Sources and schemas; do not commit private data
├── backend/                # API/cloud functions, if applicable
├── docs/
│   ├── architecture.md
│   ├── data-schema.md
│   └── project-report.md
├── assets/                 # Screenshots and diagrams
└── LICENSE
```

## 16. Details to confirm before publishing

- Exact app framework and repository ownership.
- Which Firebase services are actually used.
- Whether the ESP32 and sensors are physically assembled and tested.
- Exact sensor models and calibration procedure.
- Whether NPK values are simulated or measured in the demo.
- Dataset names, licenses, row counts, and label definitions.
- Trained model versions and evaluation metrics.
- API contract between the ML service and the app.
- Team roles and your specific contribution.
- Screenshots or a screen recording showing the final app state.

