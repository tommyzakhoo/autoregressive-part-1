# A Series Of Correlated Events
### Analyzing Economics Time Series With Autoregressive Models

<br>

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/panic.jpg", width="300">
  <br>
  <i> A crowd forms outside a Wall Street bank during the Panic of 1907. Photo from <a href="https://digitalcollections.nypl.org/items/510d47dd-5b2c-a3d9-e040-e00a18064a99">New York Public Library</a>. </i>
</p>

## Status
Work in progress. Last update: 14 August 2018.

### Table of contents

- [Motivation And Project Description](#motivation-and-project-description)
- [Introduction to Time Series Analysis](#introduction-to-time-series-analysis)

## Motivation And Project Description

I was briefly exposed to the analysis of time series during an undergraduate class in Econometrics. I recently had the opportunity to take a data science challenge involving an autoregressive model, which piqued my interest in the topic once again.

In this project, I will generate a toy dataset to illustrate the so-called "Box–Jenkins method". Then, I will apply the same method to model two real world dataset.

The writing here will be terse. For a more in-depth and mathematical introduction, I highly recommend "<b> Time Series Analysis: Forecasting and Control, 5th Edition </b>" by George E. P. Box and Gwilym M. Jenkins et al.

## Introduction to Time Series Analysis

In this section, I have generated a set of data from a simple toy autoregressive model defined by the equation below. The Python code to do this is simple and can be found here: [generate_data.py](generate_data.py).

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/example_ar3.gif">
</p>

In our model, time t is discrete. The variable X at time t depends on its value at time t-1, t-2 and t-3, plus an error term epsilon that is drawn from the standard normal distribution. The first three values of X at time t = 1,2,3 are set to zero. 

consisting of 30,000 data points in Python and

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig1.png", height="300">
</p>


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
