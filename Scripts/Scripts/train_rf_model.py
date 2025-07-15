import pandas as pd 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score 
data = pd.read_csv("battery_data.csv") 
X = data[['voltage', 'current', 'temperature']] 
y = data['SoC'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
rf_model = RandomForestRegressor(n_estimators=100, random_state=42) 
rf_model.fit(X_train, y_train) 
y_pred = rf_model.predict(X_test) 
mse = mean_squared_error(y_test, y_pred) 
r2 = r2_score(y_test, y_pred) 
print(f"Random Forest MSE: {mse:.2f}") 
print(f"Random Forest R² Score: {r2:.2f}")
