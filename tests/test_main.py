from conftest import get_script


def test_finding_decorated_docstring(logger):
    script = get_script('documented.py')
    logger.info(f'Script: {script}')
