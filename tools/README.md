# Tools

`tools/` 保存由人、CI 或定时任务直接启动、用来完成一个可命名的重复工作流程的程序。工具的主要接口是进程入口，
而不是供其他模块导入的内部函数。

工具把一个重复工作流程封装为稳定进程接口：调用者知道何时启动、如何传入配置、如何根据 stdout/stderr 和退出码
判断结果，以及它会修改哪些本地或远程状态。完整准入条件见 [仓库架构](../docs/project/architecture.md)。

当前工具：

- [`process-inspector/`](process-inspector/)：开发者按关键字检查本机进程和线程数。
- [`repo-manager/`](repo-manager/)：开发者与 CI 列出模块、检查仓库规则并调用模块自己的检查命令。

模块清单以 [`modules.toml`](../modules.toml) 为准；本文件只补充工具目录入口。
