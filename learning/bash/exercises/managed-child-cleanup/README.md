# 受管子进程清理

补齐 TERM 中断路径：父 Bash 只管理自己启动的两个直接子进程，退出前确认它们已结束并收集状态。
这里没有参考实现；从一个新的 Bash 脚本开始，先实现下面的正常路径，再处理 TERM。

## 实现接口

测试以 `bash /candidate.sh STATE_DIR FIRST_SECONDS SECOND_SECONDS` 启动你的脚本，不会 source 它。

- `STATE_DIR` 是测试创建的临时目录，路径可能含空格；两个时长是传给 `sleep` 的正数，可以含小数。
- 直接启动两个 `sleep` 后台任务，分别使用两个时长；不得包裹在额外子 Shell 中，也不得创建其他后台任务。
- 立即记录各自的 `$!`。向 `$STATE_DIR/children.tsv` 写恰好两行，格式为 `first<TAB>PID` 和 `second<TAB>PID`。
- 两个 PID 登记完毕、TERM 处理器已安装后，创建空文件 `$STATE_DIR/ready`。测试看见此文件才读取清单、发送信号。
- 正常路径逐项 `wait` 两个任务，全部成功后返回 0，不能提前终止任务。
- 中断测试只向父脚本发送一次 TERM。父脚本终止仍在运行的受管任务，对两个 PID 完成等待，最后返回 143。
  已结束任务或非零等待状态不能阻断剩余清理。
- stdout/stderr 不规定格式，可用于诊断；不要把测试之外的 PID 当作清理目标，不使用 `kill 0`、负 PID 或按名称 `pkill`。

`children.tsv` 和 `ready` 是测试观察点，不是通用进程监督协议。不接受启动与登记期间的信号，不测试重复信号。

## 运行验收

从仓库根目录运行，最后一个参数替换为你的实现路径；可以放在 `.scratch/`，也可传仓库外路径：

```sh
mise exec -- bash learning/bash/exercises/managed-child-cleanup/test.sh .scratch/my-cleanup.sh
```

需 Docker 和根 mise 环境。实现路径支持空格，但 Docker 挂载参数不支持本测试路径或实现路径中包含逗号。
测试将自身与实现单文件只读挂载到固定 Bash 镜像，关闭网络，限制进程数与资源，临时文件
仅写容器 `/tmp`。不挂载宿主机其他目录或 Docker socket。容器内总运行期限为 20 秒；失败、超时或测试进程被误杀后，
容器退出会销毁其中剩余进程。它用于隔离可信的学习代码失误，不是运行恶意代码的安全沙箱。

| 场景 | 发送 TERM 前的状态 | 期望 |
| --- | --- | --- |
| 正常 | 不发送 TERM，两个任务自然结束 | 父状态 0，两个 PID 均消失 |
| 全运行中断 | 两个任务均在运行 | 只给父 PID 发 TERM，父状态 143，两个 PID 均消失 |
| 部分完成后中断 | 第一个已结束，第二个仍运行 | 同样返回 143 且不遗留任务 |

测试通过 `/proc` 核对 PID 是父脚本直接启动的 `sleep`，检查完成时父子状态，并保留一个无关哨兵进程检验清理范围。
未就绪、卡住或退出状态错误均失败。测试自身有超时清理，不要求学习者实现 KILL 升级。
`check:learning` 仅对本测试做 ShellCheck 和 shfmt，不会在尚无实现时伪造通过的验收。

## 必要参考与边界

- `$!` 给出刚启动后台任务的 PID，不说明最终成功。
- `kill -TERM "$pid"` 请求发送信号，不等待目标退出，也不自动转发给其子进程。
- `wait "$pid"` 等待并取得该子进程状态，不主动终止它；已捕获信号可中断 Bash 对异步任务的 `wait`，返回大于 128，随后运行 trap。
- 先请求仍在运行的任务终止，再确认其结束；对仍运行的任务先等待可能阻塞后续终止请求。
- 143 是本练习明确约定的父退出状态，不是所有 POSIX Shell 的通用信号映射。

验收只能观察进程消失和退出状态，不能单凭这些结果证明代码显式调用了每个 `wait`：Bash 自身也会回收已退出的后台
进程。因此还需结合实现走读确认等待路径；测试通过不等于独立掌握。当前还没有学习者完成本练习的证据。

不覆盖孙进程、忽略 TERM、启动登记竞态、连续信号、重启或严格生产期限。需要这些能力时，使用服务管理器、容器运行时
或 Python/Go 等更适合状态管理的实现，不继续扩展本练习。

依据：[Signals](https://www.gnu.org/software/bash/manual/html_node/Signals.html)、
[trap](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html)、
[kill 与 wait](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html)。
返回 [Bash 学习工作区](../../README.md)。
