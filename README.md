# A Series Of Correlated Events - Part 1
### An Introduction to Time Series Analysis and Fitting Autoregressive Models

<br>

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/panic.jpg", width="300">
  <br>
  <i> A crowd forms outside a Wall Street bank during the Panic of 1907. Photo from <a href="https://digitalcollections.nypl.org/items/510d47dd-5b2c-a3d9-e040-e00a18064a99">New York Public Library</a>. </i>
</p>

## Status
Completed on 4 September 2018.

### Table of contents

- [Tools, Techniques and Concepts](#tools-techniques-and-concepts)
- [Motivation And Project Description](#motivation-and-project-description)
- [Autoregressive Model and Stationarity](#autoregressive-model-and-stationarity)
- [The Autocorrelation and Partial Autocorrelation Function](#the-autocorrelation-and-partial-autocorrelation-function)
- [Fitting an Autoregressive Model to Data](#fitting-an-autoregressive-model-to-data)
- [Summary and Final Thoughts](#summary-and-final-thoughts)

## Tools, Techniques and Concepts

Python, Matplotlib, Statsmodel, Time Series Analysis, Stationarity, Box-Jenkins Method, Autoregressive Model, Auto-correlation, Partial auto-correlation, p-values, statistical significance

## Motivation And Project Description

I was briefly exposed to time series analysis during an undergraduate econometrics class. I recently took a data science challenge that requires fitting an autoregressive model, which piqued my interest in the topic once again.

In the second part of this project, I will be applying the so-called "Box–Jenkins method" to a set of virtual currency time series data. Before that, I will briefly describe the method here, using an artificially generated toy dataset for illustration.

For a more in-depth and mathematical introduction, I highly recommend "<i> Time Series Analysis: Forecasting and Control, 5th Edition </i>" by George E. P. Box and Gwilym M. Jenkins et al. Alternatively, Wikipedia has a nice summary of the method with references. [(link to Wikipedia article)](https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method)

## Autoregressive Model and Stationarity

In this section, I will generate a set of data from a simple toy autoregressive model, defined by the equation shown below. The Python code to do this is simple and can be found here: [generate_data.py](generate_data.py).

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/example_ar3.gif">
</p>

In this model, time t is discrete. The variable X at time t are positively related to its value at time t-1, t-2 and t-3 (these are known as lagged variables), plus an error term epsilon that is drawn from a standard normal distribution. The first three values of X at time t = 1,2,3 are initialized to zero. 

The toy data consists of values for 30,000 time steps, the first 200 time steps is illustrated below using the [Matplotlib package](https://matplotlib.org/). Due to the positive relationship to previous values, a positive (negative) value of X tend to be followed by a positive (negative) one, until a big enough error comes by the break the trend. This give rise to the interesting "cyclic" pattern in the figure.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig1.png", height="300">
</p>

An important assumption of our analysis is [stationarity](https://en.wikipedia.org/wiki/Stationary_process), which means that the mean and the variance of X remains constant, and does not depend on time t. Stationarity is strong assumption that is often not met by real data. However, as we will see later, there are ways to possibly transform data into a stationary one. 

As for our toy model, a mathematical result says that I can check for stationarity by writing down an associated polynomial equation, and checking that all of its (possibly complex) roots are outside the unit circle. Again, I will skip the details, but Wikipedia has a nice  [summary with references](https://en.wikipedia.org/wiki/Autoregressive_model#Definition). I did this for my toy model, and saw that all of its roots are indeed outside the unit circle.

## The Autocorrelation and Partial Autocorrelation Function

The next step in the Box-Jenkins method is to select a model by looking at the autocorrelation and partial autocorrelation functions. I did this using the [statsmodel package](https://www.statsmodels.org/stable/index.html) and the output, along with 99% confidence regions in blue, are shown below. The Python code is very simple and can be found here: [plot_data.py](plot_data.py). In this case, I already know what the underlying model is, but it is still interesting to see how the behavior of these functions agree with mathematical predictions.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig2.png", height="300">
</p>

The autocorrelation plot shows the correlation between X and lagged/past values of itself. Mathematical results says that this should decrease exponentially for an autoregressive model, which fits what we see in the figure.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig3.png", height="300">
</p>

The partial autocorrelation plot also shows the correlation between X and lagged values of itself, <b>after</b> removing the effects of correlations with all earlier lagged values. That is, the correlation between X and a lagged value of itself that is not accounted for by earlier lags. Mathematical resuls says that for an autoregressive model, this plot would be zero from some point onwards. This is what we see in the figure: only the first four terms are significantly different from zero at a 99% level of confidence, which matches up exactly with how we specified our model.

## Fitting an Autoregressive Model to Data

Finally, I use statsmodel again to fit an autoregressive model to the data. Code for this can be found here: [fit_data.py](fit_data.py)

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/coeffs.png", height="300">
</p>

The list above shows the fitted coefficients for the first 10 lagged terms. The first three are almost equal to the 0.40, 0.20 and 0.10 in the toy model that the data was generated from. Due to the randomness in the data, 

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/pvalues.png", height="300">
</p>

Above shows the p-values for each of the fitted coefficients, which have the [Student's t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution).

The first three are p-values are tiny and definitely statistically significant at very high levels of significance. For example, I would keep the first three coefficients and reject the rest, at the 99.99% significance level. If I did so, I would have pretty much recovered the model that the data was generated with!

## Summary and Final Thoughts

In part 2, I will analyze a vritual currency time series dataset. In this part, I gave an basic introduction to time series analysis using the Box-Jenkins method, and fitting an autoregressive model to data.

A short summary of what I have done here is as follows.

- 
-
-

While this was a straightforward exercise, it is nice to see how everything works under ideal conditions, and that our code actually works!

