from fields import INTEGER, STRING,TEXT


class Field:
    field_type = ''
    null = 'NULL'
    unique = ''
    primary_key = ''
    foreign_key = ''
    auto_increment = ''

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        pass
