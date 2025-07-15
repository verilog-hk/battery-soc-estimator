🔋 Battery SoC Estimator using ML & Smoothing Techniques

This project predicts the State of Charge (SoC) of a battery using supervised machine learning (ML) models trained on synthetic battery data. It combines signal smoothing (moving average filtering) with model-based predictions to improve stability and real-world usability for Battery Management Systems (BMS).

---

## 🧠 Overview

In BMS systems, raw SoC predictions often fluctuate due to sensor noise and dynamic loads. This project aims to:

- 📊 Use **ML models** (Linear Regression, Random Forest) for accurate SoC prediction.
- 🧹 Apply **signal smoothing** to eliminate spikes in prediction.
- 🧪 Use synthetic data to simulate real-world conditions.

---

## 📁 Folder Structure

| Folder         | Description |
|----------------|-------------|
| `Data/`        | Contains `battery_data.csv` (synthetic data) |
| `Scripts/`     | Python files for data generation, training, and filtering |
| `Filtering/`   | Smoothing techniques (moving average) |
| `ML_Model/`    | (Optional) Saved model files |
| `Plots/`       | SoC plots, comparison graphs |
| `README.md`    | Project explanation (this file) |

---

## 📦 Dependencies

Install all required packages:

bash
pip install pandas numpy scikit-learn matplotlib seaborn



🧪 Scripts Summary
dataset.py
Creates 1000 synthetic battery samples with:

Voltage: 3.0 V – 4.2 V

Current: 0.1 A – 2.0 A

Temperature: 20 °C – 45 °C

SoC computed with a derived relation and noise.

train_model.py
Trains a Linear Regression model.

🧮 Results:

Mean Squared Error (MSE): 4.44

R² Score: 0.99

train_rf_model.py
Trains a Random Forest Regressor.

🧮 Results:

MSE: 5.57

R² Score: 0.99

smoothing.py
Applies a moving average filter (window = 10) to predicted SoC values.

Improves stability for real-time applications.

📈 Visual Results

✅ Linear Regression
Performs best overall with lower MSE.

More efficient and faster to train.

✅ Random Forest
Handles non-linearity better, but slightly higher MSE.

No added accuracy benefit in this case.

✅ Moving Average Smoothing
Removes prediction spikes.

Final plot shows smoother curve, more suitable for real-time SoC tracking.

🚀 Future Work
Integrate real sensor data for validation.

Add Kalman or LMS filters for adaptive correction.

Use deep learning (e.g., LSTM) to capture time-series behavior.

Model battery aging and temperature effects.


