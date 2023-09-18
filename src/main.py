from data_preprocessing import load_and_clean_data, save_cleaned_data
from data_analysis import plot_class_balance_before_after, plot_synthetic_data
from model import evaluate_model
from model_building import train_decision_tree

from model_evaluation import evaluate_tree_depth, find_optimal_threshold
from generate_synthetic_data import generate_synthetic_test_data
import pandas as pd

# Read and clean the data
fraud_data = load_and_clean_data('./data/creditcard_data.csv')

# Model Training
trained_model, X_resampled, y_resampled, X_test, y_test, predictions, probabilities, y_train = train_decision_tree(fraud_data)

# Finding Optimal Threshold
optimal_threshold = find_optimal_threshold(y_test, probabilities)

# Data Analysis and Visualization
plot_class_balance_before_after(y_train, y_resampled)

# # Generate synthetic test data using only X_resampled and y_resampled
# X_synthetic, y_synthetic = generate_synthetic_test_data(pd.concat([X_resampled, y_resampled], axis=1))

# # Visualize the synthetic data to make sure it's balanced
# plot_synthetic_data(y_synthetic)

# # Model Evaluation
# predictions_synthetic = trained_model.predict(X_synthetic)

# Model Evaluation
evaluate_model(y_test, probabilities, optimal_threshold)

# Evaluating Tree Depth using resampled data and original test set
evaluate_tree_depth(X_resampled, y_resampled, X_test, y_test)




