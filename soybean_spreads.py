"""
#App to find patterns in Corn spread trade
"""
import streamlit as st

from datetime import datetime
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(page_title=" Soybean Spreads ",layout="wide")

SF_H_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='SF-H')
SH_K_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='SH-K')
SK_N_df=pd.read_excel("energy_spread_data_RBOB.xlsx",sheet_name='SK-N')


Soybean_spreads = { 
    'SF-H': {
        'description':'Soybean Jan-Mar',
        'data': SF_H_df,
        'y1a1':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y1a2':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg','SMA10_SF-H_Close_5yr',
                'SMA20_SF-H_Close_5yr','SMA10_SF-H_Close_10yr','SMA20_SF-H_Close_10yr'],
        'y1a3':['2018 SF-H CLOSE','2019 SF-H CLOSE','2020 SF-H CLOSE','2021 SF-H CLOSE',
                '2022 SF-H CLOSE','2023 SF-H CLOSE','SF-H CLOSE 5 yr Avg'],
        'y1b1':['2023 SF-H VOLUME','2022 SF-H VOLUME','SF-H VOLUME 5 yr Avg','SF-H VOLUME 10 yr Avg'],
        'y1b2':['2023 SF-H VOLUME','2022 SF-H VOLUME','SF-H VOLUME 5 yr Avg','SF-H VOLUME 10 yr Avg','SMA10_SF-H_Vol_5yr',
                'SMA20_SF-H_Vol_5yr','SMA10_SF-H_Vol_10yr','SMA20_SF-H_Vol_10yr'],
        'y1b3':['2018 SF-H VOLUME','2019 SF-H VOLUME','2020 SF-H VOLUME','2021 SF-H VOLUME',
                '2022 SF-H VOLUME','2023 SF-H VOLUME','SF-H VOLUME 5 yr Avg'],
        'y2a1':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg'],
        'y2b1':['2023 SF OpenInt','2022 SF OpenInt','SF OpenInt 5 yr Avg','SF OpenInt 10 yr Avg'],
        'y2a2':['2023 SF-H CLOSE','2022 SF-H CLOSE','SF-H CLOSE 5 yr Avg','SF-H CLOSE 10 yr Avg','SMA10_SF-H_Close_5yr',
                'SMA20_SF-H_Close_5yr','SMA10_SF-H_Close_10yr','SMA20_SF-H_Close_10yr'],
        'y2b2':['2023 SF OpenInt','2022 SF OpenInt','SF OpenInt 5 yr Avg','SF OpenInt 10 yr Avg','SMA10_SF_OpenInt_5yr',
                'SMA20_SF_OpenInt_5yr','SMA10_SF_OpenInt_10yr','SMA20_SF_OpenInt_10yr'],
        'y2a3':['2018 SF-H CLOSE','2019 SF-H CLOSE','2020 SF-H CLOSE','2021 SF-H CLOSE',
                '2022 SF-H CLOSE','2023 SF-H CLOSE','SF-H CLOSE 5 yr Avg'],
        'y2b3':['2018 SF OpenInt','2019 SF OpenInt','2020 SF OpenInt','2021 SF OpenInt',
                '2022 SF OpenInt','2023 SF OpenInt','SF OpenInt 5 yr Avg'],
        'x_value':'2022 Dates'
    },
    'SH-K': {
        'description':'Soybean Mar-May',
        'data': SH_K_df,
        'y1a1':['2023 SH-K CLOSE','2022 SH-K CLOSE','2021 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y1a2':['2023 SH-K CLOSE','2022 SH-K CLOSE','2021 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg','SMA10_SH-K_Close_5yr',
                'SMA20_SH-K_Close_5yr','SMA10_SH-K_Close_10yr','SMA20_SH-K_Close_10yr'],
        'y1a3':['2017 SH-K CLOSE','2018 SH-K CLOSE','2019 SH-K CLOSE','2020 SH-K CLOSE',
                '2021 SH-K CLOSE','2022 SH-K CLOSE','2023 SH-K CLOSE','SH-K CLOSE 5 yr Avg'],
        'y1b1':['2023 SH-K VOLUME','2022 SH-K VOLUME','2021 SH-K VOLUME','SH-K VOLUME 5 yr Avg','SH-K VOLUME 10 yr Avg'],
        'y1b2':['2023 SH-K VOLUME','2022 SH-K VOLUME','2021 SH-K VOLUME','SH-K VOLUME 5 yr Avg','SH-K VOLUME 10 yr Avg','SMA10_SH-K_Vol_5yr',
                'SMA20_SH-K_Vol_5yr','SMA10_SH-K_Vol_10yr','SMA20_SH-K_Vol_10yr'],
        'y1b3':['2017 SH-K VOLUME','2018 SH-K VOLUME','2019 SH-K VOLUME','2020 SH-K VOLUME',
                '2021 SH-K VOLUME','2022 SH-K VOLUME','2023 SH-K VOLUME','SH-K VOLUME 5 yr Avg'],
        'y2a1':['2023 SH-K CLOSE','2022 SH-K CLOSE','2021 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg'],
        'y2b1':['2023 SH OpenInt','2022 SH OpenInt','2021 SH OpenInt','SH OpenInt 5 yr Avg','SH OpenInt 10 yr Avg'],
        'y2a2':['2023 SH-K CLOSE','2022 SH-K CLOSE','2021 SH-K CLOSE','SH-K CLOSE 5 yr Avg','SH-K CLOSE 10 yr Avg','SMA10_SH-K_Close_5yr',
                'SMA20_SH-K_Close_5yr','SMA10_SH-K_Close_10yr','SMA20_SH-K_Close_10yr'],
        'y2b2':['2023 SH OpenInt','2022 SH OpenInt','2021 SH OpenInt','SH OpenInt 5 yr Avg','SH OpenInt 10 yr Avg','SMA10_SH_OpenInt_5yr',
                'SMA20_SH_OpenInt_5yr','SMA10_SH_OpenInt_10yr','SMA20_SH_OpenInt_10yr'],
        'y2a3':['2017 SH-K CLOSE','2018 SH-K CLOSE','2019 SH-K CLOSE','2020 SH-K CLOSE',
                '2021 SH-K CLOSE','2022 SH-K CLOSE','2023 SH-K CLOSE','SH-K CLOSE 5 yr Avg'],
        'y2b3':['2017 SH OpenInt','2018 SH OpenInt','2019 SH OpenInt','2020 SH OpenInt',
                '2021 SH OpenInt','2022 SH OpenInt','2023 SH OpenInt','SH OpenInt 5 yr Avg'],
        'x_value':'2022 Dates'
        
    },
    'SK-N': {
        'description':'Soybean May-Jul',
        'data': SK_N_df,
        'y1a1':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y1a2':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg','SMA10_SK-N_Close_5yr',
                'SMA20_SK-N_Close_5yr','SMA10_SK-N_Close_10yr','SMA20_SK-N_Close_10yr'],
        'y1a3':['2018 SK-N CLOSE','2019 SK-N CLOSE','2020 SK-N CLOSE','2021 SK-N CLOSE',
                '2022 SK-N CLOSE','2023 SK-N CLOSE','SK-N CLOSE 5 yr Avg'],
        'y1b1':['2023 SK-N VOLUME','2022 SK-N VOLUME','SK-N VOLUME 5 yr Avg','SK-N VOLUME 10 yr Avg'],
        'y1b2':['2023 SK-N VOLUME','2022 SK-N VOLUME','SK-N VOLUME 5 yr Avg','SK-N VOLUME 10 yr Avg','SMA10_SK-N_Vol_5yr',
                'SMA20_SK-N_Vol_5yr','SMA10_SK-N_Vol_10yr','SMA20_SK-N_Vol_10yr'],
        'y1b3':['2018 SK-N VOLUME','2019 SK-N VOLUME','2020 SK-N VOLUME','2021 SK-N VOLUME',
                '2022 SK-N VOLUME','2023 SK-N VOLUME','SK-N VOLUME 5 yr Avg'],
        'y2a1':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg'],
        'y2b1':['2023 SK OpenInt','2022 SK OpenInt','SK OpenInt 5 yr Avg','SK OpenInt 10 yr Avg'],
        'y2a2':['2023 SK-N CLOSE','2022 SK-N CLOSE','SK-N CLOSE 5 yr Avg','SK-N CLOSE 10 yr Avg','SMA10_SK-N_Close_5yr',
                'SMA20_SK-N_Close_5yr','SMA10_SK-N_Close_10yr','SMA20_SK-N_Close_10yr'],
        'y2b2':['2023 SK OpenInt','2022 SK OpenInt','SK OpenInt 5 yr Avg','SK OpenInt 10 yr Avg','SMA10_SK_OpenInt_5yr',
                'SMA20_SK_OpenInt_5yr','SMA10_SK_OpenInt_10yr','SMA20_SK_OpenInt_10yr'],
        'y2a3':['2018 SK-N CLOSE','2019 SK-N CLOSE','2020 SK-N CLOSE','2021 SK-N CLOSE',
                '2022 SK-N CLOSE','2023 SK-N CLOSE','SK-N CLOSE 5 yr Avg'],
        'y2b3':['2018 SK OpenInt','2019 SK OpenInt','2020 SK OpenInt','2021 SK OpenInt',
                '2022 SK OpenInt','2023 SK OpenInt','SK OpenInt 5 yr Avg'],
        'x_value':'2022 Dates'
    }
              }





