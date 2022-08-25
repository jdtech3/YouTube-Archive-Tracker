# -*- coding: utf-8 -*-

"""
crud_projects.py - Implements the CRUD operations for project list
"""

# Libs
from datetime import datetime
from sheets.auth import projects_wks
from typing import List


# Request object that wraps around the info
class Project:
    def __init__(self, name: str, contact: str, contributors: List[str], goals: str, links: List[str]):
        self.name = name
        self.contact = contact
        self.contributors = contributors
        self.goals = goals
        self.links = links


def create() -> Project:
    raise NotImplementedError(f'Project creation is not implemented yet.')


def read() -> List[Project]:
    projects = []
    for row_raw in projects_wks.get_all_values(include_tailing_empty=True, include_tailing_empty_rows=False)[1:]:
        row = [value if value != '' else None for value in row_raw]

        # Preprocess comma-separated values into a List
        contributors = row[2].split(',') if row[2] is not None else None
        links = row[4].split(',') if row[2] is not None else None

        proj_obj = Project(
            name=row[0],
            contact=row[1],
            contributors=contributors,
            goals=row[3],
            links=links,
        )
        projects.append(proj_obj)

    return projects
