import streamlit as st 
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    """Function for loading data"""
    df = pd.read_csv("data/2330.TW.csv",index_col="Date")
    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns
    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns
    #stock_column = df['Date']
    #unique_stocks = stock_column.unique()
    return df,numeric_cols, text_cols

df, numeric_cols, text_cols = load_data()

# Title of dashboard
st.title("Stock Dashboard")






# Set Sidebar a title
st.sidebar.title("設定(Settings)")
# add checkbox to sidebox
check_box = st.sidebar.checkbox(label='顯示每日收盤明細')

if check_box:
    # lets show the dataset
    st.write(df)
st.sidebar.subheader("Timeseries Settings")
feature_selection = st.sidebar.multiselect(label="Features to plot",options=numeric_cols)
#stock_dropdown = st.sidebar.selectbox(label="Stock Ticker",options=unique_stocks)

#print(feature_selection)
#df = df[df['Name'] == stock_dropdown]
df_features = df[feature_selection]

plotly_figure = px.line(data_frame=df_features,
    x=df_features.index, y=feature_selection,
    title='Stock timeline')
st.plotly_chart(plotly_figure)    
