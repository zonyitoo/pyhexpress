# -*- coding: utf-8 -*-

from regexpvalue import *

class PyHexpress:

    def __init__(self):
        self.value = []

    def __repr__(self):
        return ''.join(str(ins) for ins in self.value)

    def __str__(self):
        return ''.join(str(ins) for ins in self.value)

    # static
    @staticmethod
    def words():
        return PyHexpress().including(r'\\w')

    # Starting
    def starting(self, val=''):
        self.value.append(RegExpStart(val))
        return self

    def begins(self, val=''):
        return self.starting(val)

    def begin(self, val=''):
        return self.starting(val)

    def start(self, val=''):
        return self.starting(val)

    # Has
    def has(self, val):
        self.value.append(RegExpIncluding(val))
        return self

    def including(self, val):
        return self.has(val)

    # Ending
    def end(self, val=''):
        self.value.append(RegExpEnding(val))
        return self

    # Find & capture
    def capture(self, *value):
        self.value.append(RegExpFind(*value))
        return self

    def find(self, *value):
        return self.capture(value)

    # Matching
    def matching(self, *value):
        self.value.append(RegExpMatching(*value))
        return self

    # others
    def maybe(self, value):
        self.value.append(RegExpEither(value).maybe())
        return self
