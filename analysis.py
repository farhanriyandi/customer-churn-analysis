import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)

def plot_churn_distribution(df):
    """Plots the distribution of the churn column."""
    df['churn'].value_counts().plot(kind='bar')
    plt.title('Customer Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.show()

print("Added data visualization function.")
