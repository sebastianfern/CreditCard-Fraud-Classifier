# model.py
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score

def evaluate_model(y_test, probabilities, optimal_threshold):
    """
    Evaluate the machine learning model with custom thresholding.
    Print out the classification report, confusion matrix, and accuracy score.
    Also calculates and prints the AUC-ROC score.
    
    Parameters:
    y_test (array-like): The true labels for the test data.
    probabilities (array-like): The predicted probabilities for the positive class.
    optimal_threshold (float): The custom decision threshold to be used for classifying as 'fraud' or 'not fraud'.
    """
    
    # Using the optimal_threshold to classify 'fraud' and 'not fraud'
    custom_predictions = [1 if prob > optimal_threshold else 0 for prob in probabilities]
    
    print("Classification Report:")
    print(classification_report(y_test, custom_predictions))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, custom_predictions))
    
    print("\nAccuracy Score:")
    print(accuracy_score(y_test, custom_predictions))
    
    # Calculate the AUC-ROC score
    roc_auc = roc_auc_score(y_test, probabilities)
    
    print("\nAUC-ROC:")
    print(roc_auc)

