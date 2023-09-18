# CreditCard-Fraud-Classifier

## Overview
This project is a fraud detection system that uses Decision Tree classifiers to identify potentially fraudulent credit card transactions. The system employs various data preprocessing techniques, such as handling imbalanced classes, and evaluates the model's performance using metrics like precision, recall, and F1-score. Additionally, it experiments with threshold tuning to improve the model's ability to correctly classify instances of fraud. The project also utilizes Logistic Regression and Random Forest algorithms to achieve higher predictive accuracy and compares their [precision, recall, f1-score] to that of the Decision Tree to demonstrate the improvements.

## Decision Tree Classification Report

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Class 0 (Non-Fraud) | 1.00 | 1.00 | 1.00 | 85,307 |
| Class 1 (Fraud) | 0.36 | 0.82 | 0.50 | 136 |
| Accuracy | 1.00 | | | 85,443 |
| Macro Avg | 0.68 | 0.91 | 0.75 | 85,443 |
| Weighted Avg | 1.00 | 1.00 | 1.00 | 85,443 |

### Confusion Matrix
[[85108   199]
 [   24   112]]


### Accuracy Score
0.9973900729141065

### AUC-ROC
0.9112674103014786

## Threshold Tuning Results

Threshold tuning results for Decison Tree:

1. Train AUC-ROC: 0.917, Test AUC-ROC: 0.983
2. Train AUC-ROC: 0.919, Test AUC-ROC: 0.986
3. Train AUC-ROC: 0.936, Test AUC-ROC: 0.962
4. Train AUC-ROC: 0.947, Test AUC-ROC: 0.945
5. Train AUC-ROC: 0.961, Test AUC-ROC: 0.964
6. Train AUC-ROC: 0.974, Test AUC-ROC: 0.968
7. Train AUC-ROC: 0.983, Test AUC-ROC: 0.986
8. Train AUC-ROC: 0.987, Test AUC-ROC: 0.990
9. Train AUC-ROC: 0.989, Test AUC-ROC: 0.992

![before_after_oversampling](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/30295379-c3e0-42f0-9630-789c092ba0cf)
![decisionTree_trainTestComparison](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/b1a6af76-96c8-43f4-b487-7a8fbe413ede)


