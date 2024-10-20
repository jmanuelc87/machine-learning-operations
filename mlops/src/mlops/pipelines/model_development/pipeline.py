from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import model_dict, train_and_evaluate_model, selection_best_params


def create_pipeline(**kwargs) -> Pipeline:
    nodes = []

    for m in model_dict.keys():        
        nodes.append(
            node(
                func=lambda X, y, params, m=m: train_and_evaluate_model(X, y, m, params),
                inputs=["csv_train_energy_efficiency", "csv_target_energy_efficiency", "params:models"],
                outputs=f"{m}_r2_score",
                name=f"train_and_evaluate_{m}")
        )

    nodes.append(
        node(
            func=selection_best_params,
            inputs=["csv_train_energy_efficiency", "csv_target_energy_efficiency", "params:selector"],
            outputs="selection_best_model",
            name="selection_best_params_node"
        )
    )

    _pipes = []

    hc = ['heating', 'cooling']

    for p in hc:
        __pipe = pipeline_modular(
            pipe=nodes,
            inputs={
                "csv_train_energy_efficiency": f"{p}.csv_energy_efficiency_train",
                "csv_target_energy_efficiency": f"{p}.csv_target_energy_efficiency_train"
            },
            namespace=p
        )

        _pipes.append(__pipe)

    in2 = {f"{p}.csv_energy_efficiency_train": f"data_science.{p}.csv_energy_efficiency_train" for p in hc }
    in1 = {f"{p}.csv_target_energy_efficiency_train": f"data_science.{p}.csv_target_energy_efficiency_train" for p in hc}
    in1.update(in2)

    return pipeline_modular(
        pipe=_pipes,
        inputs=in1,
        namespace="model_development"
    )