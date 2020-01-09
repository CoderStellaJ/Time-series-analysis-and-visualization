# Time series analysis and visualization

### Data source
historical bid/ask/trade prices, and, where available, volumes, with (i) 1-min frequency and (ii) 1-day frequency for KTB Futures and EUR currency. 
In this project, I choose EUR as analysis target.

### User guide


### Manipulation of data
`preprocess.py`, `data.py`
<br/> input and output are both dataframes
1. raw data:
<br/> transforms .xlsx data into time series dataframe
2. seasonal decomposition:
<br/> y = trend + seasonal + decomposition
<br/> y = trend * seasonal * decomposition
3. de-trended data 
4. lag differenced data
5. rolling statistics: mean and std
6. Augmented Dickey-Fuller test
<br/> stationarity hypothesis test
7. Autocorrelation plots
<br/> correlation between the series with its lags


### Visualization
`visualization.py`
1. plot raw data: `plot`, `plot_price`, `plot_volume`
2. plot seasonal decomposition: `seasonal_decompose`
3. plot rolling statistics for raw/detrended/lag differenced data: `plot_rolling_statistics`
4. plot acf and pacf: `plot_acf_pacf`

### Time series analysis
#### Properties and types of series
1. Trend 
<br/>A long-term increase or decrease in the data. 
This can be seen as a slope (is doesn’t have to be linear) roughly going through the data.

2. Seasonality
<br/>A time series is said to be seasonal when it is affected by seasonal factors (hour of day, week, month, year, etc.). 
Seasonality can be observed with nice cyclical patterns of fixed frequency.

3. Cyclicity
<br/>A cycle occurs when the data exhibits rises and falls that are not of a fixed frequency. 
These fluctuations are usually due to economic conditions, and are often related to the “business cycle”. 
The duration of these fluctuations is usually at least 2 years.

4. Residuals
<br/>Each time series can be decomposed in two parts:
<br/>A forecast, made up of one or several forecasted values
<br/>Residuals. They are the difference between an observation and its predicted value at each time step.
<br/> Value of series at time t = Predicted value at time t + Residual at time t

#### Decomposition of a time series
* A trend (upward or downwards movement of the curve on the long term)
* A seasonal component
* Residuals

#### Stationarity
1. De-trending
<br/> We remove the underlying trend in the series. This can be done in several ways, depending on the nature of data :
<br/>Indexed data: data measured in currencies are linked to a price index or related to inflation. Dividing the series by this index (ie deflating) element-wise is therefore the solution to de-trend the data.
<br/>Non-indexed data: is it necessary to estimate if the trend is constant, linear or exponential. The first two cases are easy, for the last one it is necessary to estimate a growth rate (inflation or deflation) and apply the same method as for indexed data.

2. Differencing
<br/>Seasonal or cyclical patterns can be removed by substracting periodical values. 
If the data is 12-month seasonal, substracting the series with a 12-lag difference series will give a “flatter” series

3. Logging
in the case where the compound rate in the trend is not due to a price index (ie the series is not measured in a currency), 
logging can help linearize a series with an exponential trend (recall that log(exp(x)) = x). 
It does not remove an eventual trend whatsoever, unlike deflation.

#### Autocorrelation plots (ACF & PACF)
- An autocorrelation (ACF) plot represents the autocorrelation of the series with lags of itself.
- A partial autocorrelation (PACF) plot represents the amount of correlation between a series and a lag of itself that is not explained by correlations at all lower-order lags.
<br/> Ideally, we want no correlation between the series and lags of itself. Graphically speaking, we would like all the spikes to fall in the blue region.

### Financial concepts
#### KTB Future
Korea Treasury Bond Future

Future:
Futures are financial contracts obligating the buyer to purchase an asset or the seller to sell an asset and have a predetermined future date and price.

#### Bid and Ask Prices
The bid price is what buyers are willing to pay for it. The ask price is what sellers are willing to take for it.

#### Analysis
Here are 2 resources that I referred to.
1. [Time series analysis in python 1](https://towardsdatascience.com/time-series-in-python-exponential-smoothing-and-arima-processes-2c67f2a52788)
2. [Time seires analysis in python 2](https://towardsdatascience.com/time-series-in-python-part-2-dealing-with-seasonal-data-397a65b74051)

