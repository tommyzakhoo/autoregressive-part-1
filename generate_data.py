
import numpy as np # package for arrays, random numbers, writing to CSV

# generate time series data with our toy autoregressive AR(3) model

toy_data = np.zeros(30000) # initialize array of zeros

white_noise = np.random.normal(0,1,30000) # array of standard normal errors

for i in range(4,30000): # first three entries skipped
    toy_data[i] = 0.40*toy_data[i-1] + 0.20*toy_data[i-2] + 0.10*toy_data[i-3] + white_noise[i]
    # AR(3) model: x(t) = 0.40*x(t-1) + 0.20*x(t-2) + 0.10*x(t-3) + error(t)

np.savetxt("toy_data.csv",toy_data,delimiter=",") # save time series data as csv file
