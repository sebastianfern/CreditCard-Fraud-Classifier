#model_evaluation.py
from sklearn.metrics import accuracy_score, precision_recall_curve
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score

import numpy as np


def evaluate_tree_depth(X_train, y_train, X_test, y_test):
    train_scores, test_scores = list(), list()
    values = [i for i in range(1, 10)]
    
    for i in values:
        dtc = DecisionTreeClassifier(max_depth=i)
        dtc.fit(X_train, y_train)
        train_yhat = dtc.predict(X_train)
        train_acc = accuracy_score(y_train, train_yhat)
        train_scores.append(train_acc)

        test_yhat = dtc.predict(X_test)
        test_acc = accuracy_score(y_test, test_yhat)
        test_scores.append(test_acc)
        print('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))
    
    plt.plot(values, train_scores, 'go--', label='Train')
    plt.plot(values, test_scores, '-o', label='Test')
    plt.legend()
    plt.show(block=True)

def find_optimal_threshold(y_true, probabilities, initial_threshold=0.85):
    # Start with a higher initial threshold
    threshold = initial_threshold
    
    # Calculate precision and recall at the initial threshold
    y_pred = (probabilities >= threshold).astype(int)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    
    # If either precision or recall is 0, increment the threshold
    while precision == 0 or recall == 0:
        threshold += 0.05  # You can adjust the step size
        y_pred = (probabilities >= threshold).astype(int)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
    
    return threshold
