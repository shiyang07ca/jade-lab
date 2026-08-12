# Bash 学习资源

## Knowledge

- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
  Bash 语法、参数展开、builtin、作业控制和调用规则的一手来源。遇到“Bash 保证什么”时先查这里。
- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
  POSIX shell 的标准定义。用来区分可移植 shell 行为与 Bash 扩展，不能用它推导 Bash 独有功能。
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
  `cp`、`mv`、`sort`、`timeout`、`mktemp` 等 GNU 工具行为的一手文档。脚本依赖 GNU 扩展时必须明确平台要求。
- [ShellCheck repository and wiki](https://github.com/koalaman/shellcheck)
  ShellCheck 规则、安装和限制的官方入口。用于静态分析；警告需要结合目标 Shell 和可复现实验解释。
- [jq Manual](https://jqlang.org/manual/)
  jq 过滤器、类型、退出状态和参数传递的官方说明。用于 JSON 处理练习。
- [Everything curl](https://everything.curl.dev/)
  由 curl 项目维护的协议、命令行、退出状态和安全说明。用于 HTTP/API 与失败处理练习。
- [curl command-line manual](https://curl.se/docs/manpage.html)
  当前命令行选项与退出状态的一手说明；课件中的 `-f`、`-sS`、连接期限和总期限以此核实。
- [util-linux flock manual](https://man7.org/linux/man-pages/man1/flock.1.html)
  Linux 课程示例所用 `flock` 接口；它不是 POSIX 或 macOS 默认接口。
- [The Linux Command Line — William Shotts](https://linuxcommand.org/tlcl.php)
  可公开阅读的系统入门教材。用于第一次建立命令行全貌；精确语义仍回到 Bash、POSIX 或具体工具手册。

## Wisdom (Communities)

- [BashFAQ](https://mywiki.wooledge.org/BashFAQ) 与 [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls)
  长期维护的实践问答和反例集合。适合调查 quoting、`set -e`、管道和子进程陷阱；结论仍应在目标 Bash 版本验证。
- [Unix & Linux Stack Exchange](https://unix.stackexchange.com/)
  适合搜索实际系统和 shell 问题。答案质量不一，应优先采用能引用手册、标准或可重复命令的回答。
- [Stack Overflow — bash](https://stackoverflow.com/questions/tagged/bash)
  用于定位具体错误和相似案例，不把高票数当作正确性证明。

## 适用边界

- 尚缺一份学习者实际需要维护的脱敏脚本或日志，用于验证知识能否迁移到真实工作。
- 部署、systemd、PostgreSQL 和联网 API 示例依赖课程 Bash 镜像之外的系统工具；投入真实使用前必须在目标平台固定并验证这些依赖。
