# C O N F I G
# O N F I G C
# N F I G C O
# F I G C O N
# I G C O N F
# G C O N F i
"""
Library for working with configuration files of the ".ini" type
"""

__version__ = "0.1"
__author__ = "DraksPlay"
__author_email__ = "draksplay@mail.ru"

from .checkers import (
check_suffix,
check_file
)
from .exceptions import (
    ConfigFileNotFound,
    ConfigInvalidSuffix
)

# The main library that parses data from a file
import configparser


class Config:

    """
    Class for working with the config
    """

    def __init__(self, filename):
        """
        Initializing and checking the file for correctness.
        :param filename: the path to the configuration file.
        """
        assert check_suffix(filename) == True, ConfigInvalidSuffix
        assert check_file(filename) == True, ConfigFileNotFound
        self.__config_file = configparser.ConfigParser()
        self.__config_file.read(filename)

    def get(self):
        """
        A method for getting and sorting information of all data from the config.
        :return: dictionary with data.
        """
        d = {}
        for section in self.__config_file.sections():
            if len(self.__config_file.options(section)) > 0:
                d[section] = {}
            else:
                continue
            for option in self.__config_file.options(section):
                d[section][option] = self.__config_file[section][option]
        return d

    def __str__(self):
        """
        Output of a word with data in a string type.
        :return: str with data.
        """
        return str(self.get())