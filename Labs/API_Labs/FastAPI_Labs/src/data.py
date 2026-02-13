import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def load_data():
    wine_dataset = load_wine()
    X = wine_dataset.data
    y = wine_dataset.target
    feature_names = wine_dataset.feature_names
    return X, y, feature_names

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12)
    return X_train, X_test, y_train, y_test