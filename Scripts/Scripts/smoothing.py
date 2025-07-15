import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv("battery_data.csv") 
data['smoothed_soc'] = data['SoC'].rolling(window=10).mean() 
plt.figure(figsize=(10,5)) 
plt.plot(data['SoC'], label='Original SoC', alpha=0.6) 
plt.plot(data['smoothed_soc'], label='Smoothed SoC (Window=10)', linewidth=2) 
plt.title("SoC Smoothing Using Moving Average") 
plt.xlabel("Sample Index") 
plt.ylabel("State of Charge") 
plt.legend() 
plt.grid(True) 
plt.show() 
