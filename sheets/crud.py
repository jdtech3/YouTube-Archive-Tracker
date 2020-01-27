# -*- coding: utf-8 -*-

"""
crud.py - Implements the CRUD operations as well as the info
          filling for the autofilled fields
"""

# Libs
from datetime import datetime
from sheets.auth import tracker_wks
from typing import List


# Channel object that wraps around the info
class Channel:
    def __init__(self, **kwargs):
        _fields = [
            '_id',                  # str
            'name',                 # str
            'link',                 # str
            'uploader',             # str
            'total_videos',         # int
            'total_videos_date',    # datetime.date
            'uploaded_videos',      # int
            'size_GB',              # float
            'last_update_date',     # datetime.date
            'status',               # str
            'description',          # str
            'notes',                # str
            'language',             # str
            'uploader_email'        # str
        ]

        for arg in kwargs.keys():
            if arg not in _fields:
                raise AttributeError(f'Invalid keyword argument received: {arg}')

        # Turn all empty str into None
        kwargs = {key: value if value != '' else None for key, value in kwargs.items()}

        # Do some questionable one-liners that ensure that None doesn't cause error
        self.id = kwargs['_id']
        self.name = kwargs['name']
        self.link = kwargs['link']
        self.uploader = kwargs['uploader']
        self.total_videos = int(kwargs['total_videos'])         if kwargs['total_videos'] else None
        self.total_videos_date = kwargs['total_videos_date']
        self.uploaded_videos = int(kwargs['uploaded_videos'])   if kwargs['uploaded_videos'] else None
        self.size_GB = float(kwargs['size_GB'])                 if kwargs['size_GB'] else None
        self.last_update_date = kwargs['last_update_date']
        self.status = kwargs['status']
        self.description = kwargs['description']
        self.notes = kwargs['notes']
        self.language = kwargs['language']
        self.uploader_email = kwargs['uploader_email']


def create(channel_id: str, context: str) -> Channel:
    # Contexts:
    #   - downloading
    #   - uploading

    if context == 'downloading':
        raise NotImplementedError(f'Context {context} is not implemented yet')

    elif context == 'uploading':
        raise NotImplementedError(f'Context {context} is not implemented yet')

    else:
        raise NotImplementedError(f'Context {context} is not implemented yet or was invalid.')


def read(channel_id: str) -> List[Channel]:
    channels = []
    for record in tracker_wks.find(channel_id):
        # Read from worksheet - note: pygsheets address are in (col, row) format
        row = record.row                                                                        # get row # of channel
        chan_data = tracker_wks.get_values(start=(row, 1), end=(row, 13), returnas='cell')[0]   # get list of pygsheets.Cell

        # Preprocessing of dates
        # total_videos_date_str = chan_data[4].note.replace('As of ', '')
        # total_videos_date = datetime.strptime(total_videos_date_str, '%Y-%m-%d').date()
        last_update_date_str = chan_data[7].value
        # Questionable 1-liner again...
        last_update_date = datetime.strptime(last_update_date_str, '%Y-%m-%d').date() if last_update_date_str != 'Unknown' else last_update_date_str
        # Set total_videos_date to last_update_date fow now
        total_videos_date = last_update_date

        chan_obj = Channel(
            _id=chan_data[0].value,
            name=chan_data[1].value,
            link=chan_data[2].value,
            uploader=chan_data[3].value,
            total_videos=chan_data[4].value,
            total_videos_date=total_videos_date,
            uploaded_videos=chan_data[5].value,
            size_GB=chan_data[6].value,
            last_update_date=last_update_date,
            status=chan_data[8].value,
            description=chan_data[9].value,
            notes=chan_data[10].value,
            language=chan_data[11].value,
            uploader_email=chan_data[12].value
        )
        channels.append(chan_obj)

    return channels


def update(channel_id: str, context: str) -> Channel:
    # Contexts:
    #   - uploading
    #   - done

    if context == 'uploading':
        raise NotImplementedError(f'Context {context} is not implemented yet')

    elif context == 'done':
        raise NotImplementedError(f'Context {context} is not implemented yet')

    else:
        raise NotImplementedError(f'Context {context} is not implemented yet or was invalid.')


def delete(channel_id: str) -> Channel:
    raise NotImplementedError('Delete operation is not implemented yet.')

