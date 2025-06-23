# Copyright 2023 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from pathlib import Path
import boto3
import mlrun

from src.heelm import heelm

def setup(
    project: mlrun.projects.MlrunProject,
) -> mlrun.projects.MlrunProject:
    
    
    project.set_source("git://github.com/daniels290813/jiggy.git#main", pull_at_runtime=False)
    pipeline_fn = project.set_function('untitled.py',name='hello', kind='job', image='mlrun/mlrun', handler='hello')
    pipeline_fn.save()
    project.set_function(f"db://{project.name}/hello", name="hello")
    project.save()
    pipe_image = project.build_image(base_image='mlrun/mlrun', set_as_default=False)
    print(pipe_image.outputs)
    project.set_workflow("my_workflow", "pipeline.py", embed=True, image=pipe_image.outputs['image'])
    

    # Save and return the project:
    project.save()
    return project
