#!/usr/bin/python3
"""
    a class Square
"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
        class Square
    """
    def __init__(self, size):
        """
        inisilising an obj
        """
        super().__init__(self, width, height)
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """
        calculating the size
        """
        return self.__width ** 2
