from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular
from .nodes import calculate_correlations, calculate_stats, calculate_boxplots, compare_r2_metric


def create_pipeline(**kwargs) -> Pipeline:
    base_nodes = [
        node(
            func=calculate_correlations,
            inputs=["csv_energy_efficiency"],
            outputs="correlations_plot_energy_efficiency",
            name="calculate_correlations_node"
        ),
        
        node(
            func=calculate_stats,
            inputs=["csv_energy_efficiency"],
            outputs="stats_energy_efficiency",
            name="calc_stats_node"
        ),
        
        node(
            func=calculate_boxplots,
            inputs=["csv_energy_efficiency"],
            outputs="boxplot_energy_efficiency",
            name="calculate_boxplots_node"
        )
    ]
    
    _nodes = []
    hc = ['heating', 'cooling']
    
    for n in hc:
        _nodes.append(
            node(
                func=compare_r2_metric,
                inputs=[f"{n}.linear-regression_r2_score", f"{n}.random-forest_r2_score", f"{n}.xgboost_r2_score"],
                outputs=f"boxplot_models_{n}_energy_efficiency",
                name=f"compare_r2_metric_{n}_node"
            )
        )
        
    in1 = {f"{p}.linear-regression_r2_score": f"model_development.{p}.linear-regression_r2_score" for p in hc }
    in2 = {f"{p}.random-forest_r2_score": f"model_development.{p}.random-forest_r2_score" for p in hc}
    in3 = {f"{p}.xgboost_r2_score": f"model_development.{p}.xgboost_r2_score" for p in hc}
    in4 = {"csv_energy_efficiency": "data_processing.csv_renamed_energy_efficiency"}
    in1.update(in2)
    in1.update(in3)
    in1.update(in4)
    
    pipe = pipeline_modular(
        pipe=base_nodes + _nodes,
        inputs=in1,
        namespace="data_visualization"
    )
    
    return pipe
