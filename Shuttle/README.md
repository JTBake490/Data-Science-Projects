# Notes For Shuttle Classification

## Source
* Data came separated into two files from the UCI Machine Lerning Repository:
    - shuttle_train
    - shuttle_test
* Shuttle Page: https://archive.ics.uci.edu/ml/datasets/Statlog+(Shuttle)
* Shuttle Download Page: https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/

## Environment
* All packages and dependencies are located in requirements.yml
* Run the following command to create an environment
```
conda env create --file requirements.yml
```

## EDA and Preprocessing
- No missing values
- Imbalanced 
    - not too concerned since the data came pre-split
    - the goal is to build a model that performs well to the test dataset provided.
- No Column Names
- No feature engineering performed

## Model Chosen
- Random Forest Classifier
- Metrics for the chosen model
    - Accuracy: 99%
    - Precision: 99%
    - Recall: 95.3%
    - F1 Score: 97.38%

## Deployment
* Flask web app
* TKinter GUI
