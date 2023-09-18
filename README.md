# CreditCard-Fraud-Classifier
Fraud detection system that uses Decision Tree classifiers to identify potentially fraudulent transactions. 

This system utilizes various data preprocessing techniques, such as handling imbalanced classes, and evaluates the model's performance using metrics like precision, recall, and F1-score. Additionally, experimented with threshold tuning to try and improve the model's ability to correctly classify instances of fraud. Will utulize logistic regression,then random forest algorithms to achieve higher predictive accuracy. Also will compare its [precision, recall, f1-score] to to the decision tree to show its improvement of each.  
Decision Tree Classification Report:[
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     85307
           1       0.36      0.82      0.50       136

    accuracy                           1.00     85443
   macro avg       0.68      0.91      0.75     85443
weighted avg       1.00      1.00      1.00     85443


Confusion Matrix:
[[85108   199]
 [   24   112]]

Accuracy Score:
0.9973900729141065

AUC-ROC:
0.9112674103014786
>1, train: 0.917, test: 0.983
>2, train: 0.919, test: 0.986
>3, train: 0.936, test: 0.962
>4, train: 0.947, test: 0.945
>5, train: 0.961, test: 0.964
>6, train: 0.974, test: 0.968
>7, train: 0.983, test: 0.986
>8, train: 0.987, test: 0.990
>9, train: 0.989, test: 0.992
]
