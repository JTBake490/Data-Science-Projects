# Notes For Auto MPG Regression

## Source
* The data was obtained from the UCI Machine Learning Repository

## Objective
* Create a model that can determine the MPG of a vehicle given certain parameters

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

## Best Model
* The best model was a Multilayer Perceptron
* An Adjusted R2 score of 0.75 with ten fold cross-validation

## Deployment
* Tkinter GUI application