from kedro.pipeline import Pipeline, pipeline, node
from .nodes import calculate_correlations, calculate_stats, calculate_boxplots


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=calculate_correlations,
            inputs=["csv_renamed_energy_efficiency"],
            outputs=["correlations_energy_efficiency", "correlations_plot_energy_efficiency"],
            name="calculate_correlations_node"
        ),
        
        node(
            func=calculate_stats,
            inputs=["csv_renamed_energy_efficiency"],
            outputs="stats_energy_efficiency",
            name="calc_stats_node"
        ),
        
        node(
            func=calculate_boxplots,
            inputs=["csv_renamed_energy_efficiency"],
            outputs="boxplot_energy_efficiency",
            name="calculate_boxplots_node"
        ),
    ])
