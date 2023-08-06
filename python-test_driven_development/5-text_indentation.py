#!/usr/bin/python3
"""
doc
"""


def text_indentation(text):
    """
    doc
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = [".", "?", ":"]
    for letter in text:
        if letter in s:
            print(letter)
            print("\n")
        else:
            print(letter, end="")
