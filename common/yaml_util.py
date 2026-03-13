import pytest
import yaml
from pathlib import Path
path =Path(__file__).parent.parent.resolve()

def ddt(yaml_path, **kwargs):
    file =open(f"{path}\\data\\{yaml_path}",'r',encoding='utf-8')
    data_list=yaml.safe_load(file)
    return pytest.mark.parametrize("data",data_list,**kwargs)


