import ast
import pytest

from kintsugi.utils.ast import extract_classes_from_ast, extract_functions_from_ast, extract_module_docstring_from_ast, build_from_module


@pytest.mark.order("first")
def test_conversion_from_module_to_ast(test_module):
    test_ast = build_from_module(test_module)
    assert isinstance(test_ast, ast.Module)
    assert test_ast is not None
    assert test_ast.body is not None
    assert len(test_ast.body) > 0


@pytest.mark.order(after="test_conversion_from_module_to_ast")
def test_extracting_module_docstring_from_ast(test_ast):
    docstring = extract_module_docstring_from_ast(test_ast)
    assert docstring == 'This is a test module for Kintsugi tests'


@pytest.mark.order(after="test_conversion_from_module_to_ast")
def test_extracting_classes_from_module(test_ast):
    classes = extract_classes_from_ast(test_ast)
    assert len(classes) == 2
    assert classes[0].name == 'DocumentedClass'
    assert classes[1].name == 'AnotherDocumentedClass'


@pytest.mark.order(after="test_conversion_from_module_to_ast")
def test_extracting_functions_from_module(test_ast):
    functions = extract_functions_from_ast(test_ast)
    assert len(functions) == 1
    assert functions[0].name == 'documented_function'
