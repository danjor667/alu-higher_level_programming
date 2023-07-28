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
    data = ""
    with open(filename) as f:
        for line in f:
            data += line
            if search_string in line:
                data += new_string
    with open(filename, "w") as f:
            f.write(data)
