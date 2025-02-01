import mlflow
from pathlib import Path
import hydra_zen
from omegaconf import OmegaConf


def toto(out_path='${outs:${hydra:runtime.output_dir}/out.txt}', a=1):
    print(a)
    path_out = Path(out_path)
    path_out.parent.mkdir(parents=True, exist_ok=True)
    path_out.write_text(f'{a=}')

run_config = hydra_zen.builds(toto, populate_full_signature=True)




if __name__ == '__main__':
    hydra_zen.zen(toto).hydra_main(
        config_path=None,
        version_base="1.3"
    )
        

