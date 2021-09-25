# Notes For Auto MPG Regression

## Source
* The data was obtained from the UCI Machine Learning Repository

## Features
* Used a Seaborn pairplot to determine any obvious correlations
* Settled on the following columns based on the pairplot
    - displacement, 
    - horsepower
    - weight
    - model year

## Preprocessing
* Missing values
    - Filled in missing values with an iterative imputer; values based on the features chosen for regression predictions

## Deployment
* Tkinter GUI application
