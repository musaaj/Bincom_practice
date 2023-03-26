#!/bin/python3
"""
This program reads a text file containing full name
of a person and prints it out
"""
from typing import List


def read_text_file(filename: str) -> str:
    """read a unicode text file return the
    content as string. Tested on Ubuntu 20.02.04 only

    Args:
        filename: str: the file must reside in the same
        location as this file

    Return: str: with all line break striped
    """
    with open(filename, 'r') as fp:
        try:
            return fp.read()
        except FileNotFoundError:
            return ''


if __name__ == '__main__':
    name: List[str] = read_text_file('name.txt').split()
    print(
        f"""
        First Name: {name[0]}
        Middle Name: {name[1]}
        Last Name: {name[2]}
        """
    )
