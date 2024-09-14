import ast


def find_decorated_classes(script: ast.Module) -> list[ast.ClassDef]:
    """Find all classes that are decorated with a decorator."""
    return [
        node
        for node in ast.walk(script)
        if isinstance(node, ast.ClassDef) and node.decorator_list
    ]
