import streamlit as st
import pandas as pd
# from vega_datasets import data

df = pd.read_csv('startup_cleaned.csv')
# df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
# # st.dataframe(df)
def load_investor_details(investor):
    st.title(investor)
    # load last 5 recent investment of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
 
#  biggest investments
    big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    st.subheader('Biggest Investments')
    st.dataframe(big_series)
    col1,col2=st.columns(2)
    with col1:
        # fig, ax = plt.subplots()
        # ax.bar(big_series.index,big_series.values)
        # source =big_series.barley()
        
        st.bar_chart(big_series,stack=False)

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'StartUp':
    st.sidebar.selectbox('select StartUp',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    # st.title('StartUp Analysis')
else:
    # st.title('Investor Analysis')
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investors Details')
    if btn2:
        load_investor_details(selected_investor)
    
    
    
    
    # now what we implimented
    # - drop(remove) remark column
    # - rename column
    # - convert amount to cr -> RS
    # - date column
    # - Drop data missed
    
    