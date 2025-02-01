from pathlib import Path
from omegaconf import OmegaConf
import hydra_zen
import re

def configure(stage_configs):
    dvc_stages = dict()
    for stage, configs in stage_configs.items():
        cfg_dir = Path(f'configs/{stage}')
        cfg_dir.mkdir(exist_ok=True, parents=True)
        for name, cfg in configs.items():
            (cfg_dir / f'{name}.yaml').write_text(hydra_zen.to_yaml(cfg))

            outs = []
            deps = []
            OmegaConf.register_new_resolver('outs', lambda k: outs.append(k) or k, replace=True)
            OmegaConf.register_new_resolver('deps', lambda k: deps.append(k) or k, replace=True)
            OmegaConf.register_new_resolver('hydra', lambda k: OmegaConf.select(OmegaConf.from_dotlist([f'runtime.output_dir=data/{stage}/{name}']), k), replace=True)
            OmegaConf.resolve(OmegaConf.create(cfg))
            module = re.sub(r'\.\w+$', '', cfg._target_)
            dvc_stages[f'{stage}/{name}'] = dict(
                # cmd=( f'python -m {module} '
                cmd=( f'python xp_workflow/run.py '
                    f'-cd configs/{stage} -cn {name} '
                    f'hydra.run.dir=data/{stage}/{name}'),
                outs=outs,
                deps=deps,
                params=[{f'configs/{stage}/{name}.yaml': None}]
            )

    Path('dvc.yaml').write_text(
        hydra_zen.to_yaml(
            dict(stages=dvc_stages)
        )
    )
