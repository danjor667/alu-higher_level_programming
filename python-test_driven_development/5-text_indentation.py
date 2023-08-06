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
    for word in text.split():
        if word[-1] in s:
            print(word)
        print(word + " ", end="")
