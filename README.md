# 🔋 Battery SoC Estimator using ML & Signal Smoothing

This project implements a **machine learning-based State-of-Charge (SoC) estimation system** using battery parameters like voltage, current, and temperature. The system combines:

- 🔍 Supervised ML models (Linear Regression, Random Forest)
- 🧹 Smoothing filter (Moving Average)
- 📊 Visualization of battery SoC

---

## 🧠 Project Overview

Accurate SoC prediction is critical for battery health and optimization. This project:

1. Generates synthetic battery data.
2. Predicts SoC using ML models.
3. Applies a moving average filter to stabilize the predictions.

---

## 📁 Folder Structure

| Folder         | Description |
|----------------|-------------|
| Data      | Contains `battery_data.csv` with 1000 synthetic battery readings |
| Scripts   | All core Python scripts: data generation, training, evaluation |
| ML_Model    | Optional folder to store trained model `.pkl` files |
| Filtering   | Optional smoothing logic (e.g., `moving_average.py`) |
| Plots       | Visualization outputs (e.g., PNG plots of SoC) |
| README.md    | This file |

---

📦 Dependencies

Install required packages:

bash
pip install pandas numpy matplotlib seaborn scikit-learn



Key Scripts


dataset.py

Generates synthetic data with voltage, current, temperature.

SoC = f(voltage, current) + Gaussian noise

Output: battery_data.csv

explore_dataset.py

Uses seaborn to plot relationships between features.

train_model.py

Trains a Linear Regression model.

Achieves MSE ≈ 4.44, R² ≈ 0.99

train_rf_model.py

Trains a Random Forest model.

Slightly higher MSE (≈ 5.57), same R² (≈ 0.99)

smoothing.py

Applies a moving average filter (window=10) to smooth SoC values.

Reduces prediction spikes for stable BMS use.
