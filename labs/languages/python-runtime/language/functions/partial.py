from functools import partial


# A normal function
def f(a, b, c, x):
    return a + b + c + x


# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
print(g(5))
