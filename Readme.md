Repositorio grupal equipo 9. 
=======

# Proyecto de Operaciones de Aprendizaje Automático

[![Python version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://pypi.org/project/kedro/)
[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Descripción del Proyecto


El proyecto busca desarrollar un pipeline de Machine Learning que abarque todas las etapas del ciclo desde la extracción y manipulación de datos, hasta el desarrollo del modelo y la implementación de un pipeline que automatice estas tareas.

El dataset utilizado se basa en el análisis de 12 formas de edificios diferentes, los cuales fueron simulados en el software Ecotect y 
se obtuvieron 768 formas de edificios en distintos entornos de ejecución, los edificios tienen diversas características como área de superficie, de pared y acristalamiento. Son en total 8 las variables de entrada, las cuales buscan obtener la carga de calefacción y enfriamento, siendo estas las variables de salida del conjunto de datos.

El link del dataset se encuentra en : https://archive.ics.uci.edu/dataset/242/energy+efficiency 

El conjunto de datos incluye 8 variables de entrada y 2 variables de salida, como se muestra en la siguiente imagen:
<img width="935" alt="image" src="https://github.com/user-attachments/assets/80106791-b69a-4c02-8e93-a80bcd6f3bc3">


## Objetivo

Este proyecto permite a los miembros del equipo desarrollar competencias clave en la construcción de pipelines de Machine Learning. Las principales actividades incluyen:

* Manipulación y preparación de datos.
* Exploración y preprocesamiento de datos.
* Uso de técnicas de versionado de datos.
* Construcción y evaluación de modelos de ML.
* Desarrollo y estructuración de modelos de ML y desarrollo de pipelines aplicando buenas prácticas.

El proyecto será evaluado y revisado por la plana docente del curso de MLOps del Tecnológico de Monterrey


## Tecnologías Utilizadas

* **Python**: Lenguaje principal del proyecto
* **Kedro**: Para la creación y gestión del pipeline
* **MLflow**: Para el seguimiento de experimentos y modelos
* **Archivos YAML**: Configuración de nodos y parámetros
* **Git**: Control de versiones

## Estructura del Directorio

```plaintext
.
├── README.md               # Descripción general del proyecto
├── conf                    # Configuraciones para cada entorno
├── data                    # Almacenamiento de datos, particionado en raw, interim, processed y primary
├── docs                    # Documentación del proyecto
├── notebooks               # Notebooks de Jupyter para experimentación y análisis
├── pyproject.toml          # Configuración de dependencias del proyecto
├── requirements.txt        # Dependencias del proyecto
├── session_store.db        # Almacenamiento de sesiones para Kedro
├── src                     # Código fuente del proyecto
└── tests                   # Pruebas para verificar el pipeline
```

## Repositorio de Trabajo

El repositorio en el que estamos trabajando tiene por nombre: machine-learning-operations

Se puede acceder a él dando clic en: https://github.com/jmanuelc87/machine-learning-operations 

## Exploración de Datos

Se realizaron técnicas de exploración de datos como análisis de completitud, correlación entre variables, distribución de valores, escalamiento de variables numéricas y nos apoyamos en gráficos como histogramas y diagramas de cajas. Para el desarrollo del modelo, se exploraron los algoritmos de Regresión Lineal, Random Forest y XGBoost siendo el último donde se obtuvo una mayor precisión, con una media del 98%.

El notebook donde se puede revisar este código se encuentra en: https://github.com/jmanuelc87/machine-learning-operations/blob/orlando/mlops/notebooks/Experimental%20ML%20Process.ipynb 

## Proceso Generado

Para el cumplimiento del objetivo, se desarrolló un proceso compuesto de los nodos de la imagen: 

![kedro pipeline](https://github.com/jmanuelc87/machine-learning-operations/blob/main/mlops/docs/images/kedro-pipeline.svg)


## Instalación y Ejecución

### Pre-requisitos
Asegúrate de tener instalados:

* Python 3.9 o superior
* Git

### Configuración del Entorno
1. Clona el repositorio:
```bash
git clone https://github.com/jmanuelc87/machine-learning-operations.git
```

2. Instala Kedro y las dependencias necesarias:
```bash
pip install kedro
pip install -r requirements.txt
```

Alternativamente, puedes instalar Kedro con conda:

```bash
conda install -c conda-forge kedro
```

### Ejecución del Pipeline
1. Navega al directorio principal del proyecto:
```bash
cd machine-learning-operations/mlops
```

2. Valida la instalación de Python y Kedro:
```bash
python --version
kedro info
```

3. Para ejecutar el pipeline:
```bash
kedro run
```

4. Si deseas visualizar el pipeline en un navegador, ejecuta:
```bash
kedro viz
```
Luego, abre http://127.0.0.1:4141/?pid=default&expandAllPipelines=false en tu navegador.



## EQUIPO DE TRABAJO - GRUPO 9

El equipo está conformado por los siguientes miembros: 

* Orlando Marath Barraza Aguilar
* Juan Manuel Carballo Montaño
* Didier Omar Gamboa Angulo
* Jorge Luis Pedroza Rivera
* Emily Ann Sedán Herrera


La forma de interacción y coordinación es de manera digital, haciendo uso de grupos de Whatsapp, reuniones virtuales y empleando herramientas de trabajo colaborativo.
Los miembros del equipo residen en diferentes estados de México y algunos en Perú. Además, trabajan en diferentes sectores como consultoría y aerolíneas y cuentan con diferentes skills en tecnologías como Java, Go, Python y Oracle.
