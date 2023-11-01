import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("daily-website-visitors.csv")
ds=data['Page.Loads'].head()
xy=data['Day.Of.Week'].head()
df=data.describe()
print(df)
#segmentation
data["Date"] = pd.to_datetime(data["Date"],format="%m/%d/%Y")
plt.figure(figsize=(40, 80))
plt.bar(data['Day.Of.Week'].head(100), data['Page.Loads'].head(100));
plt.show()
