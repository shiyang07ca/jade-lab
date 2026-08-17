# 日志分析练习

第 13 课的可执行最终版本。它适合练习参数解析、文本流、退出状态、可选 HTTP 通知和失败分支，不宣称替代日志平台。

从仓库根目录运行：

```bash
mise run bash learning/bash/exercises/log-analyzer/test.sh
mise run bash learning/bash/exercises/log-analyzer/analyze-log.sh /path/to/app.log
```

`fixtures/migration-practice.txt` 是人工构造的迁移练习输入。它故意包含动态请求字段、多行堆栈、未知级别、畸形行和
不同的时间戳格式，用于暴露当前解析规则的边界；它不能替代学习者实际工作日志的迁移检验。

脚本只按示例格式的第三列识别 `[INFO]`、`[WARN]`、`[ERROR]` 和 `[FATAL]`。所谓“后半段密度更高”只是按文件行数归一化的启发式信号，不是时间序列错误率。

接口约定：

- `--help` 不需要日志路径；未知或重复位置参数会失败。
- `--alert-threshold` 接受 `0` 到 `999999999`，前导零按十进制处理。
- `--top` 控制高频严重消息数量，默认 5，只接受 1–100 的十进制整数。
- `--webhook` 只接受 `http://` 或 `https://`；URL 可能包含敏感令牌，不要在 xtrace 或公开日志中输出。
- stdout 是报告，stderr 是诊断和阈值告警。可选 webhook 属于 best-effort 通知，发送失败不会改变分析结果。
- 输入格式变化时先修改测试夹具和解析规则，不要把本脚本当作通用日志解析器。
