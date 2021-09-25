import sys
from multiprocessing import cpu_count

import numpy as np
import pandas as pd

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.dummy import DummyRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor


data_file = sys.argv[1]
sep = '\t'
column_names = ('mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
                'acceleration', 'model_year', 'origin', 'car_name')

col_types = {
    'mpg' : np.float64,
    'cylinders' : np.int64,
    'displacement' : np.float64,
    'horsepower' : np.float64,
    'weight' : np.float64,
    'acceleration' : np.float64,
    'model_year' : np.int64,
    'origin' : np.int64,
}

df_raw = pd.read_csv(data_file, sep=sep, header=None)
temp = df_raw[0].str.split(expand=True)
df = pd.concat((temp, df_raw[1]), axis=1)
df.columns = column_names
df.horsepower.replace({'?' : np.nan}, inplace=True)
df = df.astype(col_types)

# At this point, create a Seaborn pairplot.

# Modeling
MAX_ITER = 20_000
CV = 10 
RANDOM_STATE = 1_000
CORES = cpu_count() // 2

scores = ('r2', 'neg_root_mean_squared_error', 'neg_median_absolute_error')
X, y = df.loc[:, ['displacement', 'horsepower', 'weight', 'model_year']], df.iloc[:, 0]

count = y.shape[0] // CV
features = X.shape[1]
# scikit-learn doese not have adjusted R2 by default
adj_r2_score = lambda r2: (1) - ((1 - r2) * (count - 1) / (count - features - 1))

imp = IterativeImputer(sample_posterior=True)
ct = make_column_transformer((imp, ['horsepower']), remainder='passthrough')
ft = FunctionTransformer(func=np.log, validate=True)

cv_scores = {}

regular_algos = {
    'dummy' : DummyRegressor(strategy='mean'),
    'rfr' : make_pipeline(ct, RandomForestRegressor(random_state=RANDOM_STATE)),
}

scaled_algos = {
    'mlp' : make_pipeline(ct, ft, StandardScaler(), MLPRegressor(max_iter=MAX_ITER, random_state=RANDOM_STATE, n_iter_no_change=5)),
    'knn' : make_pipeline(ct, ft, StandardScaler(), KNeighborsRegressor())
}
    
for name, pipe in regular_algos.items():
    cv_scores[f'{name}_model'] = cross_validate(pipe, X, y, cv=CV, n_jobs=CORES, scoring=scores)

for name, pipe in scaled_algos.items():
    cv_scores[f'{name}_model'] = cross_validate(pipe, X, y, cv=CV, n_jobs=CORES, scoring=scores)


if __name__ == '__main__':
    # Mean Cross Validated results
    for model, metrics in cv_scores.items():
        adj_r2s = np.array([adj_r2_score(r2) for r2 in metrics['test_r2']])
        print(model)
        print(f'R2_mean: {metrics["test_r2"].mean()}')
        print(f'ADJ_R2_mean: {adj_r2s.mean()}')
        print(f'RMSE_mean: {metrics["test_neg_root_mean_squared_error"].mean()}')
        print(f'MidAE_mean: {metrics["test_neg_median_absolute_error"].mean()}')
        print()