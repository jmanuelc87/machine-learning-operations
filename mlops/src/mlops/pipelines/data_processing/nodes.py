import numpy as np
import pandas as pd


def convert_to_csv(df: pd.DataFrame) -> pd.DataFrame:
    return df


def rename_columns(df: pd.DataFrame, params) -> pd.DataFrame:
    renamed = df[['X1','X2','X3','X4','X5','X6','X7','X8','Y1','Y2']] \
        .rename(params, axis=1, inplace=False)

    return renamed


def remove_null_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()