def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

        
titletxt='Price & Volume'
subfig = make_subplots(specs=[[{"secondary_y": True}]])






with st.sidebar.container():
    spread = st.selectbox(
    'Select your spread',
    ('SF-H','SH-K','SK-N'))

    st.write('Selected Spread:', Soybean_spreads[spread]['description'])
    selected_values = st.radio('Chart Value', ['Volume','Open Interest'], index = 0)
    selected_graph = st.radio('Chart Type', ['Latest and Historic Avg','Historic & Moving Avg','Full History'], index = 0)
    
    

if selected_graph=='Latest and Historic Avg':
    y1a=Soybean_spreads[spread]['y1a1']
    y1b=Soybean_spreads[spread]['y1b1']

elif selected_graph=='Historic & Moving Avg':
    y1a=Soybean_spreads[spread]['y1a2']
    y1b=Soybean_spreads[spread]['y1b2']

    
else:
    y1a=Soybean_spreads[spread]['y1a3']
    y1b=Soybean_spreads[spread]['y1b3']
    
fig = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y1a, title=titletxt)
fig2 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y1b, title=titletxt)



fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Date"
subfig.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="Spread Volume"
subfig.layout.title=titletxt
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#subfig.show()

subfig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)






#--------------------------------------------------------------------------------------------------------------##########################********************************************


