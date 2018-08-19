# A Series Of Correlated Events
### Analyzing Economics Time Series With Autoregressive Models

<br>

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/panic.jpg", width="300">
  <br>
  <i> A crowd forms outside a Wall Street bank during the Panic of 1907. Photo from <a href="https://digitalcollections.nypl.org/items/510d47dd-5b2c-a3d9-e040-e00a18064a99">New York Public Library</a>. </i>
</p>

## Status
Work in progress. Last update: 18 August 2018.

### Table of contents

- [Motivation And Project Description](#motivation-and-project-description)
- [Introduction to Time Series Analysis](#introduction-to-time-series-analysis)

## Motivation And Project Description

I was briefly exposed to time series analysis during an undergraduate econometrics class. I recently took a data science challenge that requires fitting an autoregressive model, which piqued my interest in the topic once again.

In this project, I will be applying the so-called "Box–Jenkins method" to two real world datasets. Before that, I will briefly decribe the method with an artificial toy dataset.

For a more in-depth and mathematical introduction, I highly recommend "<i> Time Series Analysis: Forecasting and Control, 5th Edition </i>" by George E. P. Box and Gwilym M. Jenkins et al. Alternatively, Wikipedia has a nice summary of the method with references. [(link to Wikipedia article)](https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method)

## Introduction to Time Series Analysis

In this section, I will generate a set of data from a simple toy autoregressive model, defined by the equation shown below. The Python code to do this is simple and can be found here: [generate_data.py](generate_data.py).

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/example_ar3.gif">
</p>

In this model, time t is discrete. The variable X at time t are positively related to its value at time t-1, t-2 and t-3 (these are known as lagged variables), plus an error term epsilon that is drawn from a standard normal distribution. The first three values of X at time t = 1,2,3 are initialized to zero. 

The toy data consists of values for 30,000 time steps, the first 200 time steps is illustrated below using the Matplotlib package. Due to the positive relationship to previous values, a positive (negative) value of X tend to be followed by a positive (negative) one, until a big enough error comes by the break the trend. This give rise to the interesting "cyclic" pattern in the figure.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig1.png", height="300">
</p>

An important assumption of our analysis is [stationarity](https://en.wikipedia.org/wiki/Stationary_process), which means that the mean and the variance of X does not depend on time t.

https://en.wikipedia.org/wiki/Stationary_process

## Dataset 1 - Virtual Currency

The market for virtual goods is a challenging but exciting frontier for modern economics.

## Dataset 2 - Housing Construction Price


<!--

```python
s = "Python syntax highlighting"
print s
```

This project is a part of the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) at [Code for San Francisco](http://www.codeforsanfrancisco.org).  Other DSWG projects can be found at the [main GitHub repo](https://github.com/sfbrigade/data-science-wg).

#### -- Project Status: [Active, On-Hold, Completed]

## Project Intro/Objective
The purpose of this project is ________. (Describe the main goals of the project and potential civic impact. Limit to a short paragraph, 3-6 Sentences)

### Partner
* [Name of Partner organization/Government department etc..]
* Website for partner
* Partner contact: [Name of Contact], [slack handle of contact if any]
* If you do not have a partner leave this section out

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* etc.

### Technologies
* R 
* Python
* D3
* PostGres, MySql
* Pandas, jupyter
* HTML
* JavaScript
* etc. 

## Project Description
(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- etc. (be as specific as possible)

-->
