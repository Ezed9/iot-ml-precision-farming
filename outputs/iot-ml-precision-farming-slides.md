# Slide-by-slide presentation plan

## Slide 1 — Title and team

**Title:** IoT-Enabled AI/ML Precision Farming System  
**Include:** ReGen Hackathon 2025, NIT Silchar, Team Chicken Legs, team members.  
**Visual:** Existing team/title artwork.

## Slide 2 — Problem statement

**Message:** Monitor soil conditions and recommend optimal farming practices.  
**Visual:** One concise problem statement with a farm image or sensor illustration.

## Slide 3 — Why this problem matters

**Cover:** Traditional decision-making, no continuous soil visibility, irrigation uncertainty, crop-selection guesswork, pest damage, and weather uncertainty.  
**Speaker point:** These are decision-quality and timing problems, not just data-collection problems.

## Slide 4 — Proposed solution

**Cover:** IoT sensing + cloud + ML analytics + farmer app.  
**Visual:** Five-layer architecture diagram.

## Slide 5 — Product features

**Cover:** Remote monitoring, alerts, irrigation advice, crop recommendation, pest detection, and future weather integration.  
**Visual:** Feature icons or a compact user-flow diagram.

## Slide 6 — Hardware and sensors

**Cover:** ESP32, capacitive soil-moisture sensor, DS18B20, DHT11, pH, NPK, MQ135, sound sensor, and battery.  
**Visual:** Labeled hardware collage.

## Slide 7 — IoT data flow

**Cover:** Sensors collect readings; ESP32 processes/transmits; cloud stores data; analytics generates insights; app presents actions.  
**Visual:** Arrow-based workflow.

## Slide 8 — Cloud and data architecture

**Cover:** Firebase real-time storage for the app-oriented design. Mention Google Cloud Pub/Sub, Storage, BigQuery, Dataflow, and Vertex AI only as an expanded/proposed architecture if not implemented.  
**Visual:** Data pipeline with “implemented” and “planned” labels.

## Slide 9 — App walkthrough

**Cover:** Splash screen, onboarding, home dashboard, crop recommendation, and irrigation advice.  
**Visual:** Use screenshots 15–16 as a five-panel walkthrough.

## Slide 10 — Crop recommendation ML

**Cover:** Soil nutrients, moisture, temperature, humidity, and weather → crop ranking.  
**Model:** XGBoost candidate.  
**Visual:** Feature-to-recommendation diagram and evaluation metrics placeholder.

## Slide 11 — Pest detection and irrigation intelligence

**Cover:** Sound patterns → pest-risk classification; soil moisture + crop target range → irrigation advice.  
**Models:** MLP candidate for sound; transparent rules first for irrigation, then time-series ML.  
**Visual:** Two-panel analytics flow.

## Slide 12 — ML implementation plan

**Cover:** Dataset sourcing, cleaning, feature engineering, train/validation/test split, evaluation, model export, API integration, and monitoring.  
**Visual:** Milestone timeline.  
**Important:** Label this as your planned/current contribution until completed.

## Slide 13 — Benefits and impact

**Cover:** Save water and effort, reduce crop losses, improve crop selection, and make smart farming more accessible.  
**Visual:** Benefit-to-outcome mapping.

## Slide 14 — Challenges, future scope, and conclusion

**Cover:** Awareness, cost, connectivity, calibration, data quality, and model reliability. Future scope includes automated pumps, solar power, regional-language voice assistance, and broader deployment.  
**Closing line:** Make farm decisions measurable, timely, and actionable.

