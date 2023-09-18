# CreditCard-Fraud-Classifier

## Overview
This project serves as a critical re-evaluation of the most popular Kaggle notebook for the Credit Card Fraud Dataset ([source](https://www.kaggle.com/datasets/joebeachcapital/credit-card-fraud)) focused on identifying fraudulent credit card transactions using Decision Tree classifiers. The original notebook provided valuable insights into credit card fraud detection but had room for methodological improvement. Specifically, it applied oversampling techniques before splitting the data into training and test sets, leading to potentially misleading results. To address this issue, we first split the dataset into training and test sets, and then apply oversampling techniques—specifically, SMOTE and RandomOverSampler—only to the training data, in line with best practices. Although the original author intended for the oversampling to balance the data, our findings suggest that oversampling may not be the most effective approach in this case. We substantiate this claim by evaluating the corrected model's performance using metrics such as precision, recall, F1-score, and AUC-ROC, providing a more robust and reliable assessment of its capabilities.

## Decision Tree Classification Report without resampling
 

### Initial Class distribution
  
![Initial_noResampling](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/854b1569-0bb4-468a-a3ec-ffd4a0eb5fbc)

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Class 0 (Non-Fraud) | 1.00 | 1.00 | 1.00 | 85,307 |
| Class 1 (Fraud) | 0.77 | 0.81 | 0.79 | 136 |
| Accuracy | 1.00 | | | 85,443 |
| Macro Avg | 0.88 | 0.90 | 0.89 | 85,443 |
| Weighted Avg | 1.00 | 1.00 | 1.00 | 85,443 |

### Confusion Matrix
[[85,274 33]
[ 26 110]]

### Accuracy Score
0.9993094811745842

### AUC-ROC
0.8731373933867919

### Results for the First Decision Tree

1. Train AUC-ROC: 0.999, Test AUC-ROC: 0.999
2. Train AUC-ROC: 0.999, Test AUC-ROC: 0.999
3. Train AUC-ROC: 0.999, Test AUC-ROC: 0.999
4. Train AUC-ROC: 0.999, Test AUC-ROC: 0.999
5. Train AUC-ROC: 1.000, Test AUC-ROC: 1.000
6. Train AUC-ROC: 1.000, Test AUC-ROC: 1.000
7. Train AUC-ROC: 1.000, Test AUC-ROC: 0.999
8. Train AUC-ROC: 1.000, Test AUC-ROC: 1.000
9. Train AUC-ROC: 1.000, Test AUC-ROC: 1.000

### Train scores vs Test scores
 
![decisionTree_noResamplingtrainTestComparison](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/009a43e2-c512-4cd7-b506-700e2397a281)

## Decision Tree Classification Report using imbalanced-learn RandomOverSampler
  
  
### Class distribution before and after resampling
  
![before_after_oversampling](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/ec773f01-4c1e-4606-8ea2-a462a7d869c3)

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

### Results for the Second Decision Tree

1. Train AUC-ROC: 0.917, Test AUC-ROC: 0.983
2. Train AUC-ROC: 0.919, Test AUC-ROC: 0.986
3. Train AUC-ROC: 0.936, Test AUC-ROC: 0.962
4. Train AUC-ROC: 0.947, Test AUC-ROC: 0.945
5. Train AUC-ROC: 0.961, Test AUC-ROC: 0.964
6. Train AUC-ROC: 0.974, Test AUC-ROC: 0.968
7. Train AUC-ROC: 0.983, Test AUC-ROC: 0.986
8. Train AUC-ROC: 0.987, Test AUC-ROC: 0.990
9. Train AUC-ROC: 0.989, Test AUC-ROC: 0.992

### Train scores vs Test scores

![decisionTree_trainTestComparison](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/b1a6af76-96c8-43f4-b487-7a8fbe413ede)

## Decision Tree Classification Report using imbalanced-learn SMOTE
 
 
### Class distribution before and after resampling

![before_after_oversampling](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/30295379-c3e0-42f0-9630-789c092ba0cf)

|             | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Class 0 (Non-Fraud) | 1.00 | 1.00 | 1.00 | 85,307 |
| Class 1 (Fraud) | 0.26 | 0.86 | 0.40 | 136 |
| Accuracy | 1.00 | | | 85,443 |
| Macro Avg | 0.63 | 0.93 | 0.70 | 85,443 |
| Weighted Avg | 1.00 | 1.00 | 1.00 | 85,443 |

### Confusion Matrix
[[84971 336]
[ 19 117]]

### Accuracy Score
0.9958451833386

### AUC-ROC
0.902443829173387

### Results for the Third Decision Tree

1. Train AUC-ROC: 0.943, Test AUC-ROC: 0.967
2. Train AUC-ROC: 0.949, Test AUC-ROC: 0.981
3. Train AUC-ROC: 0.959, Test AUC-ROC: 0.962
4. Train AUC-ROC: 0.964, Test AUC-ROC: 0.984
5. Train AUC-ROC: 0.973, Test AUC-ROC: 0.980
6. Train AUC-ROC: 0.978, Test AUC-ROC: 0.986
7. Train AUC-ROC: 0.983, Test AUC-ROC: 0.983
8. Train AUC-ROC: 0.987, Test AUC-ROC: 0.984
9. Train AUC-ROC: 0.991, Test AUC-ROC: 0.991

### Train scores vs Test scores

![decisionTree_SMOTEtrainTestComparison](https://github.com/sebastianfern/CreditCard-Fraud-Classifier/assets/70400042/afe8984a-696c-4543-9200-833436360852)

## Dataset Citation
This project uses the Credit Card Fraud Dataset, which is available on OpenML. The original dataset was authored by Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson, and Gianluca Bontempi and is cited as follows:
Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. "Calibrating Probability with Undersampling for Unbalanced Classification." In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015.


