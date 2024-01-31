#!/usr/bin/python3
"""class Rectangle that defines a rectangle in task 1"""


class Rectangle:
    """ define a class"""

    def __init__(self, width=0, height=0):
        """initializes w && h attributes with default value 0"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrive value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
