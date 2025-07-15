import pandas as pd 
import numpy as np 
np.random.seed(42) 
n = 1000 
voltage = np.random.uniform(3.0, 4.2, n) 
current = np.random.uniform(0.1, 2.0, n) 
temperature = np.random.uniform(20, 45, n) 
SoC = 100 * (voltage - 3.0) / (4.2 - 3.0) - 0.5 * current + np.random.normal(0, 2, n) 
SoC = np.clip(SoC, 0, 100) 
battery_data = pd.DataFrame({ 
'voltage': voltage, 
'current': current, 
'temperature': temperature, 
'SoC': SoC 
}) 
battery_data.to_csv("battery_data.csv", index=False) 
print("Dataset created and saved as battery_data.csv")
