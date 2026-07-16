# Process Inspector

根据命令行关键字查找进程，输出 PID、名称、线程数和完整命令行。Python 实现基于 psutil，返回结构化结果后再由 CLI 渲染；`scripts/thread-count.sh` 是面向 macOS 的轻量替代实现。
