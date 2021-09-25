from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.model_selection import cross_validate, LeaveOneOut
from sklearn.pipeline import make_pipeline
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

RANDOM_STATE = 10

df = load_wine(as_frame=True)['frame']
X = df.loc[:, ['alcohol', 'malic_acid', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']]
y = df.iloc[:, -1]

loo = LeaveOneOut()
scaler = StandardScaler()

ct = make_column_transformer(
    (scaler, ['alcohol', 'color_intensity', 'proline']),
    remainder='passthrough')

pipelines = {
    'dummy' : make_pipeline(DummyClassifier(strategy='most_frequent', random_state=RANDOM_STATE)),
    'etc' : make_pipeline(ExtraTreesClassifier(random_state=RANDOM_STATE)),
    'rfc' : make_pipeline(RandomForestClassifier(random_state=RANDOM_STATE)),
    'knn' : make_pipeline(ct, KNeighborsClassifier())
}

scores = {}
for name, pipeline in pipelines.items():
    scores[name] = cross_validate(pipeline, X, y, cv=loo)

dummy_scores = scores['dummy']
extra_trees_scores = scores['etc']
random_forest_scores = scores['rfc']
knn_scores = scores['knn']

if __name__ == '__main__':
    print(f"Dummy:                  {dummy_scores['test_score'].mean()}")
    print(f"Extra Randomized Trees: {extra_trees_scores['test_score'].mean()}")
    print(f"Random Forest:          {random_forest_scores['test_score'].mean()}")
    print(f"K Nearest Neighbors:    {knn_scores['test_score'].mean()}")
    