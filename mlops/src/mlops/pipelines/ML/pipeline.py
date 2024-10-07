"""
This is a boilerplate pipeline 'ML'
generated using Kedro 0.19.8
"""

#from kedro.pipeline import Pipeline, pipeline
#from kedro.pipeline import node
#from .nodes import boxplot # Importante, vease como estoy importando como modulo, las funciones definidas en el archivos nodes.py

# Declarar los nodos por separados
#boxplot_node  = node(func=boxplot,
 #                    inputs=["raw_data"], # Importante, estos inputs hacen referencia al nombre dado en el catalogo a ese set de datos
  #                   outputs=None, # Se establece en None porque los resultados se guardan directamente en archivos y no se devuelven a Kedro.
   #                  name="boxplot_node")
#def create_pipeline(**kwargs) -> Pipeline:

 #   data_pipeline = [boxplot_node,] # aca puedes ir más nodos

  #  return pipeline(data_pipeline) # Integramos el pipeline de nodos


# src/<your_project_name>/pipelines/eda/pipeline.py

from kedro.pipeline import Pipeline, node
from .nodes import boxplot_node

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=boxplot_node,
                inputs="raw_data",
                outputs=None,
                name="boxplot_node",
            ),
        ]
    )
