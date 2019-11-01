import configparser
from pathlib import Path


def get_config():
    config_file = str(Path(__file__).parent.parent) + "/resources/config.ini"
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_file)
    return config
