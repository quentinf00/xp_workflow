from pathlib import Path
from omegaconf import OmegaConf
import hydra_zen
import hydra



def outs(s):
    return '${outs:${hydra:runtime.output_dir}/'+s+'}'

def stage_dir(stage, name):
    return f'artifacts/{stage}/{name}'

def configs_dir(stage):
    return f'artifacts/{stage}'


def deps(s, input_stage=None, input_name=None, stage_dir=stage_dir):
    if input_stage is not None:
        if input_name is None: raise Exception('No Input name specified')
        base_dir = stage_dir(input_stage, input_name) +'/'
    else:
        base_dir = ''
    return '${deps:' + base_dir + s +'}'

def configure(store, stage_groups, stage_dir=stage_dir, configs_dir=configs_dir):
    dvc_stages = dict()
    store.add_to_hydra_store(overwrite_ok=True)
    hydra.initialize(version_base="1.3")

    for stage in stage_groups:
        cfg_dir = Path(configs_dir(stage))
        cfg_dir.mkdir(exist_ok=True, parents=True)
        for _, name in store[stage]:
            cfg = hydra.compose(overrides=[f'+{stage}={name}'])

            (cfg_dir / f'{name}.yaml').write_text(hydra_zen.to_yaml(cfg))

            outs = []
            deps = []
            OmegaConf.register_new_resolver('outs', lambda k: outs.append(k) or k, replace=True)
            OmegaConf.register_new_resolver('deps', lambda k: deps.append(k) or k, replace=True)
            OmegaConf.register_new_resolver('hydra', lambda k: OmegaConf.select(OmegaConf.from_dotlist([f'runtime.output_dir={stage_dir(stage, name)}']), k), replace=True)
            OmegaConf.resolve(cfg)

            dvc_stages[f'{stage}/{name}'] = dict(
                cmd=( f'python -m xp_workflow.run '
                    f'-cd {configs_dir(stage)} -cn {name} '
                    f'hydra.run.dir={stage_dir(stage, name)}'),
                outs=outs,
                deps=deps,
                params=[{f'{configs_dir(stage)}/{name}.yaml': None}]
            )

    Path('dvc.yaml').write_text(
        hydra_zen.to_yaml(
            dict(stages=dvc_stages)
        )
    )
