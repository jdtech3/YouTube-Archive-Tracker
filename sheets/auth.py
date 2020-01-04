# -*- coding: utf-8 -*-

"""
auth.py - Creates an authenticated pygsheets object
"""

# Libs
import pygsheets
import pathlib


# Grab the service account auth file location from the config
from config import config
SA_auth_file = pathlib.Path(config['auth_file'])

# Create the pygsheets obj
client = pygsheets.authorize(service_file=SA_auth_file)
spreadsheet = client.open(config['spreadsheet_name'])
tracker_wks = spreadsheet.worksheet_by_title(config['tracker_worksheet_name'])
