import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots



def configure_page(): 
    st.set_page_config(
    page_title= "AQI Dashboard",
    page_icon=":bar_chart:",
    layout= "wide"
) 

def configure_overview(): 
    st.markdown('## AQI Dashboard')
    st.markdown('This dashboard will show visual AQI measurements from January 2025 to July 2025')
    st.markdown('The aim is to understand geographical and seasonal impacts of AQI across the United States')

def configure_sidebar(state_list):
    month = st.sidebar.number_input("Month Number", 1, 7, 1)
    state_selected = st.sidebar.selectbox(
        "State Selection", 
        state_list)  
    return month, state_selected

def create_map_plot(month_number:int, data): 
    filter_data = data[data['Month'] == month_number]
    st.markdown(f'### USA AQI for Month {month_number}')
    fig1 = px.choropleth(filter_data, locations= filter_data['STATEAB'], locationmode= "USA-states",
                        color = 'AQI', color_continuous_scale= "inferno", 
                        range_color = (0, 100), scope = "usa")
    return fig1

def create_line_plot(state, data):
    filter_data = data[data['STATEAB'] == state]
    st.markdown(f'### Temperature, Wind and AQI over Time for {state}')
    filter_data = pd.melt(filter_data, id_vars = 'Month', value_vars= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean'])
    st.line_chart(filter_data, x = "Month", y = "value", color = 'variable')

def main():
    data_df = pd.read_csv('./data/data_preprocessed.csv')
    data_grouped_month = data_df[['STATEAB', 'Month', 'AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean']].groupby(['STATEAB', 'Month']).mean().reset_index()
    state_name = tuple(data_grouped_month['STATEAB'].unique())
    configure_page()
    configure_overview()
    month, state = configure_sidebar(state_name)
    fig = create_map_plot(month, data_grouped_month)
    st.plotly_chart(fig)
    
    create_line_plot(state, data_grouped_month)
if __name__ == "__main__":
    main()

# data_df = pd.read_csv('./data/data_preprocessed.csv')
# data_df = data_df[["State Name", "Temp Arithmetic Mean", "Wind Arithmetic Mean", "AQI"]].groupby('State Name').mean()
# st.header("AQI vs Temp. By State Name")
# st.scatter_chart(data_df[["Temp Arithmetic Mean", "Wind Arithmetic Mean", "AQI"]], x = "Temp Arithmetic Mean", y = "AQI")
# data_df = data_df.reset_index()
# state_df = pd.read_csv('./data/States.csv').rename(columns = {'Postal': 'STATEAB'})
# data_df = data_df.merge(state_df, how = 'left', left_on = 'State Name', right_on = 'State')

# fig1 = px.choropleth(data_df, locations= data_df['STATEAB'], locationmode= "USA-states",
#                      color = 'AQI', color_continuous_scale= "inferno", 
#                      range_color = (0, 100), scope = "usa")



