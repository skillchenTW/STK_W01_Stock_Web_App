from re import template
import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv("data/Bitstamp_BTCUSD_d.csv")
# 該表日期是反向,所以將df的排序逆轉
df = df.iloc[::-1]
# 將日期格式由 2014/11/28 00:00  -> 2014-11-28

df['date'] = pd.to_datetime(df['date'])
df['20wma'] = df['close'].rolling(window=140).mean()

fig = go.Figure(data=[go.Candlestick(x=df['date'],
    open=df['open'], high=df['high'], low=df['low'], close=df['close'])])

fig.add_trace(go.Scatter(
    x=df['date'], y=df['20wma'],line=dict(color="#7e7e7e"),name="20-Week SMA"
))

fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark")
fig.update_layout(yaxis_title="Bitcoin price (USD)", xaxis_title="Date")

fig.update_yaxes(type="log")

fig.show()


print(df)