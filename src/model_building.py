# model_building.py
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

def train_decision_tree(fraud_data):
    # Assuming you have a DataFrame named 'fraud_data'
    X = fraud_data.drop('Class', axis=1)
    y = fraud_data['Class']

    # First, you can split the original data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Then apply random oversampling only to the training set to balance the classes
    oversampler = RandomOverSampler(random_state=42)
    X_resampled, y_resampled = oversampler.fit_resample(X_train, y_train)
    
    # Training a Decision Tree Classifier
    dtc = DecisionTreeClassifier(max_depth=15)
    dtc.fit(X_resampled, y_resampled)  # Use the resampled data for training

    # Making predictions
    predictions = dtc.predict(X_test)
    probabilities = dtc.predict_proba(X_test)[:, 1]

    return dtc, X_resampled, y_resampled, X_test, y_test, predictions, probabilities, y_train


