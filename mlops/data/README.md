# Estructura de la Carpeta de Datos

La carpeta `data` está organizada en diferentes subcarpetas que representan las etapas del ciclo de vida de los datos dentro del pipeline de Machine Learning. A continuación se describe cada subcarpeta y su propósito:

## 01_raw
Contiene los datos en su formato original, sin ninguna modificación o procesamiento. Esta carpeta debe incluir los datos tal y como se reciben de la fuente, permitiendo una referencia a los datos sin procesar en caso de necesidad de auditoría o validación.

## 02_intermediate
Almacena los datos que han pasado por un preprocesamiento inicial o transformaciones menores. En esta etapa, los datos pueden haber sido limpiados o filtrados, pero aún no están listos para ser utilizados directamente en el modelo de Machine Learning.

## 03_primary
Contiene los datos que han pasado por una fase más avanzada de preparación y están en un formato estándar que puede utilizarse para generar características específicas o entrenar modelos. Estos datos pueden considerarse una versión refinada de los datos intermedios.

## 04_feature
Aquí se encuentran los datos transformados en características (features) finales. Estas características han sido generadas, seleccionadas y escaladas en base a los requerimientos del modelo de Machine Learning. En esta etapa, los datos están listos para ser utilizados en el entrenamiento o evaluación de modelos.

## 05_model_input
Contiene los datos finales que se usarán directamente como entrada para los modelos de Machine Learning. Estos datos incluyen las características definitivas y están organizados de acuerdo con los requisitos específicos del modelo.

## 06_models
Esta carpeta almacena los modelos de Machine Learning entrenados. Los archivos aquí pueden incluir modelos guardados en distintos formatos (como `.pkl`, `.h5`, etc.), listos para su despliegue o evaluación adicional.

## 07_model_output
Guarda los resultados generados por los modelos, como predicciones y métricas de rendimiento. Esta carpeta permite analizar el rendimiento del modelo y comparar resultados en distintas versiones o etapas de desarrollo.

## 08_reporting
Contiene los informes y visualizaciones generados a partir de los datos y los resultados del modelo. Estos informes están diseñados para proporcionar información relevante a los stakeholders, mostrando métricas clave y otros análisis visuales.


Esta estructura permite un flujo de datos organizado y asegura que cada etapa del proceso de Machine Learning esté documentada y sea reproducible. 
