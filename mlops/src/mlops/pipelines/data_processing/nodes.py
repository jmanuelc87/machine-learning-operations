import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split

def convert_to_csv(df: pd.DataFrame) -> pd.DataFrame:
    return df


def rename_columns(df: pd.DataFrame, params) -> pd.DataFrame:
    renamed = df[['X1','X2','X3','X4','X5','X6','X7','X8','Y1','Y2']] \
        .rename(params, axis=1, inplace=False)

    return renamed


def remove_null_values(df: pd.DataFrame) -> pd.DataFrame:
    values_df = df.isnull().sum()
    all = values_df.to_numpy()
    if np.sum(all) == 0:
        return df
    else:
        df = df.dropna()
        return df


def feature_isolation_and_split(df: pd.DataFrame, params):
    features = df.drop(columns=params['removed'])
    target = df[params['target']]
    X_train, X_test, target_train, target_test = train_test_split(features, target,  test_size=params['test_size'], random_state=params['random_state'], shuffle=True)
    return X_train, X_test, target_train, target_test