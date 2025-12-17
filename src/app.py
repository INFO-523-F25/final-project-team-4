import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from data_preprocessing import df_groupby_average, load_preprocessed_data



def configure_page(): 
    st.set_page_config(
    page_title= "AQI Dashboard",
    page_icon=":bar_chart:",
    layout= "wide"
) 

def configure_overview(): 
    st.markdown('## AQI Dashboard')
    st.markdown('This dashboard will show visual AQI measurements from January 2025 to July 2025')
    st.markdown('The aim is to understand geographical and seasonal impacts of AQI acoss the United States')

def configure_sidebar(state_list, month_name):
    month = st.sidebar.selectbox(
        "Month Selection", 
        month_name)
    state_selected = st.sidebar.selectbox(
        "State Selection", 
        state_list)  
    return month, state_selected

def create_map_plot(month_name, data): 
    filter_data = data[data['Month Name'] == month_name]
    st.markdown(f'### USA AQI for {month_name}')
    fig1 = px.choropleth(filter_data, locations= filter_data['STATEAB'], locationmode= "USA-states",
                        color = 'AQI', color_continuous_scale= "thermal", 
                        range_color = (0, 100), scope = "usa")
    return fig1

def create_line_plot(state, data):
    filter_data = data[data['STATEAB'] == state]
    st.markdown(f'### Temperature, Wind and AQI over Time for {state}')
    filter_data = pd.melt(filter_data, id_vars = 'Month Name', value_vars= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean'])
    st.line_chart(filter_data, x = "Month Name", y = "value", color = 'variable')


def create_county_map(state,data):
    filter_data = data[data['STATEAB'] == state]
    data_grouped_month_county = df_groupby_average(filter_data, ['County Name', 'Month Name'], agg_col= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean'])
    data_grouped_pivot = data_grouped_month_county.pivot( index = 'County Name', columns = 'Month Name', values = 'AQI')
    plt.figure(figsize = (5, 5))
    sns.heatmap(data_grouped_pivot, annot = True, cmap = 'coolwarm')
    plt.xlabel("Month")
    plt.ylabel("County Name")
    plt.title(f'{state} Country AQI values')
    st.pyplot(plt, width= "content")
    # return plt



def main():
    data_df = load_preprocessed_data('./data/data_preprocessed.csv')
    data_grouped_month_state = df_groupby_average(data_df, ['STATEAB', 'Month Name'], agg_col= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean', 'Month'])
    state_name = tuple(data_grouped_month_state['STATEAB'].unique())
    month_name = data_grouped_month_state['Month Name'].unique().to_list()
    configure_page()
    configure_overview()
    month, state = configure_sidebar(state_name, month_name)
    fig = create_map_plot(month, data_grouped_month_state)
    st.plotly_chart(fig)
    create_line_plot(state, data_grouped_month_state)
    create_county_map(state= state, data = data_df)
    
if __name__ == "__main__":
    main()



