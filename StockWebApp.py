# Description : This is a stock market dashboard to show some charts and data on some stock

# Import the libraries
import streamlit as st 
import pandas as pd
from PIL import Image

# Add a title and an image
st.write("""
# Strock Market Web Application
**Visually** show data on a stock!  Data range from Jan 2, 2020 - Aug 16, 2021
""")

image = Image.open("G:/stock_case/w01_stock_web_app/statics/img/stock_image.PNG")
st.image(image, use_column_width=True)


# Create a sidebar header
st.sidebar.header('User Input')

# Create a function to get the users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-01")
    end_date = st.sidebar.text_input("End Date", "2021-08-16")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "2330")
    return start_date, end_date, stock_symbol

# Create as function to get the company name
def get_company_name(symbol):
    if symbol == '0050':
        return '台灣50'
    elif symbol == '2330':
        return '台積電'
    elif symbol == '2454':
        return '聯發科'
    else:
        '尚未設定'

# Create a funciton to get the proper company data and the proper timeframe from the start data to the end data
def get_data(symbol, start, end):
    #Load the data 
    if symbol.upper() == '0050':
        df = pd.read_csv("G:/stock_case/w01_stock_web_app/data/0050.TW.csv")
    elif symbol.upper() == '2330':
        df = pd.read_csv("G:/stock_case/w01_stock_web_app/data/2330.TW.csv")
    elif symbol.upper() == '2454':
        df = pd.read_csv("G:/stock_case/w01_stock_web_app/data/2454.TW.csv")
    else:
        df = pd.DataFrame(columns=['Date','Close','Open','Volume','Adj Close','High','Low'])
    # Get the date range 
    start = pd.to_datetime(start)        
    end = pd.to_datetime(end)
    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0
    # Start the date from the top of the data set and go down to see if the uers start data
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 - j
            break
    # Set the index to be the date 
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row + 1, :]

# Get the users input 
start, end , symbol = get_input()    
# Get the data 
df = get_data(symbol=symbol, start=start, end=end)
# Get the company name
company_name = get_company_name(symbol=symbol.upper())

# Display the close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])
# Display the volume
st.header(company_name+" Close Volume\n")
st.line_chart(df['Volume'])

# Get statistics on the data 
st.header('Data Statistics')
st.write(df.describe())

