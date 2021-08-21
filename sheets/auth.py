# -*- coding: utf-8 -*-

"""
auth.py - Creates an authenticated pygsheets object
"""

# Libs
import pygsheets
import pathlib

from config import config   # import config

# Grab the service account auth file location from the config
SA_auth_file = pathlib.Path(config['auth_file'])

# Create the pygsheets obj
client = pygsheets.authorize(service_file=SA_auth_file)
spreadsheet = client.open(config['spreadsheet_name'])
tracker_wks = spreadsheet.worksheet_by_title(config['tracker_worksheet_name'])
requests_wks = spreadsheet.worksheet_by_title(config['requests_worksheet_name'])
stats_wks = spreadsheet.worksheet_by_title(config['stats_worksheet_name'])
