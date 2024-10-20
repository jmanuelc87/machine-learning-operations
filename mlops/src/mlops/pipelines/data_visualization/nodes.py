import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

def calculate_stats(df: pd.DataFrame) -> pd.DataFrame:
    stats = df.describe(include="number").T
    stats.insert(0, 'Column Names', df.columns)
    return stats


def calculate_correlations(df: pd.DataFrame) -> tuple:
    correlations = df.corr(method='pearson')
    plt.figure(figsize=(14,11))
    sn.heatmap(correlations, annot=True)
    return plt


def calculate_boxplots(df: pd.DataFrame):
    df.plot(kind='box', subplots=True, layout=(4,4), sharex=False, sharey=False, figsize=(15,15))
    return plt


def compare_r2_metric(lr: pd.DataFrame, rf: pd.DataFrame, xg: pd.DataFrame):
    results = pd.concat([lr, rf, xg], axis=1)
    plt.figure(figsize=(8,4))
    results.boxplot()
    plt.title("Variabilidad de los R2 Scores por Modelo")
    plt.ylabel("R2 Score")
    
    return plt