#!/usr/bin/python3
"""classs Rectangle that defines a rectangle based on task 0"""


class Rectangle:
        """define a class rectangle"""

            def __init__(self, width=0, height=0):
                        """iniatializes w & h attributes with default value 0"""
                                self.width = width
                                        self.height = height

             @property
             def width(self):
                  """retrieves values of width"""
                   return self.__width

                                                                    @width.setter
                                                                        def width(self, value):
                                                                                    if not isinstance(value, int):
                                                                                                    raise TypeError("width must be an integer")
                                                                                                        if value < 0:
                                                                                                                        raise ValueError("width must be >= 0")
                                                                                                                            self.__width = value

                                                                                                                                @property
                                                                                                                                    def height(self):
                                                                                                                                                """retrive values of height"""
                                                                                                                                                        return self.__height

                                                                                                                                                        @height.setter
                                                                                                                                                            def height(self, value):
                                                                                                                                                                        if not isinstance(value, int):
                                                                                                                                                                                        raise TypeError("height must be an integer")
                                                                                                                                                                                            if value < 0:
                                                                                                                                                                                                            raise ValueError("height must be >= 0")
                                                                                                                                                                                                                self.__height = value
