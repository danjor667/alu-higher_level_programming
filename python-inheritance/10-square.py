#!/usr/bin/python3
"""
    a class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class Square
    """
    def __init__(self, size):
        """
        inisilising an obj
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculating the size
        """
        return self.__width ** 2
