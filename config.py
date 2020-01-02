# -*- coding: utf-8 -*-

"""
config.py - Reads config
"""

# Libs
from configparser import ConfigParser


# Read the config
parser = ConfigParser()
parser.read('config.ini')

# Set config dict
config = {
    'bot_prefix': parser['Discord']['prefix'],
    'bot_token': parser['Discord']['token']
}
