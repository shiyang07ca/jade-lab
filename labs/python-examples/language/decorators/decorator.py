from functools import wraps


def doublewrap(f):
    """
    a decorator decorator, allowing the decorator to be used as:
    @decorator(with, arguments, and=kwargs)
    or
    @decorator
    """

    @wraps(f)
    def new_dec(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # actual decorated function
            return f(args[0])
        else:
            # decorator arguments
            return lambda realf: f(realf, *args, **kwargs)

    return new_dec


def test_doublewrap():
    @doublewrap
    def mult(f, factor=2):
        """multiply a function's return value"""

        @wraps(f)
        def wrap(*args, **kwargs):
            return factor * f(*args, **kwargs)

        return wrap

    # try normal
    @mult
    def f(x, y):
        return x + y

    # try args
    @mult(3)
    def f2(x, y):
        return x * y

    # try kwargs
    @mult(factor=5)
    def f3(x, y):
        return x - y

    @mult()
    def f4(x, y):
        return x * y

    assert f(2, 3) == 10
    assert f2(2, 5) == 30
    assert f3(8, 1) == 5 * 7
    assert f4(8, 1) == 16


if __name__ == "__main__":
    test_doublewrap()
