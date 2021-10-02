# Notes For Zoo Type Classification

## Features
* All but one of the features is binary
* None of the features were removed for modeling

## Models Tested During SKLearn Modeling
* K Nearest Neighbors Classifier
* Gaussian Naive Bayes

## Models Tested During PySpark Modeling
* Logistic Regression
* Random Forest Classifier

## Preprocessing
* Min Max Scaler
    - All the features are binary except for legs. The scaler was used to put the range between 0 and 1
* Imputer
    - While there was not any missing data in this dataset, an imputer was added to the column transformer incase a feature is not provided in an application

## Model Chosen
* K Nearest Neighbors
    - Ran a gird search optimizing the weights and n_neighbors
    - Leave one out cross validation
    - Mean accuracy score: 0.98


## Deployment
* TKinter GUI application
    - Results are Displayed in a popup