import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
data = pd.read_csv("battery_data.csv") 
sns.pairplot(data) 
plt.suptitle("Pairplot of Battery Parameters", y=1.02) 
plt.show() 
