import numpy as np
import pandas as pd

from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import make_pipeline

from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer
from sklearn.compose import make_column_transformer
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate, LeaveOneOut, GridSearchCV

RANDOM_STATE = 100

col_names = (
    'animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne',
    'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous',
    'fins', 'legs', 'tail', 'domestic', 'catsize', 'type'
)

df = pd.read_csv('../../ML Datasets/zoo/zoo.data', header=None)
df.columns = col_names
X, y = df.iloc[:, 1:-1], df.iloc[:, -1]

imputer = KNNImputer()
loo = LeaveOneOut()
ros = RandomOverSampler(random_state=RANDOM_STATE)
scaler = MinMaxScaler()
ct = make_column_transformer(
    (imputer, slice(0, 17)),
    (scaler, [-4]),
    remainder='passthrough'
)

estimators = {}
estimators['dummy'] = DummyClassifier(strategy='most_frequent')
estimators['knn'] = KNeighborsClassifier(n_neighbors=3, algorithm='brute')
estimators['gnb'] = GaussianNB()

pipes = {}
for name, estimator in estimators.items():
    pipe = make_pipeline(ct, ros, estimator)
    pipes[name] = pipe

results = {}
for name, pipe in pipes.items():
    results[name] = cross_validate(pipe, X, y, cv=loo)

dummy_results = results['dummy']['test_score']
knn_results = results['knn']['test_score']
gnb_results = results['gnb']['test_score']

if __name__ == '__main__':
    import pathlib
    import joblib

    print(f'Dummy mean score:                {dummy_results.mean()}')
    print(f'K Nearest Neighbors mean score:  {knn_results.mean()}')
    print(f'Gaussian Naive Bayes mean score: {gnb_results.mean()}')
    print()

    # At this point it became clear that KNN performed slightly better than GNB

    params = {}
    params['kneighborsclassifier__n_neighbors'] = [3, 5, 7, 9]
    params['kneighborsclassifier__weights'] = ['uniform', 'distance']
    params['kneighborsclassifier__algorithm'] = ['brute']

    knn_pipe = pipes['knn']
    grid = GridSearchCV(estimator=knn_pipe, param_grid=params, cv=loo, refit='accuracy')
    grid.fit(X, y)

    print(f'Grid Searched KNN {grid.best_score_}')
    
    model = grid.best_estimator_
    model_name = 'zoo_model.joblib'

    with pathlib.Path(model_name) as model_path:
        joblib.dump(model, model_path)
