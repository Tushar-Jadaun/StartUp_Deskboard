import streamlit as st
import pandas as pd


df = pd.read_csv('startup_funding.csv')
df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
# st.dataframe(df)
st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'StartUp':
    st.sidebar.selectbox('select StartUp',sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    st.sidebar.selectbox('Select Startup',sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.button('Find Investors Details')
    st.title('Investor Analysis')