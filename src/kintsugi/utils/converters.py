import ast
import inspect
import types


def from_module_to_ast(module: types.ModuleType) -> ast.Module:
    return ast.parse(inspect.getsource(module))
