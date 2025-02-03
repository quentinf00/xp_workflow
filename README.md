# XP Workflow

## Three tools:

### DVC:
    version and distribute shared / reusable dataset

### MLFlow:
    track experiments/ generated artefacts
    register and distribute models

### Hydra(-Zen)
    Manage xp configurations

## Prerequisite
### Pixi
https://pixi.sh/latest/#installation

### Cookiecutter

```pixi global install cookiecutter```

## Usage
###Import template with cookiecutter
`cookiecutter https://github.com/quentinf00/xp_workflow.git project_name=my_project`

Init project
```
cd project
git init
dvc init
dvc config  core.analytics false
```


Write processing functions in `my_project `

Detail processing configurations in `configure.py`

run pipeline with `NAME=my_xp pixi run pipeline`


