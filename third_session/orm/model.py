from fields import _SQLTypes, INTEGER, STRING, TEXT
from typing import ClassVar


class Model:
    def __init__(self, *args, **kwargs):
        if not hasattr(self, '_table'):
            self._table = self.__class__.__name__.lower()
        for key, val in kwargs.items():
            setattr(self, key, val)

class Users(Model):
    _table = 'users_table'
