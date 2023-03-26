"""
This module implements basic python to PostgreSQL 
data types in form of functions
"""

class _SQLTypes:
    types = ''

    def __str__(self):
        return self.types

class INTEGER(_SQLTypes):
    types = 'INTEGER'

class STRING(_SQLTypes):
    types = 'VARCHAR'

    def __init__(self, char: int):
        self.type = f'{self.types}({char})'

class TEXT(_SQLTypes):
    types = 'TEXT'
