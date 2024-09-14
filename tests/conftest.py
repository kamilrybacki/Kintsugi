import logging


import pytest

from tests.constants import DEFAULT_LOG_FORMAT, TESTS_LOGGER


logger = pytest.fixture(scope='session')(lambda: TESTS_LOGGER)


def pytest_sessionstart(session: pytest.Session):  # pylint: disable=unused-argument
    logging.basicConfig(level=logging.INFO)
    TESTS_LOGGER.setLevel(logging.INFO)

    TESTS_LOGGER.propagate = False
    TESTS_LOGGER.handlers = []
    tests_formatter = logging.Formatter(DEFAULT_LOG_FORMAT, datefmt='%H:%M:%S')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(tests_formatter)
    TESTS_LOGGER.addHandler(console_handler)
