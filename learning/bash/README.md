# Bash 学习工作区

目标是安全地阅读、修改和测试日常自动化脚本，明确输入、参数、文件、退出状态和子进程边界。
Bash 用于薄的系统编排；状态复杂、并发密集或需要进程监督时，选择 Python、Go 或服务管理器。

## 路线与当前证据

路线是命令与展开、数据流与退出状态、脚本组织、失败处理、后台任务与清理，随后转入真实任务和按需回顾。
基础内容已接触；当前应用证据主要来自以下记录：

- [0013 日志分析](learning-records/0013-log-analysis-and-language-boundary.md)：测试改动、人工迁移夹具与真实脚本隔离修复；真实 macOS `ps -M` 行为仍待目标环境验证。
- [0014 后台任务](learning-records/0014-background-job-status-aggregation.md)：用户实现 collect-all，验证成功、单项失败和完成顺序变化。

下一步是[受管子进程清理练习](exercises/managed-child-cleanup/README.md)：只给父 Bash 发送 TERM，验证两个直接子进程
的终止与回收。该能力尚无学习者实现证据。

## 工程入口

- [日志分析器](exercises/log-analyzer/README.md)：实现、失败测试和人工迁移输入。
- [受管子进程清理](exercises/managed-child-cleanup/README.md)：实现接口、隔离验收命令与进程边界。
- [展开与引用速查](reference/expansion-and-quoting.md)：按语法上下文判断参数如何形成。

从仓库根目录运行：

```sh
mise run bash learning/bash/exercises/log-analyzer/test.sh
mise exec -- python learning/bash/check.py
```

判定环境由根 [mise.toml](../../mise.toml) 的 `JADE_BASH_IMAGE` 和 `JADE_BASH_VERSION` 固定，需可用的 Docker；
macOS 自带 Bash 仅供兼容观察。`check.py` 对所有练习脚本运行 ShellCheck 和 shfmt，再运行固定容器中的语义测试与
日志分析器测试。清理测试当前只做静态检查，有学习者实现后按练习入口手动验收。分区检查为 `mise run check:learning`。

## 当前资料

- [GNU Bash 手册](https://www.gnu.org/software/bash/manual/bash.html)：语言与 builtin 行为；信号与等待的具体来源见清理练习。
- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)：可移植 Shell 的语言边界。
