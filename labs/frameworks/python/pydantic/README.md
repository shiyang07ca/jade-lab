# Pydantic Lab

Pydantic v2 输入边界实验。`model_demo.py` 把外部字典解析为员工领域数据，并验证别名、类型、字段限制与跨字段
规则；无效输入显式抛出 `ValidationError`，不使用静默默认值。

```sh
mise run check lab-python-pydantic
```

当前实验只证明进程内模型验证，不代表数据库约束或 HTTP 错误响应已经实现。
