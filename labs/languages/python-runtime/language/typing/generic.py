from typing import Generic, TypeVar  # noqa: F401

# Before 3.12 you have to write:
# T = TypeVar("T")


# class Box(Generic[T]):
#     def __init__(self, content: T):
#         self.content = content

#     def get_content(self) -> T:
#         return self.content


# For Python >= 3.12
class Box[T]:
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content


int_box = Box(123)
print(int_box.get_content())  # 输出：123

str_box = Box("hello")
print(str_box.get_content())  # 输出：hello
