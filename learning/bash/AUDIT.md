# Bash 课件复核记录

## 结论

13 份旧 HTML 课件已于 2026-08-12 逐课复核，目标解释器固定为 GNU Bash 5.3.15。每份课件包含同日的 `course-audit` 元数据；仓库检查会拒绝缺少复核标记、版本或含未完成标记的课件。

固定运行时：

```text
docker.io/library/bash:5.3.15-alpine3.24@sha256:a19c811ee9e97fa8a080001d82b8e0ded303f0795cffdb1cbd162731bc8ce208
```

复核不表示 HTML 中每段外部系统示例都可以直接用于生产。课程镜像验证 Bash 语义和离线练习；`systemctl`、`flock`、GNU `mv -T`、PostgreSQL、curl 和 jq 等接口仍须在实际目标平台单独固定与测试。

## 逐课结果

| 课次 | 复核重点与主要修正 |
| ---: | --- |
| 1 | 区分函数、内置与外部命令；用 `type` 代替 `which` 解释 Bash 查找；fork/exec 改为外部命令的简化模型；退出状态不再等同程序故障。 |
| 2 | 修正 `cd -` 可反复切换；说明 GNU/BSD 文件命令差异；使用 `chmod u+x` 明确权限对象。 |
| 3 | 复核文件描述符、重定向顺序、管道和 `tee`；保留为组合命令入门。 |
| 4 | 补充变量名首字符规则、展开上下文、ShellCheck SC2086 边界，以及 `"$@"` 与 `"$*"` 的准确语义。 |
| 5 | 将 `[` 改为命令形式而非 alias；区分 Bash `[[ ]]` 与 POSIX `[ ]`；移除对 Dockerfile Shell 的绝对化描述。 |
| 6 | 说明 `local` 是 Bash 扩展；脚本分层改为可选结构；修复函数内 EXIT trap 引用已失效局部变量的问题。 |
| 7 | 删除百分比式经验断言；修正不可复制的反斜杠行尾注释、IP 外形匹配、`ps | grep` 误匹配和 sed 平台差异。 |
| 8 | 按 Bash 手册重写 errexit、pipefail 和 ERR/EXIT trap；修复最终失败仍返回成功的重试循环；增加 xtrace 敏感数据警告。 |
| 9 | 明确 `flock` 是 Linux 协作式锁且不能在持锁时删除 inode；区分 rename 原子可见性与持久性；重写配置优先级、JSON 通知、备份恢复与 GNU `mv -T` 链接切换。 |
| 10 | 修复函数内外双重后台化和遗漏子任务状态；补充 `lastpipe`、信号编号、PID 复用、nohup/disown 边界；长期进程改由服务管理器负责。 |
| 11 | curl 改用 `-fsS`、连接期限和总期限；字段读取增加 jq 类型与退出状态验证；删除 grep/sed 解析 JSON 和 jq 体积/依赖绝对化描述。 |
| 12 | `source` 前要求入口保护并使用一次性子 Shell；说明 ShellCheck 与 xtrace 的认识边界；数据库迁移示例明确标为缺陷审查练习，并补充密码、事务、并发与 SQL 注入问题。 |
| 13 | 修复不可复制的续行、零匹配和参数解析；将“错误率”降为按行密度启发式；新增真实日志分析脚本和离线失败测试。 |

## 自动验证

从仓库根目录运行：

```bash
mise run check learning-bash
```

该命令检查：

1. 固定镜像中的 `BASH_VERSION=5.3.15`。
2. `set -e` 条件上下文、`pipefail`、逐个 `wait` 和 EXIT 清理的冒烟行为。
3. 所有 `learning/bash/exercises/**/*.sh` 的 ShellCheck 与 shfmt。
4. 日志分析器的正常统计、密度提示、非法阈值和缺失选项值。

## 一手资料

- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)：命令查找、展开、管道、`set`、`trap`、作业控制和 `wait`。
- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)：可移植 Shell 语义。
- [POSIX `rename()`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html)：同文件系统替换的原子可见性。
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)：`mv -T`、`timeout` 与文件工具。
- [curl command-line man page](https://curl.se/docs/manpage.html)：`--fail`、`--show-error` 和期限选项。
- [jq Manual](https://jqlang.org/manual/)：`-e`、`-r`、`--arg` 与类型。
- [PostgreSQL password file](https://www.postgresql.org/docs/current/libpq-pgpass.html) 与 [environment variables](https://www.postgresql.org/docs/current/libpq-envars.html)：客户端密码处理。
- [Docker Official Image for Bash](https://hub.docker.com/_/bash)：课程镜像来源。
- [ShellCheck repository](https://github.com/koalaman/shellcheck)：静态检查规则与限制。
