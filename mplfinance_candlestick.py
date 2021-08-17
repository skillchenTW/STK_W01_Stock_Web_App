import yfinance as yf
import pandas as pd 
import mplfinance as mpf

df = yf.Ticker("BTC-USD").history(period="max")

df["50ma"] = (df["Open"].rolling(window=50).mean()) / 1.5
df["ma"] = (df["Open"].rolling(window=50).mean()) * 1.5

#mpf.plot(df,type='line')
#mpf.plot(df,type='renko')

# 設定預設的窗體由2021/06/01日看起
df = df.loc["2021-06-01":]
apds = [ mpf.make_addplot(df[["50ma","ma"]])]

#mpf.plot(df,type='candle',volume=True, mav=(10,3,20))
mpf.plot(df,type='candle',volume=True, mav=(10,3,20),show_nontrading=True)
#mpf.plot(df,type='candle',volume=True, addplot= apds)