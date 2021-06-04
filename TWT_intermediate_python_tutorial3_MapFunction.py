# map function

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x**x


newList = []
for x in li:
    newList.append(func(x))

print(newList)

# we could do this with map

# map function takes a function and a list, and applies the function to every element in the list
# careful not to use list in the name.  I had it as list = [1,2,3,4,5,6,7,8,9,10], and code errored out, presumably because list is a defined keywork
print(list(map(func, li)))
# this is super useful because it's a shortcut to the for loop, and we can apply multiple functions if we want

# instead of map you can also use list comprehension
print([func(x) for x in li])
# this says we are going to take func(x) and do it for every value x in the list
# we could also add an expression

print([func(x) for x in li if x % 2 == 0])
