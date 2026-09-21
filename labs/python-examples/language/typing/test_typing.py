from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class MyClass:
    name: str
    age: Optional[int]
    email: Optional[str]


class Test:
    a: str

    def __init__(self):
        pass

    def log(self):
        pass


def t_dataclass():
    obj1 = MyClass("Alice", 25, "alice@example.com")
    obj2 = MyClass("Bob", None, None)

    print(obj1)  # 输出: MyClass(name='Alice', age=25, email='alice@example.com')
    print(obj2)  # 输出: MyClass(name='Bob', age=None, email=None)


def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token


from collections.abc import Iterable
from typing import Any, Protocol, TypeVar


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        return self < other


LT = TypeVar("LT", bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


def t_typevar():
    from typing import Generic, List, TypeVar

    T = TypeVar("T")  # 创建一个泛型类型变量

    # 在函数签名中使用泛型类型变量
    def first_item(items: List[T]) -> T:
        return items[0]

    # 在类定义中使用泛型类型变量
    class Box(Generic[T]):
        def __init__(self, content: T):
            self.content = content

    item: T = first_item(list(range(10)))
    print(f"first item: {item}")
    box = Box("hello")
    print(f"box content: {box.content}")


if __name__ == "__main__":
    t_typevar()

    # t_dataclass()

    # parse_token(1)

    # ss = range(8)
    # print(top(ss, 4))

    # import ipdb; ipdb.set_trace()

    pass
