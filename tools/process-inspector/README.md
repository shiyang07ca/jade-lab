# Process Inspector

这个命令供开发者在本机排查重复进程或线程数异常时使用。调用方提供进程名称或命令行片段，命令读取当前进程表，
按 PID 输出匹配进程的名称、线程数和完整命令行；它不修改进程或系统状态。

## 安装和调用

```sh
mise install python uv
uv sync --frozen
uv run process-inspector python
# 或
uv run python -m process_inspector python
```

上面两个命令进入同一 Python CLI，是跨平台的受支持入口。`scripts/thread-count.sh` 是依赖 macOS `pgrep`、
`ps -M` 和 Bash 的受限入口，只用于尚未准备 Python 环境时的本机诊断；Linux CI 不验证其线程统计语义。

匹配忽略大小写，并同时搜索进程名称和命令行。输出按 PID 升序排列，每行格式为：

```text
PID=<pid> name=<name> threads=<count> command=<shell-quoted command>
```

受支持 Python 入口的退出码：

- `0`：至少找到一个匹配进程，结果写入 stdout。
- `1`：没有匹配进程，说明写入 stderr。
- `2`：参数无效；`argparse` 产生的用法说明或参数错误写入 stderr。
- 其他非零值：依赖加载或未处理的系统错误导致进程终止。

受限 Shell 入口把 `pgrep` 的状态 `1` 解释为无匹配，其他非零状态原样传播。PID 在匹配后可能退出；单个 PID 的
`ps` 读取失败会产生一条 stderr 诊断并继续处理其余 PID。只要至少输出一个结果，最终状态就是 `0`；如果所有匹配项
都无法读取，则返回第一次 `ps` 失败的状态。

进程可能在扫描期间退出；权限不足、僵尸进程和已经退出的单项会被跳过，所以结果是一次尽力而为的系统快照，
不能用于授权判断或保证进程身份。完整命令行可能含访问令牌、数据库地址或其他敏感参数；不要把原始输出提交到
仓库或粘贴到公开 issue，分享前先删除敏感值。验证命令：

```sh
uv run --frozen pytest
uv run --frozen ruff check .
bash -n scripts/thread-count.sh
```
