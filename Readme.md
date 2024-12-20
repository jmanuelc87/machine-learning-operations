# MLOps

[![Python version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://pypi.org/project/kedro/)
[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)
## INTRODUCCIÓN


El proyecto busca desarrollar un pipeline de Machine Learning que abarque todas las etapas del ciclo desde la extracción y manipulación de datos, hasta el desarrollo del modelo y la implementación de un pipeline que automatice estas tareas.

El dataset utilizado se basa en el análisis de 12 formas de edificios diferentes, los cuales fueron simulados en el software Ecotect y 
se obtuvieron 768 formas de edificios en distintos entornos de ejecución, los edificios tienen diversas características como área de superficie, de pared y acristalamiento. Son en total 8 las variables de entrada, las cuales buscan obtener la carga de calefacción y enfriamento, siendo estas las variables de salida del conjunto de datos.

El link del dataset se encuentra en : https://archive.ics.uci.edu/dataset/242/energy+efficiency 

La siguente imagen describe las variables del archvivo:
<img width="935" alt="image" src="https://github.com/user-attachments/assets/80106791-b69a-4c02-8e93-a80bcd6f3bc3">


## NECESIDAD

Este proyecto se realiza debido a que es necesario poder evaluar y afianzar las capacidades de los miembros del equipo en el desarrollo de pipelines de ML, deben estar preparados para abordar diferentes tareas como: 

* Manipulación y preparación de datos.
* Exploración y preprocesamiento de datos.
* Uso de técnicas de versionado de datos.
* Construcción y evaluación de modelos de ML.
* Desarrollo y estructuración de modelos de ML y desarrollo de pipelines aplicando buenas prácticas.

El proyecto será evaluado y revisado por la plana docente del curso de MLOps del Tecnológico de Monterrey


## TECNOLOGÍAS UTILIZADAS

- Python
- Archivos de configuración yaml
- Xml
- Kedro
- MLflow


## REPOSITORIO DE TRABAJO

El repositorio en el que estamos trabajando tiene por nombre: machine-learning-operations

Se puede acceder a él dando clic en: https://github.com/jmanuelc87/machine-learning-operations 

## EXPLORACIÓN DE DATOS

Se realizaron técnicas de exploración de datos como análisis de completitud, correlación entre variables, distribución de valores, escalamiento de variables numéricas y nos apoyamos en gráficos como histogramas y diagramas de cajas. Para el desarrollo del modelo, se exploraron los algoritmos de Regresión Lineal, Random Forest y XGBoost siendo el último donde se obtuvo una mayor precisión, con una media del 98%.

El notebook donde se puede revisar este código se encuentra en: https://github.com/jmanuelc87/machine-learning-operations/blob/orlando/mlops/notebooks/Experimental%20ML%20Process.ipynb 

## PROCESO GENERADO 

Para el cumplimiento del objetivo, se desarrolló un proceso compuesto de los nodos de la imagen: 

![kedro pipeline](https://github.com/jmanuelc87/machine-learning-operations/blob/main/mlops/docs/images/kedro-pipeline.svg)

## INICIO DE INSTALACIÓN 

Para descargar y trabajar en una copia local, se debe seguir los siguientes pasos: 

### PRE-REQUISITOS

Previamente, se debe descargar a la máquina que ejecutará el código, las siguientes herramientas: 
 
* Python  
* Programa editor de Texto (VS Code, PyCharm)
* Git

### DESCARGA

1. Clonar el repositorio

Para descargar una copia del proyecto abrir una consola de Git y ejecutar el comando: 

`git clone https://github.com/jmanuelc87/machine-learning-operations.git`

2. Descargar kedro via pip o condra

`pip install kedro`

`conda install -c conda-forge kedro`


### EJECUCIÓN

1. Ve al folder de /mlops.
2. Valida que tengas python y kedro instalados.
`python --version` &
`kedro info`
3. Inicializa kedro con `kedro run` o `kedro viz run` para la visualizacion del pipeline
4. Si elegiste la visualizacion, deberia abrirte una pestaña del navegador o ve a http://127.0.0.1:4141/?pid=__default__&expandAllPipelines=false



## EQUIPO DE TRABAJO - GRUPO 9

El equipo está conformado por los siguientes miembros: 

* Orlando Marath Barraza Aguilar
* Juan Manuel Carballo Montaño
* Luis Miguel Farfán Lara
* Didier Omar Gamboa Angulo
* Jorge Luis Pedroza Rivera
* Emily Ann Sedán Herrera


La forma de interacción y coordinación es de manera digital, haciendo uso de grupos de Whatsapp, reuniones virtuales y empleando herramientas de trabajo colaborativo.
Los miembros del equipo residen en diferentes estados de México y algunos en Perú. Además, trabajan en diferentes sectores como consultoría y aerolíneas y cuentan con diferentes skills en tecnologías como Java, Go, Python y Oracle.