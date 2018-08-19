
import pandas as pd
from pandas import Series
from statsmodels.tsa.ar_model import AR

df = pd.read_csv('toy_data.csv',header=None) # load the data from .cvs file
series = df.squeeze() # convert dataframe to pandas series

model = AR(series) # code to fit
model_fit = model.fit(trend='nc') # trend=nc means no constant term

print('Coefficients: \n\n%s \n' % model_fit.params) # print fitted coefficients
print('P-values: \n\n%s \n' % model_fit.pvalues) # print p-values
