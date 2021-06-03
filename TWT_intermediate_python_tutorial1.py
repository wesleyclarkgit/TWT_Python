# Optional Parameters Tutorial #1
# Create a function for example purposes
def func(x=1):
    return x ** 2


# here's what happens with 1 parameter
call = func(5)
print(call)

# here's what happens with two parameters


def func(word, freq):
    print(word*freq)


call = func('wes', 5)

# if we give it 2 parameters, but only invoke one, it still works, and only the parameter invoked passes


def func2(word, freq=2):
    print(word*freq)


call = func2(10)


def func3(word, add=5, freq=1):
    print(word*(freq+add))

# the order of arguments is important, like case sensitivity, in Python.
# in order to get a value for 'frequency' we have to input a value for 'add' because Python will
# interpret our intended value for frequency as the value for add if only 2 values are present(they
# go in logical order)


call = func3('hello')


# here's an example where we use a class to put it all together.
# notice how optional parameters can be used inside of methods, since methods are really just functions that
# apply to classes

class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." % (self.make, self.model, self.year, self.condition, self.kms)
        else:
            print("This car is a %s %s from %s." %
                  (self.make, self.model, self.year))

whip=car('Ford', 'Fusion', 2012)
whip.display(True)

# long story short, optional parameters can be especially helpful when using classes.
# in this example we changed the condition to New and kms to 0 because we assumed that the
# car would have 0 kms if it is new, and that it is new.
