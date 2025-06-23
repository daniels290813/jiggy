

import mlrun
from kfp import dsl
from src.heelm import faa


@dsl.pipeline(
    name="hey",
    description="Dede",
)
def pipeline(vector_name="hey"):
    project=mlrun.get_current_project()  
    
    feature_selection_func = project.get_function("hello")
    feature_selection_run = project.run_function(
        feature_selection_func,
        name="hello")
