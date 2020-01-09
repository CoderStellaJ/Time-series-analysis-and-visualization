import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

# For one column of a dataframe
def detrend(df, col_name, window_size=365):
    series = df[col_name].dropna().astype(np.float)
    detrended_series = (series - series.rolling(window=window_size).mean()) / series.rolling(window=window_size).std()
    return detrended_series.to_frame()

def lag_differenced(df, col_name, lag=12):
    series = df[col_name].dropna().astype(np.float)
    lagged_series = series - series.shift(lag)
    return lagged_series.to_frame()

def rolling_statistics(df, col_name, window_size=365):
    series = df[col_name].dropna().astype(np.float)
    mean_series = series.rolling(window=window_size).mean()
    std_series = series.rolling(window=window_size).std()
    return mean_series.to_frame(), std_series.to_frame()

def adfuller_test(df, col_name, window_size=365, lags=12):
    # stationarity check
    raw_series = df[col_name].dropna().astype(np.float)
    raw_series_values = raw_series.values

    detrended_df = detrend(df,col_name,window_size)
    detrended_series = detrended_df[col_name].dropna().astype(np.float)
    detrended_series_values = detrended_series.values

    lagged_df = lag_differenced(df, col_name, lags)
    lagged_series = lagged_df[col_name].dropna().astype(np.float)
    lagged_series_values = lagged_series.values

    list = [raw_series_values, detrended_series_values, lagged_series_values]

    for i in range(len(list)):
        if i == 0:
            print(" > Is the data stationary ?")
        elif i == 1:
            print("\n > Is the de-trended data stationary ?")
        else:
            print("\n > Is the lag differenced de-trended data stationary ?")
        dftest = adfuller(list[i], autolag='AIC')
        print("Test statistic = {:.3f}".format(dftest[0]))
        print("P-value = {:.3f}".format(dftest[1]))
        print("Critical values :")
        for k, v in dftest[4].items():
            print(
                "\t{}: {} - The data is {} stationary with {}% confidence".format(k, v, "not" if v < dftest[0] else "",
                                                                                  100 - int(k[:-1])))
