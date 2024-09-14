import importlib.util
import os
from types import ModuleType


from tests.constants import ASSETS_DIR


def get_script(script_name: str) -> ModuleType:
    if not script_name.endswith('.py'):
        raise ValueError('Script name should end with .py')
    script_path = os.path.join(ASSETS_DIR, script_name)
    if not os.path.exists(script_path):
        raise FileNotFoundError(f'Script {script_name} not found in {ASSETS_DIR}')
    asset_spec = importlib.util.spec_from_file_location('test_script', script_path)
    if asset_spec is None:
        raise ImportError(f'Could not load {script_name}')
    return importlib.util.module_from_spec(asset_spec)
