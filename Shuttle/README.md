# Notes For Shuttle Classification

* Data came separated into two files from the UCI Machine Lerning Repository:
    - shuttle_train
    - shuttle_test

* Regarding the data:
    - No missing values
    - Imbalanced 
        - not too concerned since the data came pre-split
        - the goal is to build a model that performs well to the test dataset provided.
    - No Column Names

* Modeling was fairly straightfoward
    - No feature engineering performed
    - Metrics for some models were well over 90%

* Apps
    - flask web app without CSS
    - TKinter GUI
