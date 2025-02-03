import mlflow
from pathlib import Path
import hydra_zen
from xp_workflow.mlflow_utils import mlflow_run

import logging

log = logging.getLogger(__name__)

@mlflow_run
def toto(out_path='toto_out.csv', a=1):
    log.info(out_path)
    mlflow.log_param('a',a)
    path_out = Path(out_path)
    path_out.parent.mkdir(parents=True, exist_ok=True)
    path_out.write_text(f'{a=}')

toto_config = hydra_zen.builds(toto, populate_full_signature=True)

@mlflow_run
def tata(
        in_path='???',
        out_path='tata_out.csv',
        b=1):
    mlflow.log_param('b',b)
    inp = Path(in_path).read_text()
    path_out = Path(out_path)
    path_out.parent.mkdir(parents=True, exist_ok=True)
    path_out.write_text(f'{b  *  inp=}')

tata_config = hydra_zen.builds(tata, populate_full_signature=True)
