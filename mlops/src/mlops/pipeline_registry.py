"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines


#### BORRAR .... 
# src/mlops/pipeline_registry.py

#from typing import Dict
#from kedro.pipeline import Pipeline
#from mlops.pipelines.EDA import create_pipeline as create_eda_pipeline

#def register_pipelines() -> Dict[str, Pipeline]:
 #   eda_pipeline = create_eda_pipeline()
  #  pipelines = {
   #     "EDA": eda_pipeline,
    #    "__default__": eda_pipeline,
    #}
    #return pipelines
