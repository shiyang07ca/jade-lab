# 第 3 课历史学习记录

当时完成了管道和重定向的即时自检，能区分 stdout、stderr、文件重定向和 `tee`。当前能力需通过重定向顺序、
`pipefail` 和上游失败的实际预测验证。

恢复检查：比较 `cmd >file 2>&1` 与 `cmd 2>&1 >file`，并解释 `producer | tee file` 的默认状态来自哪里。
