"""
config.api
~~~~~~~~~~~~

This module implements the work with config.

:copyright: (c) 2022 by DraksPlay.
"""

from .checkers import checker
from .exceptions import (
    ConfigFileNotFound,
    ConfigInvalidSuffix
)
import configparser

def get(filename):
    if checker(filename):
        config_file = configparser.ConfigParser()
        config_file.read(filename)
        return config_file
    else:
        raise ConfigInvalidSuffix
