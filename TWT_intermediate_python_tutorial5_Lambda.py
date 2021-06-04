# Lambda Tutorial

# this is like an anonymous function.  doesn't take up much space in a function and is super useful


def func(x):
    return x + 5


print(func(2))

# instead of defining the function like above, we can do it in another way

# lambda syntax says 'okay, lambda, then the parameter(or multiple parameters), colon, whatever value you return
# it's used when you have one expression in your function


def func2(x): return x+5


print(func2(9))

# this becomes pretty useful with longer code bases

# let's try a new function with multiple parameters


def func3(x, y): return x+y


print(func3(5, 5))


# let's use it with the map and filter function
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = list(map(func, a))
# we could do this using lambda
newList2 = list(map(lambda x: x+5, a))
print(newList2)
# this saves us from having to create the function when we will only use it for one specific case

newList3 = list(filter(lambda x: x % 2 == 0, a))
print(newList3)
