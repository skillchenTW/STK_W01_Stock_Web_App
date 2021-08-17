import pandas as pd
import matplotlib.pyplot as plt
import ta 

df1 = pd.read_csv('data/2330.TW.csv')
df = df1[["Date","Close"]]
df.Date = pd.to_datetime(df.Date,format="%Y-%m-%d")
df = df[ df.Close > 0]
df.sort_values(by="Date", inplace=True)
df["rsi"] = ta.momentum.rsi(close=df.Close, window=14)
#print(df)
plt.style.use("dark_background")
fig, [ax1,ax2] = plt.subplots(2,sharex=True, gridspec_kw={"height_ratios":[2,1]})
ax1.semilogy(df.Date,df.Close)
ax2.plot(df.Date,df.rsi)
plt.show()
