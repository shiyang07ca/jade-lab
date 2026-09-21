# Python 可观测性实验

隔离 OpenTelemetry trace 与 Prometheus metric 示例：

- `opentelemetry_demo.py` 将当前 recording span 的固定宽度 trace、span 和 parent ID 加入结构化日志事件；没有 recording span 时显式写入 `None`。
- `prometheus_demo.py` 记录请求耗时，并允许测试注入 metric、sleep 和单调时钟；直接运行只输出一次 exposition 文本，不打开监听端口。

进入本目录后运行：

```sh
uv run pytest
uv run ruff check .
uv run --frozen python prometheus_demo.py
```

实验不配置 exporter、采样、鉴权或指标 HTTP server，这些属于具体服务的部署选择。
