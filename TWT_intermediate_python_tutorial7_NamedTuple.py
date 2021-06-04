# 7 Named Tuple

# Named tuples assign meaning to each position in a tuple and allow for more readable self-documenting code.  They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of positon indesx

# here's the syntax:  collections.napedtuple(typename, field_names[, verbose=False][, rename=False])

import collections
from collections import namedtuple


Point = namedtuple('Point', 'x y z')

newP = Point(3, 4, 5)
print(newP)

# this breaks up the object by space\
# methods for some reason require an underscore
