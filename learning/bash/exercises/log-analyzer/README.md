# 日志分析练习

第 13 课的可执行最终版本。它适合练习参数解析、文本流、退出状态、可选 HTTP 通知和失败分支，不宣称替代日志平台。

从仓库根目录运行：

```bash
mise run bash learning/bash/exercises/log-analyzer/test.sh
mise run bash learning/bash/exercises/log-analyzer/analyze-log.sh /path/to/app.log
```

脚本只按示例格式的第三列识别 `[INFO]`、`[WARN]`、`[ERROR]` 和 `[FATAL]`。所谓“后半段密度更高”只是按文件行数归一化的启发式信号，不是时间序列错误率。
