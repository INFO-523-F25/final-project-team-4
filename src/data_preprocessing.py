import pandas as pd 
'''
Preprocessing functions for databoard
'''
def load_csv(path):
    '''
    loads data returns dataframe
    
    :param path: Path to data
    '''
    data = None
    try:
        data = pd.read_csv(path)
    except FileExistsError:
        print('No file found')
    return data

def add_state_code(data_df):
    '''
    Adds Abbreviation of States to data
    
    :param data_df: AQI data 
    '''
    state_df = pd.read_csv('./data/States.csv').rename(columns = {'Postal': 'STATEAB'})
    data_df = data_df.merge(state_df, how = 'left', left_on = 'State Name', right_on = 'State')
    return data_df

def adding_month(data_df, date_column):
    '''
    Add Month number and month name to dataframe
    
    :param data_df: AQI data
    :param date_column: Date Column in data
    '''
    data_df[date_column] = pd.to_datetime(data_df[date_column])
    data_df['Month'] = data_df[date_column].dt.month
    data_df['Month Name'] = data_df[date_column].dt.month_name()
    data_df['Month Name'] = pd.Categorical(data_df['Month Name'], ordered = True, categories= ["January", "February", "March", "April", "May", 'June',"July"])
    return data_df

def df_groupby_average(data_df, group_list, agg_col):
    '''
    Docstring for df_groupby_average
    
    :param data_df: AQI data
    :param group_list: list of columns to group by
    :param agg_col: list of columns being aggrerated
    '''
    grouped_data = data_df.groupby(group_list)[agg_col].mean().reset_index()
    return grouped_data

def load_preprocessed_data(path):
    '''
    Preforms predesign preprocessing steps for dashboard
    
    :param path: path to csv
    '''
    data_df = load_csv(path= path)
    data_df = add_state_code(data_df)
    data_df = adding_month(data_df, 'Date Local')
    return data_df













