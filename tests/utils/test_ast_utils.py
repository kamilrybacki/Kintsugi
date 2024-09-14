import ast

from kintsugi.utils.ast import build_from_module, extract_classes_from_ast, extract_functions_from_ast
from tests.helpers import get_script


def test_conversion_from_module_to_ast():
    script = get_script('documented.py')
    ast_module = build_from_module(script)
    assert isinstance(ast_module, ast.Module)
    assert ast_module is not None
    assert ast_module.body is not None
    assert len(ast_module.body) > 0


def test_extracting_classes_from_module():
    script = get_script('documented.py')
    ast_module = build_from_module(script)
    classes = extract_classes_from_ast(ast_module)
    assert len(classes) == 2
    assert classes[0].name == 'DocumentedClass'
    assert classes[1].name == 'AnotherDocumentedClass'


def test_extracting_functions_from_module():
    script = get_script('documented.py')
    ast_module = build_from_module(script)
    functions = extract_functions_from_ast(ast_module)
    assert len(functions) == 1
    assert functions[0].name == 'documented_function'
