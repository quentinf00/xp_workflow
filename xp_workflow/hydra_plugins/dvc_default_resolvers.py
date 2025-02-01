from omegaconf import OmegaConf
OmegaConf.register_new_resolver('outs', lambda k: k, replace=True)
OmegaConf.register_new_resolver('deps', lambda k: k, replace=True)
