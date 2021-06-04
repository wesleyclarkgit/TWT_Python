# 6 Collections

import collections
from collections import Counter

# in python, there are containers - a data type or object.  The four main ones within Python built in are
# list, set, dict, tuple

# Counter introduces new containers
# Counter, deque, namedTuple(), orderedDict, defaultdict

c = Counter('gallad')
c = Counter(['a,', 'a',  'b', 'b',  'c,', 'c'])
print(c)
c = Counter({'a': 1, "b": 2})
print(c)
c = Counter(cats=4, dogs=7)
print(c)

# this creates counter objects.  it's its own thing.  works differently than a dictionary or list

print(c['cats'])
# one nice thing about the counter is if you use it on a value that doesn't exist, it won't error out like it will in a list

# one of the useful methods is for listing everything out

print(list(c.elements()))

print(c.most_common())
# it just has some interesting methods that can be super useful


d = ['a', 'b', 'c']
c.update(d)
print(c)

c.clear()
print(c)
