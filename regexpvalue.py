# -*- coding:utf-8 -*-

import re

class RegExpValue:
    
    def __init__(self, val=''):
        self.value = val
    
class RegExpStart(RegExpValue):

    def __repr__(self):
        return '^%s' % self.value

    def __str__(self):
        return '^%s' % self.value

class RegExpIncluding(RegExpValue):

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

class RegExpEnding(RegExpValue):

    def __repr__(self):
        return '%s$' % self.value
    
    def __str__(self):
        return '%s$' % self.value

class RegExpCopies(RegExpValue):

    def __init__(self, *r, **args):
        if (len(r) > 2):
            raise ValueError()
        RegExpValue(self, r if len(r) == 2 else (0, r[0]))
        self.minimal = args['minimal'] if args.has_key('minimal') else False

    def __repr__(self):
        return '{%d,%d}%s' % (self.value[0], self.value[1], '?' if self.minimal else '')

    def __str__(self):
        return '{%d,%d}%s' % (self.value[0], self.value[1], '?' if self.minimal else '')


class RegExpExcept(RegExpValue):

    def __repr__(self):
        return '^%s' % self.value

    def __str__(self):
        return '^%s' % self.value

class RegExpModifier(RegExpValue):

    def __init__(self, *val):
        RegExpValue.__init__(self, *val)
        self.operator = ''
    
    def any(self, minimal=False):
        self.operator = '*%s' % '?' if minimal else ''
        return self

    def noMoreThanOne(self, minimal=False):
        self.operator = '?%s' % '?' if minimal else ''
        return self

    def maybe(self):
        return self.noMoreThanOne()

    def hasOrNot(self):
        return self.noMoreThanOne()

    def atLeastOne(self, minimal=False):
        self.operator = '+%s' % '?' if minimal else ''
        return self


class RegExpEither(RegExpModifier):

    def __init__(self, *val, **args):
        RegExpModifier.__init__(self, val)
        self.delimiter = args['delimiter'] if args.has_key('delimiter') else '|'
        self.opens = args['open'] if args.has_key('open') else '(?:'
        self.close = args['close'] if args.has_key('close') else ')'

    def __repr__(self):
        return '%s%s%s%s' % (self.opens, self.delimiter.join(str(val) for val in self.value), self.close, self.operator)

    def __str__(self):
        return '%s%s%s%s' % (self.opens, self.delimiter.join(str(val) for val in self.value), self.close, self.operator)

class RegExpRange(RegExpModifier):

    def __init__(self, first, last, delimiter='-'):
        RegExpModifier.__init__(self, (first, last))
        self.delimiter = delimiter

    def __repr__(self):
        return '%s%s%s%s' % (self.value[0], self.delimiter, self.value[1], self.operator)

    def __str__(self):
        return '%s%s%s%s' % (self.value[0], self.delimiter, self.value[1], self.operator)

class RegExpFind(RegExpValue):

    def __init__(self, *value):
        RegExpValue.__init__(self, value)
        self.opens = '('
        self.close = ')'

    def __repr__(self):
        return '%s%s%s' % (self.opens, ''.join(str(val) for val in self.value), self.close)

    def __str__(self):
        return '%s%s%s' % (self.opens, ''.join(str(val) for val in self.value), self.close)

class RegExpMatching(RegExpValue):

    def __init__(self, *value):
        RegExpValue.__init__(self, value)
        self.opens = '['
        self.close = ']'

    def __repr__(self):
        return '%s%s%s' % (self.opens, ''.join(str(val) for val in self.value), self.close)

    def __str__(self):
        return '%s%s%s' % (self.opens, ''.join(str(val) for val in self.value), self.close)
