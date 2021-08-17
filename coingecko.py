# 抓取各種加密貨幣的現行金額
import pandas as pd
import requests

r = requests.get("https://www.coingecko.com/en")
#r = requests.get("https://www.coingecko.com/en?page=2")
df = pd.read_html(r.text)[0]
df = df[["Coin","Price","Mkt Cap"]]
df["Coin"] = df["Coin"].apply(lambda x: x.split(" ")[0])
df["Price"] = df["Price"].apply(lambda  x: x.replace(",","").replace("$",""))
df["Mkt Cap"] = df["Mkt Cap"].apply(lambda  x: x.replace(",","").replace("$",""))
df.to_csv("crypto-data.csv",index=False)


print(df)