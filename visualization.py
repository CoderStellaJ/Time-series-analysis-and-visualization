import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
from data import *

# For raw data
def plot(df, subplots=True):
    df_fig = df.plot(subplots=subplots)
    return df_fig

# For EUR future 1min
def plot_price(EUR_future_1min, subplots=True):
    plot_df = EUR_future_1min[['Bid_open','Ask_open', 'Trade_open']]
    df_fig = plot_df.plot(subplots=subplots)
    return df_fig

def plot_volume(EUR_future_1min, subplots=True):
    plot_df = EUR_future_1min[['Bid_volume', 'Ask_volume', 'Trade_volume']]
    df_fig = plot_df.plot(subplots=subplots)
    return df_fig

# For one column of a dataframe
def seasonal_decompose(df, col_name, freq, model='additive'):
    # model can be 'additive' or 'multiplicative'
    series = df[col_name].dropna().astype(np.float)
    plot_df = series.to_frame()
    decompose = sm.tsa.seasonal_decompose(plot_df, model=model, freq=freq).plot()

    return decompose

def plot_rolling_statistics(df, col_name, window_size=365, lags=12):
    raw_df = df[col_name].dropna().astype(np.float).to_frame()
    detrended_df = detrend(df, col_name, window_size)
    lagged_df = lag_differenced(df, col_name, lags)

    raw_mean_df, raw_std_df = rolling_statistics(raw_df, col_name, window_size)
    detrended_mean_df, detrended_std_df = rolling_statistics(detrended_df, col_name, window_size)
    lagged_mean_df, lagged_std_df = rolling_statistics(lagged_df, col_name, window_size)

    fig, ax = plt.subplots(3, figsize=(12, 9))
    ax[0].plot(raw_df, label='raw data')
    ax[0].plot(raw_mean_df, label="rolling mean")
    ax[0].plot(raw_std_df, label="rolling std")
    ax[0].legend()

    ax[1].plot(detrended_df, label="de-trended data")
    ax[1].plot(detrended_mean_df, label="rolling mean")
    ax[1].plot(detrended_std_df, label="rolling std")
    ax[1].legend()

    ax[2].plot(lagged_df, label="lag differenced de-trended data")
    ax[2].plot(lagged_mean_df, label="rolling mean")
    ax[2].plot(lagged_std_df, label="rolling std")
    ax[2].legend()

    return fig


def plot_acf_pacf(df, col_name, lags):
    series = df[col_name].dropna().astype(np.float)

    fig, ax = plt.subplots(2, figsize=(12, 6))
    ax[0] = plot_acf(series, ax=ax[0], lags=lags)
    ax[1] = plot_pacf(series, ax=ax[1], lags=lags)
    return fig

