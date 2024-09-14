import ast

from kintsugi.utils.converters import from_module_to_ast
from tests.helpers import get_script


def test_conversion_from_module_to_ast():
    script = get_script('documented.py')
    ast_module = from_module_to_ast(script)
    assert isinstance(ast_module, ast.Module)
    assert ast_module is not None
    assert ast_module.body is not None
    assert len(ast_module.body) > 0
