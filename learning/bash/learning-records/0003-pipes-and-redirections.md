# 掌握了管道与重定向

用户理解了重定向（`>` 覆盖、`>>` 追加、`2>` stderr、`2>&1` 合并）和管道（`|` 连接命令的 stdout → stdin）的核心机制，能区分管道（命令↔命令）和重定向（命令↔文件）的不同。掌握了 `/dev/null` 静默输出、`tee` 同时写文件和传管道的用法，并能在实战中组合出 `grep ERROR log | tee errors.txt | wc -l` 这样的管道链。通过了 3 道自检题。

**Implications**：用户可以开始在脚本中读取和理解日志重定向（`>> log 2>&1`）和管道组合。第 4 课引入变量后，可以展示 `LOG_FILE="/var/log/app.log"; grep ERROR "$LOG_FILE"` 这种变量+重定向的组合模式。
