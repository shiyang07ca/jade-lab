# C++ 算法实现实验

本实验保留 C++ 算法和数据结构实现，用于逐项理解复杂度、边界条件和内存模型。现有源文件大多把实现与
`main` 放在同一文件，CMake 目前只把每个文件编译为独立 object target；这能发现编译错误，但不能证明行为正确，
也没有形成可供其他 CMake 项目链接的公开头文件和导出目标。

```sh
mise install cmake ninja
mise run check lab-cpp-implementations
```

代码不会因为验证不足而删除。需要复用某项实现时，先为该项补行为测试，分离公开头文件与内部实现，再把这一项
迁入按能力命名的 `packages/<name>/`；未达到这些条件前继续作为实验保留。
