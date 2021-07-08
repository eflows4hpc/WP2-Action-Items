from sklearn import datasets
import pandas as pd
import dislib as ds
import numpy as np
from dislib.classification import RandomForestClassifier
from dislib.model_selection import GridSearchCV

from pycompss.api.api import compss_barrier 

def main():

#loading mnist data
    x, y = ds.load_svmlight_file(
        "../data/train.scaled",
        block_size=(5000, 780), n_features=780, store_sparse=False)

    # Random Forests parameters 
    # n_estimators (int, optional (default=10)) – Number of trees to fit.
    # max_depth (int or np.inf, optional (default=np.inf)) – The maximum depth of the tree. If np.inf, then nodes are expanded until all leaves are pure. 
    parameters = {'n_estimators': (1, 2, 4, 8, 16),
                  'max_depth': range(10, 12)}

    rf = RandomForestClassifier()
    searcher = GridSearchCV(rf, parameters, cv=5)
    np.random.seed(0)
    searcher.fit(x, y)

    compss_barrier() 
#    print(searcher.cv_results_['mean_test_score'])
    pd_df = pd.DataFrame.from_dict(searcher.cv_results_)
    print(pd_df[['params', 'mean_test_score']])
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None):
        print(pd_df)
    print('Best estimator')
    print(searcher.best_estimator_)
    print('Best score')
    print(searcher.best_score_)
    print('Best params')
    print(searcher.best_params_)
    print('Best index')
    print(searcher.best_index_)
    print('Scorer')
    print(searcher.scorer_)
    print('n splits')
    print(searcher.n_splits_)


if __name__ == "__main__":
    main()
