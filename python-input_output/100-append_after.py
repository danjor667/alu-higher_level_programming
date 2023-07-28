#!/usr/bin/python3
"""
defining a funct
append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
    add a str after a line
    containing a specifique character
    """
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)
    with open(filename, "w") as f:
        for i in range(len(lines)):
            f.write(lines[i])
