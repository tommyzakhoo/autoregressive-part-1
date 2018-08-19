
import numpy as np
import pandas as pd

from pandas import Series
from matplotlib import pyplot as plt

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

df = pd.read_csv('toy_data.csv',header=None) # load the in-sample data
series = df.squeeze() # convert dataframe to a pandas series

plt.rcParams.update({'font.size': 22}) # set font size for plots

plt.plot(series[0:200]) # plot first 200 values of the time series

# plot first 50 terms of the partial autocorrelation function
plot_pacf(series, lags=50, alpha=0.01) # 1 - alpha = confidence level

# plot first 50 terms of the autocorrelation function
plot_acf(series, lags=50, alpha=0.01) # 1 - alpha = confidence level

# create labels and a title for our plot
plt.xlabel('Lag')
plt.ylabel('Correlation')
plt.title('First 200 values of our toy data')

# show the plot
plt.show()
