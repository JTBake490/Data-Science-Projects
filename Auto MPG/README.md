# Notes For Auto MPG Regression

## Source
* The data was obtained from the UCI Machine Learning Repository
* Auto MPG Page: https://archive.ics.uci.edu/ml/datasets/auto+mpg
* Auto MPG Download Page: https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/

## Environment
* All packages and dependencies are located in requirements.yml
* Run the following command to create an environment
```
conda env create --file requirements.yml
```

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
