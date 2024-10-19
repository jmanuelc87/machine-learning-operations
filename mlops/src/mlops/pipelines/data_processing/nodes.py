import numpy as np
import pandas as pd


def remove_null_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def rename_columns(df: pd.DataFrame, params) -> pd.DataFrame:
    renamed = df[params.keys()].rename(params, axis=1, inplace=False)
    return renamed