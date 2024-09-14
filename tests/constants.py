import os
import logging

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
TESTS_LOGGER = logging.getLogger('[T]')
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
