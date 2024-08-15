import os
import logging

import pytest


ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
TESTS_LOGGER = logging.getLogger('[T]')
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = pytest.fixture(scope='session')(lambda: TESTS_LOGGER)


def pytest_sessionstart(session):  # pylint: disable=unused-argument
    logging.basicConfig(level=logging.INFO)
    TESTS_LOGGER.setLevel(logging.INFO)

    TESTS_LOGGER.propagate = False
    TESTS_LOGGER.handlers = []
    tests_formatter = logging.Formatter(DEFAULT_LOG_FORMAT, datefmt='%H:%M:%S')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(tests_formatter)
    TESTS_LOGGER.addHandler(console_handler)


def get_script(script_name: str) -> str:
    if not script_name.endswith('.py'):
        TESTS_LOGGER.error(f'Invalid script name: {script_name}')
        return ''
    script_path = os.path.join(ASSETS_DIR, script_name)
    with open(script_path, encoding='utf-8') as script_file:
        return script_file.read()
