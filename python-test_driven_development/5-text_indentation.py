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
    i = 0
    while i < len(text):
        if text[i] == " ":
            continue
        if text[i] in s:
            print(text[i], end="")
            print("\n")
        else:
            print(text[i], end="")
        i += 1
