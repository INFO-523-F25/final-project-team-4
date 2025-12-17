import pandas as pd 

def load_csv(path):
    data = None
    try:
        data = pd.read_csv(path)
    except FileExistsError:
        print('No file found')
    return data

def add_state_code(data_df):
    state_df = pd.read_csv('./data/States.csv').rename(columns = {'Postal': 'STATEAB'})
    data_df = data_df.merge(state_df, how = 'left', left_on = 'State Name', right_on = 'State')
    return data_df

def adding_month(data_df, date_column):
    data_df[date_column] = pd.to_datetime(data_df[date_column])
    data_df['Month'] = data_df[date_column].dt.month
    data_df['Month Name'] = data_df[date_column].dt.month_name()
    data_df['Month Name'] = pd.Categorical(data_df['Month Name'], ordered = True, categories= ["January", "February", "March", "April", "May", 'June',"July"])
    return data_df

def df_groupby_average(data_df, group_list, agg_col):
    grouped_data = data_df.groupby(group_list)[agg_col].mean().reset_index()
    return grouped_data

def load_preprocessed_data(path):
    data_df = load_csv(path= path)
    data_df = add_state_code(data_df)
    data_df = adding_month(data_df, 'Date Local')
    return data_df


## For Testing
# data = load_preprocessed_data('./data/data_preprocessed.csv')
# print(data[['State Name', 'STATEAB','County Name',  'Date Local', 'Month', 'Month Name', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean', 'AQI', 'AQI Category']].head())
# print(data['Month Name'].unique())
# data_grouped_month = df_groupby_average(data, ['STATEAB', 'Month Name'], agg_col= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean', 'Month'])

# filter_data = data[data['STATEAB'] == "AZ"]
# data_grouped_month_county = df_groupby_average(filter_data, ['County Name', 'Month Name'], agg_col= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean'])
# data_grouped_pivot = data_grouped_month_county.pivot( index = 'County Name', columns = 'Month Name', values = 'AQI').fillna(0)
# print(data_grouped_pivot)












