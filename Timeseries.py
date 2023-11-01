import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("daily-website-visitors.csv")
data["Date"] = pd.to_datetime(data["Date"],format="%m/%d/%Y")
plt.figure(figsize=(20,80))
plt.plot(data['Date'].head(100),data['Page.Loads'].head(100))
plt.title("Time Series Data")
plt.xlabel("Date")
plt.ylabel("Page.Loads")
plt.legend()
plt.show()
