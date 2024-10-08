import pandas as pd


def convert_to_csv(df: pd.DataFrame) -> pd.DataFrame:
    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    renamed = df[['X1','X2','X3','X4','X5','X6','X7','X8','Y1','Y2']] \
        .rename({
            'X1':'Compactness',
            'X2':'Surface Area',
            'X3':'Wall Area',
            'X4':'Roof Area',
            'X5':'Height',
            'X6':'Orientation',
            'X7':'Glazing Area',
            'X8':'Glazing Area dist',
            'Y1':'Heating load',
            'Y2':'Cooling load'}, axis=1, inplace=False)

    return renamed


def calculate_correlations(df: pd.DataFrame) -> pd.DataFrame:
    correlations = df.corr(method='pearson')
    return correlations