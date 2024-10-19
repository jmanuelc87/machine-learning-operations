from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular
from .nodes import calculate_correlations, calculate_stats, calculate_boxplots


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
        ),
    ]
    
    return pipeline_modular(
        pipe=base_nodes,
        inputs={"csv_energy_efficiency": "data_processing.csv_renamed_energy_efficiency"},
        namespace="data_visualization"
    )
