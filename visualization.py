import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

def plot(df, subplots=True):
    df_fig = df.plot(subplots=subplots)
    return df_fig

def plot_price(EUR_future_1min, subplots=True):
    plot_df = EUR_future_1min[['Bid_open','Ask_open', 'Trade_open']]
    df_fig = plot_df.plot(subplots=subplots)
    return df_fig

def plot_volume(EUR_future_1min, subplots=True):
    plot_df = EUR_future_1min[['Bid_volume', 'Ask_volume', 'Trade_volume']]
    df_fig = plot_df.plot(subplots=subplots)
    return df_fig

def seasonal_decompose(df, col_name, freq, model='additive'):
    # model can be 'additive' or 'multiplicative'
    series = df[col_name].dropna().astype(np.float)
    plot_df = series.to_frame()
    decompose = sm.tsa.seasonal_decompose(plot_df, model=model, freq=freq).plot()

    return decompose
