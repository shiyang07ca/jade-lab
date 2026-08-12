# Bash 课件复核记录

## 结论

13 课于 2026-08-12 按 GNU Bash 5.3.15、POSIX Shell Command Language 和所用工具官方手册重新复核。此次不是
只增加版本标记，而是修正会影响真实脚本的语义，并把第 13 课改为引用唯一可执行练习。

固定判定运行时：

```text
docker.io/library/bash:5.3.15-alpine3.24@sha256:a19c811ee9e97fa8a080001d82b8e0ded303f0795cffdb1cbd162731bc8ce208
```

## 主要修正

- 第 1–4 课：区分 Shell 语法、内置和外部命令；修正标准流“自动打开”、按空格解析、赋值语义、展开顺序、
  命令替换删除尾部换行及无条件“永远双引号”等绝对表述。
- 第 5–7 课：区分 `[ ]` 与 `[[ ]]`；删除 `ls | wc -l`、命令替换遍历、不可移植 BRE/`grep -P` 和把
  `sed -i` 称为标准做法等示例；补空输入、平台和管道状态边界。
- 第 8 课：按 Bash 手册重写 `errexit`、`pipefail`、ERR/EXIT trap；删除可复制的破坏性反例和全局修改 IFS 的建议；
  区分三次尝试与三次重试。
- 第 9 课：日志改为明确 stdout/stderr 与写入失败；删除会隐藏上游失败的通用 `safe_replace`；区分 rename 原子可见性、
  崩溃持久性、元数据和业务恢复；删除重复且不安全的“大而全部署骨架”。
- 第 10–11 课：补子进程归属与清理；修正 SIGTERM/SIGHUP、GNU `timeout` 124/137、`jq -e` 状态和 JSON 批处理
  管道子 Shell；HTTP 示例统一设置连接与总期限。
- 第 12 课：本地运行 ShellCheck，不建议上传私有脚本；数据库迁移审查补全输出格式、精确匹配、排序、事务、并发和
  SQL 构造问题；用具体失败问题替代“固定时间内看懂”的承诺。
- 第 13 课：删除三份重复实现，只保留 `exercises/log-analyzer/` 的源码和测试；补 `--help`、带空格路径、空文件、
  前导零、过大阈值、未知参数和超过 5 条消息等边界测试；以测试先行方式完成 `--top N` 接口。

## 验证范围

从仓库根目录运行：

```bash
mise run check learning-bash
```

检查覆盖固定 Bash 版本、关键 Bash 语义冒烟测试、所有练习脚本的 ShellCheck/shfmt/语法，以及日志分析器离线测试。
HTML 中的 `systemctl`、`flock`、GNU `mv`/`timeout`、PostgreSQL 和联网 API 示例不会在课程容器中伪造成功；投入真实
使用前必须在目标平台固定依赖并做集成测试。

历史 `learning-records/` 保存当时的能力判断及其有限证据；含有旧表述时以当前课件和本文件为准，也不能单独证明
当前掌握程度。

## 一手资料

- [GNU Bash 5.3 Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [curl command-line manual](https://curl.se/docs/manpage.html)
- [jq Manual](https://jqlang.org/manual/)
- [PostgreSQL password file](https://www.postgresql.org/docs/current/libpq-pgpass.html)
- [ShellCheck repository](https://github.com/koalaman/shellcheck)
