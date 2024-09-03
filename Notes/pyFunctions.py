# Built-in Functions(Must learn)
# The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.
# Link : https://docs.python.org/3/library/functions.html


# 1. map(function, iterable, *iterables)
# Return an iterator that applies function to every item of iterable, yielding the results.
# If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
# With multiple iterables, the iterator stops when the shortest iterable is exhausted.

#example;
def myfunc(a,b):
  return len(a+b)
x = map(myfunc, ('apple', 'banana', 'cherry'), ['11', '2'])
print(x)
print(list(x))



