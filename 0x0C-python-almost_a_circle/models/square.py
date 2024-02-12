#!/usr/bin/python3
"""
Module containing the Square class

The Square class inherits from Rectangle and contains:
- Initialization of superclass' id, width (as size), height (as size), x, y
- Public attribute: size
- String representation: [Square] (<id>) <x>/<y> - <size>
- Attribute update method
- Dictionary representation method
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines the Square class; inherits from Rectangle

    Inherited Attributes:
        id
        __weight        __height
        __x             __y

    Class Attributes:
        size

    Inherited Methods:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)

    Methods:
        __str__
        __init__(self, size, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        size(self)       size(self, value)
        to_dictionary(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        Updates attributes based on args or kwargs
        Args:
            If args: id, size, x, y
            If kwargs: id, size, x, y
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
