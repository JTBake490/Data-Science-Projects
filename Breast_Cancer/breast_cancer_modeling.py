import numpy as np
import warnings
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import make_scorer, accuracy_score, f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression

warnings.filterwarnings('ignore')

RANDOM_STATE = 10

df = load_breast_cancer(as_frame=True)['frame']
X = df.loc[:, ['mean radius', 'mean perimeter', 'mean area', 'mean concave points', 'worst radius', 'worst perimeter', 'worst area', 'worst concave points']]
y = df.iloc[:, -1]

log_reg = LogisticRegression(solver='lbfgs',max_iter=10_000)
ss = StandardScaler()
pipe = make_pipeline(ss, log_reg)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

scoring = {}
scoring['accuracy'] = make_scorer(accuracy_score)
scoring['f1'] = make_scorer(f1_score)
scoring['roc_auc'] = make_scorer(roc_auc_score, average='weighted')

params = {}
params['logisticregression__C'] = np.arange(0.1, 1.1, 0.1)
params['logisticregression__penalty'] = ['none', 'l2'] # C will be ignored for none
params['logisticregression__class_weight'] = ['balanced', None]

grid = GridSearchCV(estimator=pipe, param_grid=params, scoring=scoring, cv=skf, refit='roc_auc')
grid.fit(X, y)

if __name__ == '__main__':
    ROUNDING = 4

    top_cv_idx = list(grid.cv_results_['rank_test_roc_auc']).index(1)
    corresponding_accuracy = grid.cv_results_['mean_test_accuracy'][top_cv_idx]
    corresponding_f1 = grid.cv_results_['mean_test_f1'][top_cv_idx]
    
    print(f'Top ROC_AUC Score ->              {np.round(grid.best_score_, ROUNDING)}')
    print(f'Corresponding Accuracy Score ->   {np.round(corresponding_accuracy, ROUNDING)}')
    print(f'Corresponding F1 Score ->         {np.round(corresponding_f1, ROUNDING)}')
