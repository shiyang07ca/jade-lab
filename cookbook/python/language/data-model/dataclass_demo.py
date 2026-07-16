from dataclasses import dataclass


@dataclass
class Rectangle:
    _width: float = 0
    _height: float = 0

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @width.setter
    def width(self, value):
        self._width = value
        # 在 width 发生变化时更新 area 和 perimeter
        self._area = self.width * self.height
        self._perimeter = 2 * (self.width + self.height)

    @height.setter
    def height(self, value):
        self._height = value
        # 在 height 发生变化时更新 area 和 perimeter
        self._area = self.width * self.height
        self._perimeter = 2 * (self.width + self.height)


def test1():
    # 创建一个 Rectangle 对象
    rectangle = Rectangle(3, 4)

    # 输出初始的 area 和 perimeter
    print(rectangle.area)  # 输出: 12.0
    print(rectangle.perimeter)  # 输出: 14.0

    # 修改 width 和 height 的值
    rectangle.width = 5
    rectangle.height = 6

    # 输出更新后的 area 和 perimeter
    print(rectangle.area)  # 输出: 30.0
    print(rectangle.perimeter)  # 输出: 22.0


def test2():
    rec = Rectangle()
    rec.width = 5
    print(rec.width, rec.height)


if __name__ == "__main__":
    print("================ 1")
    test1()

    print("================ 2")
    test2()