if selected_graph=='Latest and Historic Avg':
    y2a=Soybean_spreads[spread]['y2a1']
    y2b=Soybean_spreads[spread]['y2b1']

elif selected_graph=='Historic & Moving Avg':
    y2a=Soybean_spreads[spread]['y2a2']
    y2b=Soybean_spreads[spread]['y2b2']
    
    
else:
    y2a=Soybean_spreads[spread]['y2a3']
    y2b=Soybean_spreads[spread]['y2b3']

titletxt1='Price & Open Interest '
subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
fig1 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y2a, title=titletxt)
fig12 = px.line(Soybean_spreads[spread]['data'], x=Soybean_spreads[spread]['x_value'], y=y2b, title=titletxt)



fig12.update_traces(yaxis="y2")

subfig1.add_traces(fig1.data + fig12.data)
subfig1.layout.xaxis.title="Date"
subfig1.layout.yaxis.title="Spread Price"
#subfig.layout.yaxis2.type="log"
subfig1.layout.yaxis2.title="Open Interest"
subfig1.layout.title=titletxt1
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig1.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
#subfig.show()

subfig1.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#----------------------------------------------------------------------------------------------------------------


if selected_values=='Volume':
    subfig.update_layout(height=650,width=1200)
    st.plotly_chart(subfig,use_container_width = True,height=650,width=1200)
else:
    subfig1.update_layout(height=650,width=1200)
    st.plotly_chart(subfig1,use_container_width = True,height=650,width=1200)
    
    

     



