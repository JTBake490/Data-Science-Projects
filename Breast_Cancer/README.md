# Notes For Breast Cancer Classification

## Environment
* All packages and dependencies are located in requirements.yml
* Run the following command to create an environment
```
conda env create --file requirements.yml
```

## Features
* The Seaborn countplot is to help show the number of malignant cases vs benign cases
    - While 62.7% of the cases were benign, I determined it was not a significant amount to warrent oversampling or undersampling
* Used a Seaborn pairplot to determine any obvious separability
* Settled on the following columns based on the pairplot
    - mean radius
    - mean perimeter
    - mean area
    - mean concave points
    - worst radius
    - worst perimeter
    - worst area
    - worst concave points

## Models Used
* Logistic Regression
* Decision Tree Classifier

## Preprocessing
* Tried Scaling For The Logistic Regression
    - One grid search parameter that was tuned was the penalty term. The two penalty terms tested for were l2 and none (no penalty). As a result, the grid search was run with and without a standard scaler. Although logistic regression does not require scaling if a penalty term is not used, scaling resulted in better cross validated metrics


## Model Chosen
* Logistic Regression without a penalty term
    - Ran a gird search using stratified five fold cross validation
    - The metric to determine the best estimator was the best mean AUC ROC score
    - Top mean AUC ROC score: 0.9571
    - Corresponding mean Accuracy score: 0.9631
    - Corresponding mean F1 score: 0.9712

## Deployment
* Tkinter GUI application
