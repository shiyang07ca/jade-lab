# Bash 课程进度

课程以能否解释和修改真实脚本判断完成，不以课件数量判断。现有学习记录支持第 1–12 课已经达到当时的检查标准；
第 13 课只有课件，仍需实践证明。

| 课次 | 主题 | 材料 | 状态 |
| ---: | --- | --- | --- |
| 1 | Shell 执行模型、`PATH`、退出状态和标准流 | [课件](lessons/0001-how-shell-executes-commands.html) | 已有学习记录 |
| 2 | 文件系统导航、查看、创建和权限 | [课件](lessons/0002-file-system-operations.html) | 已有学习记录 |
| 3 | 管道与重定向 | [课件](lessons/0003-pipes-and-redirections.html) | 已有学习记录 |
| 4 | 变量、引用与展开 | [课件](lessons/0004-variables-quoting-expansion.html) | 已有学习记录 |
| 5 | `if`、循环、`case` 与短路执行 | [课件](lessons/0005-control-flow.html) | 已有学习记录 |
| 6 | 函数、局部变量、入口和 `source` | [课件](lessons/0006-functions-and-script-structure.html) | 已有学习记录 |
| 7 | `grep`、`sed`、`awk` 与组合使用 | [课件](lessons/0007-text-processing-trio.html) | 已有学习记录 |
| 8 | 失败处理、清理和调试 | [课件](lessons/0008-error-handling-and-debugging.html) | 已有学习记录 |
| 9 | 部署脚本常见结构 | [课件](lessons/0009-deployment-patterns.html) | 已有学习记录 |
| 10 | 后台任务、信号、等待和超时 | [课件](lessons/0010-process-management.html) | 已有学习记录 |
| 11 | 使用 `curl` 与 `jq` 处理 HTTP/JSON | [课件](lessons/0011-json-api-curl-jq.html) | 已有学习记录 |
| 12 | 分层阅读和调试陌生脚本 | [课件](lessons/0012-reading-and-debugging-scripts.html) | 已有学习记录 |
| 13 | 日志分析与监控脚本综合练习 | [课件](lessons/0013-log-analysis-practice.html) · [实现](exercises/log-analyzer/analyze-log.sh) · [测试](exercises/log-analyzer/test.sh) | 实现已验证，待学习记录 |

## 下一项检查

选择一份学习者确实需要维护的部署脚本，在隔离环境中完成：

1. 不运行脚本，先说明输入、外部命令、文件修改、进程和预期退出状态。
2. 使用假配置和可控命令复现至少一个成功和两个失败情况。
3. 记录 ShellCheck 与目标 Shell 的版本，运行语法和静态检查，并解释每个保留或忽略的警告。
4. 证明临时文件、锁、后台进程和敏感输出在成功、失败及信号中断后得到正确处理。

通过后再新增学习记录；如果没有真实脚本需求，本课程暂停，不用用虚构功能填满剩余课次。

课件已按 [AUDIT.md](AUDIT.md) 在 GNU Bash 5.3.15 目标下复核。复核只说明材料当前可用，不替代学习表现证据。
