# Python 语言与标准库示例

这里保存 Python 类型系统、数据模型、描述器、装饰器、并发、导入、日志和 mock 示例。每个文件独立展示一种语言或
标准库行为。

进入本目录后运行：

```sh
uv run pytest
uv run python -m compileall -q language standard-library testing
```

当前自动测试覆盖 `testing/mocking/`，语法编译覆盖其余示例。
