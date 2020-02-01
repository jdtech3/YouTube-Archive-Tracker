# -*- coding: utf-8 -*-

"""
crud.py - Implements the CRUD operations as well as the info
          filling for the autofilled fields
"""

# Libs
from datetime import datetime
from sheets.auth import requests_wks
from typing import List


# Request object that wraps around the info
class Request:
    def __init__(self, **kwargs):
        _fields = [
            'name',                 # str
            'link',                 # str
            'requester',            # str
            'reason',
            'filled',               # bool
            'filled_by',            # List[str]
        ]

        for arg in kwargs.keys():
            if arg not in _fields:
                raise AttributeError(f'Invalid keyword argument received: {arg}')

        # Turn all empty str into None
        kwargs = {key: value if value != '' else None for key, value in kwargs.items()}

        self.name = kwargs['name']
        self.link = kwargs['link']
        self.requester = kwargs['requester']
        self.reason = kwargs['reason']

        # Process filled: turn 'Yes', 'No' to True, False
        if kwargs['filled'] == 'Yes':
            self.filled = True
        else:
            self.filled = False

        # filled_by should be a list of Discord usernames
        self.filled_by = kwargs['filled_by']


def create() -> Request:
    raise NotImplementedError(f'Request creation is not implemented yet.')


def read() -> List[Request]:
    requests = []
    for record in requests_wks.get_all_records():
        # Preprocess filled_by (comma-separated list of names) into a List
        filled_by_str = record['Filled By\n(auto filled by checking channels)']
        filled_by = filled_by_str.split(',')

        req_obj = Request(
            name=record['Channel Name'],
            link=record['Channel URL'],
            requester=record['Requester'],
            reason=record['Reason/Notes'],
            filled=record['Filled?\n(auto checks channels)'],
            filled_by=filled_by
        )
        requests.append(req_obj)

    return requests
