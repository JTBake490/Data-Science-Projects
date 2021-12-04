# Notes Regarding Legendary Pokemon Classification

## Source Data
The data for this project was downloaded from https://www.kaggle.com/mariotormo/complete-pokemon-dataset-updated-090420?select=pokedex_%28Update_04.21%29.csv

## Environment
* All packages and dependencies are located in requirements.yml
* Run the following command to create an environment
```
conda env create --file requirements.yml
```

## Preprocessing
Several columns had many missing values. The way the missing values were handled depended on why the data was missing.
* Base Friendship and Base Experience were missing because new pokemon were created and these values simply had not been added. Since these values are known, these values were added.

* Type 2, Ability 2, Egg Type 2, and Hidden Ability have several hundred null values. These values are null not because the information is unknown but because it is not relevant to many pokemon. Instead of imputing these values, boolean features were created. i.e. has_hidden ability

* Egg Type 1 had three missing values. The pokemon with the missing values are variations of other pokemon without the values missing. Thus these values were imputed using the other variations' values.

* Catch Rate had eighteen values missing. All catch rate values are known and can be looked up on pokemondb.net. Many missing values are galarian variation pokemon. The other missing values are from pokemon variations which can be obtained from another variation and cannot not be caught in the list variation. All these values were imputed with the exact values.

* Ability 1 had three missing values. Two partner variations and one is a special legendary variation. These were imputed using the standard form ability of each pokemon.

* Weight KG, Growth Rate, and Egg Cycles each had one missing value. These values are from alternate form pokemon. These were imputed using the standard values of each pokemon.

* Egg Type 2 had one missing value. The pokemon is a parterner pokemon. The missing value was imputed using the stanard value.

* Percentage Male had missing values because some pokemon are genderless. Instead of using percentage male and percetage female, I created a is_genderless features instead.

## Preprocessing Not Taken
The dataset not only lists every pokemon, but also contains alternate forms of the pokemon as separate pokemon. It was decided to not drop alternate forms since this might affect whether the stat features are a good indicator of a legendary.

## Model Used
Rules based classification using the following features:
* Egg Type 1 (Primary Type)
* Egg Cycles
* Growth Rate
* Catch Rate
* Is Genderless

## Metrics
* A dummy classifier simply predicted _legendary_ if the pokemon's Egg Type 1 is undiscovered. The dummy classifier dummy metrics are as follows:
    - Accuracy:     97.22%
    - Precision:    82.24%
    - Recall:       98.43%
    - F1:           89.61%
    - Roc Auc:      97.74% 
    - 29 Pokemon incorrectly classified:
        * 27 False Positives
        * 2 False Negatives

* Rules based classifier used a combination of the features listed above. The rules based classifier metrics are as follows:
    - Accuracy:     99.52%
    - Precision:    96.92%
    - Recall:       99.21%
    - F1:           98.05%
    - Roc Auc:      99.39% 
    - 5 pokemon incorrectly classified:
        * 4 False Positives
        * 1 False Negative

## Deployment
* Streamlit web application