import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

def load_model(model_path):
    return load(model_path)

def load_data(data_path):
    return pd.read_csv(data_path)

def test_fraud_cases(model, data):
    test_rows = [541, 623, 4920, 6108, 6329]  # Indexes of fraudulent rows
    for row_num in test_rows:
        test_data = data.iloc[row_num].drop('Class')
        true_label = data.iloc[row_num]['Class']
        
        # Assuming that your data needs to be scaled
        scaler = StandardScaler()
        test_data_scaled = scaler.fit_transform(test_data.values.reshape(-1, 1))
        
        prediction = model.predict(test_data_scaled.reshape(1, -1))
        print(f"Row {row_num}: True label = {true_label}, Predicted = {prediction[0]}")

if __name__ == "__main__":
    model_path = "./src/src"  # Replace with your model path
    data_path = "../data\cleaned_data.csv"  # Replace with your data path

    trained_model = load_model(model_path)
    data = load_data(data_path)

    print("Testing specific fraud cases...")
    test_fraud_cases(trained_model, data)
