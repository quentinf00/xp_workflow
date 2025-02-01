import hydra_zen
from pathlib import Path

from omegaconf import OmegaConf
import scratch
import xp_workflow.configure

ALL_CONFIGS = dict()

# DVC_STAGES.update(scratch.dvc_config)

ALL_CONFIGS['toto']=dict(
    a1=scratch.run_config(a=1), 
    a2=scratch.run_config(a=2),
)


if __name__ == '__main__':
    xp_workflow.configure.configure(ALL_CONFIGS)

    ## Dump configs
