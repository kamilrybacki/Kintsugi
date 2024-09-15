import ast
import inspect
import types


def build_from_module(module: types.ModuleType) -> ast.Module:
    return ast.parse(inspect.getsource(module))


def extract_module_docstring_from_ast(ast_module: ast.Module):
    return ast.get_docstring(ast_module)


def extract_classes_from_ast(ast_module: ast.Module):
    return [node for node in ast_module.body if isinstance(node, ast.ClassDef)]


def extract_functions_from_ast(ast_module: ast.Module):
    return [node for node in ast_module.body if isinstance(node, ast.FunctionDef)]
