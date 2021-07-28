#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
import numpy as np

if __name__ == "__main__":

    path = '/home/maksim/Desktop/datasets/binary/blood-transfusion-service-center.csv'
    data = np.loadtxt(open(path, "rb"), delimiter=",", skiprows=1)
    X, y = data[:,0:-1],data[:,-1]

    X_train, X_test, y_train, y_test = \
            sklearn.model_selection.train_test_split(X, y, random_state=1)

    automl = autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=30)

    automl.fit(X_train, y_train)

    y_hat = automl.predict(X_test)

    print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))
    

