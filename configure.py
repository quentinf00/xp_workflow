import hydra_zen
from pathlib import Path

from omegaconf import OmegaConf
import scratch
from xp_workflow.configure import configure, deps, outs
from test_project.stages import toto, tata

store = hydra_zen.ZenStore()

toto_store = store(group='toto')

# artefacts
toto_out = 'toto.txt'
tata_out = 'tata.txt'

toto_store(toto, out_path=outs(toto_out), a=3, name='a3')
toto_store(toto, out_path=outs(toto_out), a=2, name='a4')

tata_store = store(group='tata')

for _, name in store['toto']:
    dep_outs = dict(
        in_path=deps(toto_out, 'toto', name), 
        out_path=outs(tata_out)
    )
    tata_store(tata, name=f'{name}_b1', b=4, **dep_outs)
    tata_store(tata, name=f'{name}_b2', b=2, **dep_outs)

if __name__ == '__main__':
    stages = ['toto', 'tata']

    for stage in stages:
        print(f'Stage {stage}:')
        for _, name in store[stage]:
            print(f'\t  Config: {name}')
    configure(store, stages)

