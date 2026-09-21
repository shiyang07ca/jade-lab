"""

通常，仅当需要控制低级别新实例的创建时，才会编写自定义实现。现在，如果您需要此方法的自定义实现，则应执行几个步骤：.__new__()

- 通过使用适当的参数进行调用来创建新实例。super().__new__()
- 根据您的特定需求自定义新实例。
- 返回新实例以继续实例化过程。

"""


class SomeClass:
    def __new__(cls, *args, **kwargs):
        # It’s important to note that object.__new__() itself only accepts
        # a single argument, the class to instantiate. If you call
        # object.__new__() with more arguments, then you get a TypeError:
        # super().__new__(cls, *args, **kwargs)
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        self.value = value


# Singleton class
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("I'm called")


from operator import itemgetter


def named_tuple_factory(type_name, *fields):
    num_fields = len(fields)

    class NamedTuple(tuple):
        __slots__ = ()

        def __new__(cls, *args):
            if len(args) != num_fields:
                raise TypeError(
                    f"{type_name} expected exactly {num_fields} arguments,"
                    f" got {len(args)}"
                )
            cls.__name__ = type_name
            for index, field in enumerate(fields):
                import ipdb

                ipdb.set_trace()
                setattr(cls, field, property(itemgetter(index)))
            return super().__new__(cls, args)

        def __repr__(self):
            return f"""{type_name}({", ".join(repr(arg) for arg in self)})"""

    return NamedTuple


class MyClass:
    class_var = 10

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def print_vars(self):
        print("Class variable:", MyClass.class_var)
        print("Instance variable:", self.instance_var)

    @classmethod
    def set_class_var(cls):
        cls.class_var = 100


def t_class_var():
    a = MyClass(5)
    b = MyClass(6)
    a.print_vars()
    b.print_vars()

    print("================================================================")

    a.instance_var = 8
    b.instance_var = 9
    a.print_vars()
    b.print_vars()

    print("================================================================")

    # a.class_var = 20
    # b.class_var = 40
    # a.print_vars()
    # b.print_vars()

    a.set_class_var()
    a.print_vars()
    b.print_vars()

    print("================================================================")

    MyClass.class_var = 30
    a.print_vars()
    b.print_vars()


def t_class1():
    sc = SomeClass(22)
    # print(sc)

    first = Singleton()
    second = Singleton()
    print(first is second)

    Point = named_tuple_factory("Point", "x", "y")

    point = Point(21, 42)
    point

    point.x

    point.y

    point[0]

    point[1]

    # point.x = 84

    print(dir(point))


if __name__ == "__main__":
    # t_class1()

    t_class_var()

    ...
