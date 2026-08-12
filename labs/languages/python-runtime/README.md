# Python 运行时机制实验

本实验保留 Python 类型系统、数据模型、描述器、装饰器、并发、导入机制、日志和 mock 测试程序。文件用于隔离
观察语言或标准库行为，不组成一个 import package，也不承诺统一 API。

```sh
mise install python uv
mise run check lab-python-runtime
```

当前自动测试只覆盖 `testing/mocking/`，其余源码执行语法编译。运行单个实验前应阅读文件中的入口和依赖；如果某项
能力出现真实代码调用方，再提取到按能力命名的 `packages/<name>/`，而不是把整个语言目录发布成一个软件包。
