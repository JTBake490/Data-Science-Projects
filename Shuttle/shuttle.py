import sys
from multiprocessing import cpu_count

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer

cores = cpu_count() // 4

        
def basic_stats_classifier(func):
    def inner(*args):
        algo, X_train, y_train, X_test, y_test = args
        outter_func = func(*args)
        y_pred = outter_func.predict(X_test)
        average = 'macro'
        places = 4
        
        print(np.round(accuracy_score(y_test, y_pred), places))
        print(np.round(precision_score(y_test, y_pred, average=average, zero_division=0), places))
        print(np.round(recall_score(y_test, y_pred, average=average), places))
        print(np.round(f1_score(y_test, y_pred, average=average), places))
        print()

        return outter_func
    return inner


@basic_stats_classifier
def train_model(algo, X_train, y_train, X_test=None, y_test=None):
    '''Fits and predicts a classifier. X_test and y_test parameter is for basic_stats_classifier decorator.'''
    return algo.fit(X_train, y_train)


if __name__ == '__main__':
    train, test = sys.argv[1], sys.argv[2]
    
    random_state = 1000
    sep = ' '
    
    df = pd.read_csv(train, sep=sep, header=None)
    test_df = pd.read_csv(test, sep=sep, header=None)
    
    X_train, y_train = df.iloc[:, :-1], df.iloc[:, -1]
    X_test, y_test = test_df.iloc[:, :-1], test_df.iloc[:, -1]
    
    ss = StandardScaler()
    ss.fit(X_train)
    X_train_scaled, X_test_scaled = ss.transform(X_train), ss.transform(X_test)
    
    print('Dummy')
    dummy_model = train_model(DummyClassifier(strategy='most_frequent', random_state=random_state), X_train, y_train, X_test, y_test)
    
    print('Random Forest')
    rfc_model = train_model(RandomForestClassifier(n_jobs=cores, random_state=random_state), X_train, y_train, X_test, y_test)
    
    print('MLP')
    mlp_model = train_model(MLPClassifier(random_state=random_state), X_train_scaled, y_train, X_test_scaled, y_test)
    
    print('KNN')
    knn_model = train_model(KNeighborsClassifier(n_jobs=cores), X_train_scaled, y_train, X_test_scaled, y_test)
