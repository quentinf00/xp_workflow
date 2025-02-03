import hydra_zen
from pathlib import Path

from omegaconf import OmegaConf
from xp_workflow.configure import configure, deps, outs
import {{cookiecutter.project_name}}

store = hydra_zen.ZenStore()

"""
Example pipeline
from test_project.stages import toto, tata # Two functions


# artefacts -> files produced by each function
toto_out = 'toto.txt'
tata_out = 'tata.txt'

# define first function arguments
toto_store = store(group='toto')

# specify the function outputs with the outs helper function
toto_store(toto, out_path=outs(toto_out), a=3, name='a3')
toto_store(toto, out_path=outs(toto_out), a=2, name='a4')

# define first function arguments
tata_store = store(group='tata')

for _, name in store['toto']:
    # specify the function dependencies with the deps helper function
    dep_outs = dict(
        in_path=deps(toto_out, 'toto', name), 
        out_path=outs(tata_out)
    )
    tata_store(tata, name=f'{name}_b1', b=4, **dep_outs)
    tata_store(tata, name=f'{name}_b2', b=2, **dep_outs)


# compose the configurations in artifacts folder and define the execution dag dvc.yaml
configure(store, ['toto', 'tata'])
"""

if __name__ == '__main__':
    stages = []

    for stage in stages:
        print(f'Stage {stage}:')
        for _, name in store[stage]:
            print(f'\t  Config: {name}')
    
    configure(store, stages)
