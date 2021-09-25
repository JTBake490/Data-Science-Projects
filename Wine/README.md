# Notes For Wine Classification

## Features
* Used a Seaborn pairplot to determine any obvious correlations and separability
* Settled on the following columns based on the pairplot
    - alcohol 
    - malic_acid
    - flavanoids
    - nonflavanoid_phenols
    - color_intensity
    - hue
    - od280/0d315_of_diluted_wines
    - proline

## Models Use
* Extra Randomized Trees Classifier
* Random Forest Classifier
* K Nearest Neighbors Classifier

## Preprocessing
* Scaling For The K Nearest Neighbors Classifier
    - Most features use measurements which fall between zero and five units. The three exceptions were alcohol, color_intensity, and proline.
    - The standard scaler was used on the three mentioned features

## Model Chosen
* Both the extra trees and random forest provided leave one out cross validated scores close to 98%. Extra Trees was chosen for the model.
    - Note: While both models only misclassified four datapoints, the misclassified datapoints were not the same.

## Deployment
* Tkinter GUI application
