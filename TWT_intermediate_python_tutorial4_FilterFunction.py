# Filter Function

def add7(x):
    return x + 7


def isOdd(x):
    return x % 2 != 0


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter is like map, it takes a function and an iterable list
b = list(filter(isOdd, a))

print(a)
print(b)

# use map function to apply new list b, and add 7 to each item in the list
c = list(map(add7, b))
print(c)
