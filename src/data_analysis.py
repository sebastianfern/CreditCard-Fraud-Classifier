# data_analysis.py
import seaborn as sns
import matplotlib.pyplot as plt

def plot_class_distribution(fraud_data, title='Class Distribution'):
    """
    Plot the class distribution of a dataset
    """
    plt.bar(['Class 0', 'Class 1'], [sum(fraud_data == 0), sum(fraud_data == 1)], color=['blue', 'orange'])
    plt.title(title)
    plt.ylabel('Count')
    plt.show()

def plot_class_balance_before_after(y_train, y_resampled):
    plt.subplot(1, 2, 1)
    plt.bar(['Class 0', 'Class 1'], [sum(y_train == 0), sum(y_train == 1)], color=['blue', 'orange'])
    plt.title('Before Oversampling')
    plt.ylabel('Count')

    plt.subplot(1, 2, 2)
    plt.bar(['Class 0', 'Class 1'], [sum(y_resampled == 0), sum(y_resampled == 1)], color=['blue', 'orange'])
    plt.title('After Oversampling')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()

def plot_synthetic_data(y_synthetic):
    """
    Plot the class distribution of synthetic data
    """
    plot_class_distribution(y_synthetic, title='Synthetic Data')

