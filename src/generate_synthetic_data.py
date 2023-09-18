from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import pandas as pd

def generate_synthetic_test_data(original_data, test_size=0.3):
    X = original_data.drop('Class', axis=1)
    y = original_data['Class']

    # Splitting the data into train and test sets to isolate some data for SMOTE
    X_train, X_test_real, y_train, y_test_real = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Applying SMOTE
    sm = SMOTE(random_state=42)
    X_synthetic, y_synthetic = sm.fit_resample(X_train, y_train)
    
    return X_synthetic, y_synthetic
