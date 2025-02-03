# XP Workflow

## Three tools:

### DVC:
    version and distribute shared / reusable dataset

### MLFlow:
    track experiments/ generated artefacts
    register and distribute models

### Hydra(-Zen)
    Manage xp configurations



## Pipeline:
listing --- extract-features --> data.csv --- prepro-<...>-datasets ---> <...>-ds
listing --- split ---> <...>.split.txt

<train/val)-dses --- train ---> model.ckpt

test-ds, model.ckpt --- eval ---> pred.csv

pred.csv --- diag ---> diag


tracked by dvc:
    - listings, splits, data.csv, train dataset, preds

logged in mlflow:
    - model.ckpt,  diags



## Target workflow

### Dev
- write configurable function
- write composable config
    - define deps and outputs
- pixi tasks:
    - dump dvc pipeline
    - run dvc pipeline


### Run
- start parent run
- log dvc.yaml
- set env mlflow run id
- run dvc stages
    - log .hydra dir


## Next steps:

- test mlflow integration
- organize configs
- better management of path (dependency path frmo previous stage outputs)
- apply to real use case
- (think about packaging)


