# Notes For Zoo Type Classification

## Source
* The data for this project came from the UCI Machine Learning Repository

## Environment
* All packages and dependencies are located in requirements.yml
* Run the following command to create an environment
```
conda env create --file requirements.yml
```

## Features
* All but one of the features are binary
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

## Class Imbalance
* The Seaborn Count Plot shows there is class imbalance
    - There are more values of type one than the other types
* A random oversampler was used to oversample the non-majority types

## Model Chosen
* K Nearest Neighbors
    - Ran a gird search optimizing the weights and n_neighbors
    - Leave one out cross validation
    - Mean accuracy score: 0.98


## Deployment
* TKinter GUI application
    - Results are Displayed in a popup
