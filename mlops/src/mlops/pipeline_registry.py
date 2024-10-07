"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from mlops.src.mlops.pipelines.ML import pipeline as ML_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines() # Esto creo que detecta automaticamente todos los pipeliens
    pipelines["ML"] = ML_pipeline.create_pipeline() # Aca se registra el pipeline
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
