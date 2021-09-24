from sklearn.datasets import load_iris
from sklearn.model_selection import LeaveOneOut, cross_validate
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

RANDOM_STATE = 10

df = load_iris(as_frame=True)['frame']
X, y = df.iloc[:, :-1], df.iloc[:, -1]

loo = LeaveOneOut()
norm = Normalizer()

pipes = {
    'dummy' : make_pipeline(DummyClassifier(strategy='constant', constant=1)),
    'knn' : make_pipeline(norm, KNeighborsClassifier()),
    'gnb' : make_pipeline(norm, GaussianNB())
}

scores = {}
for name, pipe in pipes.items():
    scores[name] = cross_validate(pipe, X, y, cv=loo)

dummy_scores = scores['dummy']
knn_scores = scores['knn']
gnb_scores = scores['gnb']

if __name__ == '__main__':
    # Display Scores In The Console
    print(f"Dummy Mean Cross Validated Accuracy Score:                 {dummy_scores['test_score'].mean()}")
    print(f"KNN Mean Cross Validated Accuracy Score:                   {knn_scores['test_score'].mean()}")
    print(f"Gaussian Naive Bayes Cross Validated Accuracy Score:       {gnb_scores['test_score'].mean()}")