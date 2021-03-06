#Homework 04 - CS2021
 
def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).
 
    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    while(s != Link.empty and s.rest!=Link.empty):
        s.rest = s.rest.rest
        s=s.rest
 
 
def has_cycle(s):
    """Return whether Link s contains a cycle.
 
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    """
    "*** YOUR CODE HERE ***"
    new_set = set()
    while s is not Link.empty:
        if s in new_set:
            return True
        else:
            new_set.add(s)
            s = s.rest
    return False
 
def has_cycle_constant(s):
    """Return whether Link s contains a cycle.
 
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if s == Link.empty:
        return False
    else:
      l, g = s, s.rest
      while g != Link.empty:
          if g.rest == Link.empty:
              return False
          elif g == l or g.rest == l:
              return True
          else:
              l, g = l.rest, g.rest.rest
      return False
 
##############################
# Linked List implementation #
##############################
 
class Link:
 
    empty = ()
 
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
 
    def __len__(self):
        return 1 + len(self.rest)
 
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
 
    def __contains__(self, value):
        "*** YOUR CODE HERE ***"
        while self != Link.empty:
            if self.first == value:
                return True
        else:
            self = self.rest
            return False
    def __iadd__(self, other):
        "*** YOUR CODE HERE ***"
        self.repr+=other.repr
        return self
 
 
 
class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.
 
    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> list(s)
    [5, 25, 10]
 
    >>> m = ScaleIterator(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        "*** YOUR CODE HERE ***"
        self.num = iter(s)
        self.k = k
        
 
    def __iter__(self):
        return self
 
    def __next__(self):
        "*** YOUR CODE HERE ***"
        next_element = next(self.num)
        if next_element:
            return next_element * self.k
        else:
            raise StopIteration
 
 
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.
 
    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]
 
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for elem in s:
        yield elem * k
 
 
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.
 
    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"
    while True:
        yield min(e0, e1)
        if e0 < e1:
            e0 = next(i0)
        elif e1 < e0:
            e1 = next(i1)
        else:
            e0, e1 = next(i0), next(i1)
 
 
def make_s():
    """A generator function that yields all positive integers with only factors
    2, 3, and 5.
 
    >>> s = make_s()
    >>> type(s)
    <class 'generator'>
    >>> [next(s) for _ in range(20)]
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    """
    "*** YOUR CODE HERE ***"
    yield 1
    factors = merge(merge(scale(make_s(),2), scale(make_s(),3)),scale(make_s(),5))
    for i in factors:
        yield i
    
    
 
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.
 
    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1
 
 
def _test():
    import doctest
    doctest.testmod()
 
if __name__ == "__main__":
    _test()
