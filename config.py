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
    'bot_token': parser['Discord']['token'],

    'auth_file': parser['Sheets']['auth_file'],
    'spreadsheet_name': parser['Sheets']['spreadsheet_name'],
    'tracker_worksheet_name': parser['Sheets']['tracker_worksheet_name'],
    'requests_worksheet_name': parser['Sheets']['requests_worksheet_name'],
    'stats_worksheet_name': parser['Sheets']['stats_worksheet_name']
}
