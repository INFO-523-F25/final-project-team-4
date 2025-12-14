# merged_df.to_csv('./data/data_preprocessed.csv', index = False)
# merged_df['State Name'].unique()
data_df = pd.read_csv('./data/data_preprocessed.csv')
# data_df = data_df[["State Name", "Temp Arithmetic Mean", "Wind Arithmetic Mean", "AQI"]].groupby('State Name').mean()
# st.header("AQI vs Temp. By State Name")
# st.scatter_chart(data_df[["Temp Arithmetic Mean", "Wind Arithmetic Mean", "AQI"]], x = "Temp Arithmetic Mean", y = "AQI")
# data_df = data_df.reset_index()
# print(merged_df.isna().sum())

# state_df = pd.read_csv('./data/States.csv').rename(columns = {'Postal': 'STATEAB'})
# data_df = data_df.merge(state_df, how = 'left', left_on = 'State Name', right_on = 'State')
# data_df = data_df[['State Name', 'STATEAB', 'Date Local', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean', 'AQI', 'AQI Category']]
# data_df['Date Local'] = pd.to_datetime(data_df['Date Local'])
# data_df['Month'] = data_df['Date Local'].dt.month
# # print(data_df[data_df['STATEAB'].isna()]['State Name'].unique())

import seaborn as sns 
import matplotlib.pyplot as plt
data_df = pd.read_csv('./data/data_preprocessed.csv')
data_grouped_month = data_df[['STATEAB', 'Month', 'AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean']].groupby(['STATEAB', 'Month']).mean().reset_index()
filter_data = data_grouped_month[data_grouped_month ['STATEAB'] == 'AZ']
filter_data = pd.melt(filter_data, id_vars = 'Month', value_vars= ['AQI', 'Temp Arithmetic Mean', 'Wind Arithmetic Mean'])

# data_grouped_month[data_grouped_month['Month'] == 1]

# state_name = tuple(data_grouped_month['STATEAB'].unique())
# print(state_name)

# data_grouped_month_pivot = data_grouped_month.pivot( index = 'STATEAB', columns= 'Month', values = "AQI")
# sns.heatmap(data_grouped_month_pivot, cmap= 'crest', annot= True)

# data_df.to_csv('./data/data_preprocessed.csv', index = False)


# data_grouped_month_pivot[data_grouped_month_pivot['Month'] == 1]