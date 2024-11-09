import pytest
import unittest
import numpy as np
import pandas as pd
import hypothesis.strategies as st

from collections import defaultdict
from mlops.pipelines.data_transformation.nodes import remove_null_values, rename_columns, feature_standard_scaling, feature_encoding

@pytest.fixture
def dataframe_with_nulls():
    decimals = st.deferred(lambda: st.floats(allow_nan=True))
    list = []
    for i in range(10):
        list.append(decimals.example())
    
    return pd.DataFrame(data=list, columns=['0'])


@pytest.fixture
def dataframe_with_cols():
    cols = ["Relative Compactness", "Surface Area", "Wall Area", "Roof Area", "Overall Height", "Orientation", "Glazing Area", "Glazing Area Distribution"]
    dict = defaultdict(list)
    for c in cols:
        dict[c].extend([15, 10, 5])
        
    return pd.DataFrame(data=dict)


def test_remove_null_values(dataframe_with_nulls):
    
    non_nulls_df = remove_null_values(dataframe_with_nulls)
    
    assert non_nulls_df.isna().all().item() == False
    
    
def test_rename_columns():
    columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'Y1', 'Y2']
    non_cols_df = pd.DataFrame(data=np.ones((1,10)), columns=columns)
    cols_df = rename_columns(non_cols_df)
    assert len(cols_df.columns) == len(columns) and sorted(cols_df.columns) != sorted(columns)


def test_feature_standard_scaling(dataframe_with_cols):
    scaled_df, model = feature_standard_scaling(dataframe_with_cols)
    assert model.mean_[0] - 10. <= 0.01 and model.var_[0] - 16.66 <= 0.01
    
    
def test_feature_encoding(dataframe_with_cols):
    encoded_df, model = feature_encoding(dataframe_with_cols)
    assert len(encoded_df.columns) == 8