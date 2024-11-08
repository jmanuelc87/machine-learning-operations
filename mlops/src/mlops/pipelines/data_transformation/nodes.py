import numpy as np
import pandas as pd

from category_encoders import BinaryEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def remove_null_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    renamed = df.rename({
        "X1": "Relative Compactness",
        "X2": "Surface Area",
        "X3": "Wall Area",
        "X4": "Roof Area",
        "X5": "Overall Height",
        "X6": "Orientation",
        "X7": "Glazing Area",
        "X8": "Glazing Area Distribution",
        "Y1": "Heating Load",
        "Y2": "Cooling Load"
    }, axis=1, inplace=False)
    return renamed

def feature_standard_scaling(df: pd.DataFrame):
    features = df[["Relative Compactness", "Surface Area", "Wall Area", "Roof Area"]]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(X=features)
    return pd.DataFrame(data=scaled_data, columns=features.columns), scaler


def feature_encoding(df: pd.DataFrame):
    features = df[["Overall Height", "Orientation", "Glazing Area", "Glazing Area Distribution"]]
    encoder = BinaryEncoder(cols=["Overall Height", "Orientation", "Glazing Area", "Glazing Area Distribution"])
    categorical_data = encoder.fit_transform(features)
    return categorical_data, encoder


def feature_merge(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)
    dataset = pd.concat(objs=[df1, df2], axis=1)
    return dataset


def separate_targets(df: pd.DataFrame) -> pd.DataFrame:
    features = df.drop(columns=["Heating Load", "Cooling Load"])
    cooling_target = df[["Cooling Load"]]
    heating_target = df[["Heating Load"]]
    return features, heating_target, cooling_target


def features_train_test_split(df1: pd.DataFrame, target: pd.DataFrame, params):
    X_train, X_test, y_train, y_test = train_test_split(df1, target,  test_size=params['test_size'], random_state=params['random_state'], shuffle=True)
    return X_train, X_test, y_train, y_test