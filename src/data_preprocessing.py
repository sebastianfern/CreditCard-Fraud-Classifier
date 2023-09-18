# data_preprocessing.py
import pandas as pd
from utils import class_adj

def load_and_clean_data(filepath):
    fraud_data = pd.read_csv(filepath)
    fraud_data['Class'] = fraud_data['Class'].apply(class_adj)
    return fraud_data

def save_cleaned_data(fraud_data, filepath):
    fraud_data.to_csv(filepath, index=False)


