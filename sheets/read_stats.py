# -*- coding: utf-8 -*-

"""
read_stats.py - Allows reading of key archive stats from the sheet
                (designed around Ruthalas's regular stat posts)
"""

# Libs
from sheets.auth import stats_wks


class Stats:
    def __init__(self):
        one_backup_channels = int(stats_wks.get_value('O2').replace(',', ''))
        duplicate_backup_channels = int(stats_wks.get_value('P2').replace(',', ''))

        # TODO: add languages stat
        self.channels = int(stats_wks.get_value('N2').replace(',', ''))
        self.contributors = int(stats_wks.get_value('S2').replace(',', ''))
        self.size_tb = float(stats_wks.get_value('X2').replace(',', ''))
        self.videos = int(stats_wks.get_value('Y2').replace(',', ''))
        self.avg_size_gb = float(stats_wks.get_value('Z2').replace(',', ''))
        self.duplicate_channels_percentage = (duplicate_backup_channels / one_backup_channels) * 100
        self.languages = int(stats_wks.get_value('AB2').replace(',', ''))
