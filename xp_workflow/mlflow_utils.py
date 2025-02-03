import hydra_zen
import mlflow
from functools import wraps
from pathlib import Path
import os


def start_pipeline(run_name, project_name, dvc_root):
    mlflow.set_experiment(project_name)
    with mlflow.start_run(run_name=run_name):
        Path('.pipeline_id').write_text(mlflow.active_run().info.run_id)
        mlflow.log_artifact(Path(dvc_root) / "dvc.yaml")

def mlflow_run(wrapped_function, project_name=os.environ.get('MLFLOW_PROJECT_NAME')):
    @wraps(wrapped_function)
    def wrapper(*args, **kwargs):
        if Path('.pipeline_id').exists():
            os.environ['MLFLOW_RUN_ID'] = Path('.pipeline_id').read_text()
        mlflow.set_experiment(project_name)
        with mlflow.start_run():  # recover parent run thanks to MLFLOW_RUN_ID env variable
            with mlflow.start_run(run_name=os.environ.get('DVC_STAGE', wrapped_function.__name__), nested=True):  # start child run
                return wrapped_function(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    hydra_zen.store(start_pipeline)
    hydra_zen.store.add_to_hydra_store()
    hydra_zen.zen(start_pipeline).hydra_main(config_name='start_pipeline', version_base="1.3")

