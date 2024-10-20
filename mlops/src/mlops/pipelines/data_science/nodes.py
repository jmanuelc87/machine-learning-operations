import pandas as pd

from category_encoders import BinaryEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score


def feature_standard_scaling(df: pd.DataFrame, params) -> pd.DataFrame:
    features = df[params['scaling']]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(X=features)
    return pd.DataFrame(data=scaled_data, columns=features.columns)


def feature_encoding(df: pd.DataFrame, params) -> pd.DataFrame:
    features = df[params['encoding']]
    encoder = BinaryEncoder(cols=params['encoding'])
    categorical_data = encoder.fit_transform(features)
    return categorical_data


def feature_merge(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)
    dataset = pd.concat(objs=[df1, df2], axis=1)
    return dataset


def separate_targets(df: pd.DataFrame) -> pd.DataFrame:
    features = df.drop(columns=["Y1", "Y2"])
    cooling_target = df[["Y2"]]
    heating_target = df[["Y1"]]
    return features, heating_target, cooling_target
    

def features_train_test_split(df1: pd.DataFrame, target: pd.DataFrame, params):
    X_train, X_test, y_train, y_test = train_test_split(df1, target,  test_size=params['test_size'], random_state=params['random_state'], shuffle=True)
    return X_train, X_test, y_train, y_test