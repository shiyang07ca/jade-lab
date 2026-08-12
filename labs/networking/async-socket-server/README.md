# Async Socket Server Lab

比较阻塞、线程、`select`、Linux `epoll` 与 libuv server 的历史网络实验。源码来自公开教学材料，当前保留其
平台假设和阶段差异用于阅读，不是可直接部署的 server。

该模块主要面向 Linux；macOS 不提供 `epoll`，libuv 示例还需要系统级 libuv。开始修改前先选择一个明确实现，
在对应平台只构建目标文件，并用本地 client 验证连接、退出和资源释放。不要直接运行 `make all` 来推断每个变体
都能在当前机器工作。
