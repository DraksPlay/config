

class ConfigException(Exception):

    def __init__(self, log):
        raise log

class ConfigFileNotFound(ConfigException):
    """Configuration file was not found! Check the file path."""

class ConfigInvalidSuffix(ConfigException):
    """The suffix file must be of type ".ini"."""
