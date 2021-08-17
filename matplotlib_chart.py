import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

df1 = pd.read_csv("data/2454.TW.csv")
df = df1[["Date","Close"]]
df["Date"] = pd.to_datetime(df.Date)
print(df)
plt.style.use("fivethirtyeight")

fig,ax = plt.subplots()

ax.plot(df.Date,df.Close)
ax.yaxis.set_major_formatter("NT${x:,.0f}")
#ax.yaxis.set_minor_formatter("NT${x:,.0f}")
plt.show()
