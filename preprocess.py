import pandas as pd

def read_data():
    dfs = pd.read_excel('./raw_KTB_EUR_numbers/raw_KTB_EUR_numbers.xlsx', sheet_name=None, parse_dates=True, index=False)
    EUR_future_1min_sheet = dfs['EUR future 1min']
    EUR_1min = dfs['EUR 1min']
    EUR_1day = dfs['EUR 1day']
    return EUR_future_1min_sheet, EUR_1min, EUR_1day

def preprocess_EUR_1day(EUR_1day):
    EUR_1day = EUR_1day.set_index('Unnamed: 0')
    EUR_1day.index.name = 'Dates'
    EUR_1day.columns = EUR_1day.iloc[5]
    EUR_1day = EUR_1day[6:]
    return EUR_1day

def preprocess_EUR_1min(EUR_1min):
    EUR_1min = EUR_1min.dropna(how='all', axis=1)
    EUR_1min = EUR_1min.iloc[7:]
    EUR_1min = EUR_1min.set_index('Start date')
    del EUR_1min['Start date.1']
    del EUR_1min['Start date.2']
    EUR_1min.columns = ['Bid_open', 'Ask_open', 'Trade_open']
    return EUR_1min

def preprocess_EUR_future_1min(EUR_future_1min):
    EUR_future_1min = EUR_future_1min.set_index('Unnamed: 0')
    EUR_future_1min.index.name = 'Dates'

    EUR_future_1min = EUR_future_1min.dropna(how='all', axis=1)
    del EUR_future_1min['Unnamed: 4']
    del EUR_future_1min['Unnamed: 8']
    EUR_future_1min = EUR_future_1min.iloc[4:]

    EUR_future_1min.columns = ['Trade_open', 'Trade_volume', 'Bid_open', 'Bid_volume', 'Ask_open', 'Ask_volume']

    return EUR_future_1min