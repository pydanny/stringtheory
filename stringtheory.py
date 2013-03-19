__author__ = 'Daniel Greenfeld'
__version__ = "0.1.0"

import math


class String(str):
    """ Adding critically unimportant functionality to Python's str type """

    def len(self):
        return self.__len__()

    @property
    def length(self):
        return self.len()

    @property
    def size(self):
        return self.length

    @property
    def width(self):
        return self.length

    @property
    def height(self):
        return self.length

    @property
    def area(self):
        return self.height * self.width


class ConqueringString(String):
    """ Adding stupidly dangerous functionality to Python's str type """

    def __init__(self, text):
        super(ConqueringString, self).__init__(text)
        self._length = self.__len__()

    def __len__(self):
        try:
            return self._length
        except AttributeError:
            return super(ConqueringString, self).__len__()

    def len(self, value=None):
        if value is None:
            return self._length
        self._length = value

    @property
    def length(self):
        return self.len()

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def size(self):
        return self.length

    @size.setter
    def size(self, value):
        self.length = value

    @property
    def area(self):
        return self.height * self.width

    @area.setter
    def area(self, value):
        self.length = math.sqrt(value)

if __name__ == "__main__":
    s = ConqueringString("Hello, World!")
    print(s)
    print(s.length)
    s.length = 5
    print(s.length)
    print(s.area)
    s.area = 50
    print(s.area)
    print(len(s))
    print(s[5:10])  # slicing still works!
    print(s.upper())  # other methods still work!
