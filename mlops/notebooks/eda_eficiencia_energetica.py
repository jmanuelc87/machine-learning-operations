# Loading the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

df = pd.read_excel("ENB2012_data.xlsx")
df

"""# Análisis descriptivo"""

df.info()

##Porcentaje valores faltantes por columna
df.isna().mean() * 100

# Primero identificamos cantidad de valores únicos por columna, ya que las que tienen un solo valor único o todos los valores diferentes no serán útiles en análisis y deberían eliminarse antes del EDA.
df.nunique()

##Descriptivas de variables numéricas
df.describe().T

# Calculamos la asimetría para las variables numéricas
df.skew()

# Calculamos curtosis para las variables numéricas
df.kurt()

# Se hace una lista de variables numéricas y otra de categóricas
num_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()

# Se dibujan histogramas combinando Matplotlib y Seaborn para ver la distribución de los valores para cada variable

fig, axes = plt.subplots(4,2, figsize=(15,15)) # ---> Matplotlib
plt.subplots_adjust(wspace=0.3)
axes = axes.ravel()
for col, ax in zip(df[num_cols], axes):
  sns.histplot(x=df[col], ax=ax, bins=10) # ---> Seaborn
  ax.set(title=f'{col}', xlabel=None) # ---> Matplotlib

# Se grafica diagramas de caja para ver distribución de los datos

fig, axes = plt.subplots(4,2, figsize=(15,15))
axes = axes.ravel()
for col, ax in zip(df[num_cols], axes):
  df[col].plot(kind='box', ax=ax) # ---> Pandas

## Gráfico de barras para la variable X7 para ver la frecuencia de cada categoría:
sns.countplot(x='X7', data=df)

## Utilizamos un for para diagramar el gráfico de barras para todas las variables categóricas
fig, axes = plt.subplots(2,2, figsize=(12,8))
axes = axes.ravel()
for col, ax in zip(df[cat_cols], axes):
  sns.countplot(x=df[col], ax=ax) # ---> Seaborn
  ax.set(title=f'{col}', xlabel=None)

## Diagramamos mapa de calor para ver la correlación de las variables
plt.figure(figsize = (14, 10))
sns.heatmap(round(df.corr(numeric_only=True),2), annot = True) # ---> Seaborn