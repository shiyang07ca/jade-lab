"""
协变和逆变是类型系统中的概念，它们决定了在类型层次结构中，子类和父类的泛型如何相互作用。

协变（Covariance）：协变意味着一个泛型类型可以接受其子类型。例如，List[Cat] 可以被认为是 List[Animal] 的子类型，如果 Cat 是 Animal 的子类的话。

逆变（Contravariance）：逆变意味着一个泛型类型可以接受其父类型。即使 Cat 是 Animal 的子类，但在逆变情况下，List[Animal] 可以被认为是 List[Cat] 的子类型。
"""

# Python 的 TypeVar 支持指定泛型类型是协变还是逆变。

# TypeVar 可以定义一个泛型类型变量，允许在类型检查期间将该变量绑定为特定的类型。它通常用于泛型函数、类或接口中。

# 协变类型变量使用 covariant=True，表示它可以从子类转换为父类。
from typing import TypeVar, Generic

T_co = TypeVar("T_co", covariant=True)


class Animal:
    pass


class Cat(Animal):
    pass


class Box(Generic[T_co]):
    def __init__(self, item: T_co):
        self.item = item


# Box[Cat] 是 Box[Animal] 的子类型，因为 T_co 是协变的
cat_box: Box[Cat] = Box(Cat())
animal_box: Box[Animal] = cat_box  # 可以赋值，因为 T_co 是协变的

# 在这个例子中，T_co 是协变的，因此 Box[Cat] 可以被视为 Box[Animal] 的子类型。由于 T_co 可以是 Cat 或者 Animal，所以类型系统允许我们将 Box[Cat] 赋值给 Box[Animal]。
