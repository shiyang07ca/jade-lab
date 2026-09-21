# Unix/Linux 系统编程示例

本目录按章节保存 Unix/Linux 系统调用、文件、进程、信号、终端、管道、套接字和线程示例。源码来自逐章练习，部分
程序依赖终端、POSIX API、Linux 行为或同章节的多个源文件，不承诺在 macOS 与 Linux 上得到相同行为。

## 编译单文件示例

需要系统 C 编译器和 POSIX shell。构建结果写入 `.scratch/`：

```sh
mkdir -p .scratch/build/unix-linux-programming
cc -std=c11 -Wall -Wextra \
  -o .scratch/build/unix-linux-programming/more01 \
  labs/unix-linux-programming/CH01/more01.c
.scratch/build/unix-linux-programming/more01 labs/unix-linux-programming/README.md
```

多文件程序需要先检查目标源码的头文件、同章节辅助文件和链接库。例如第 9 章的 shell 示例在 `CH09/Makefile.smsh`
中记录源文件组合，该命令生成的目标和对象文件在运行后清理。

## 验证范围

选择示例后先完成编译，再根据源码准备终端、文件、端口、信号或并发条件。各章节使用独立验证命令；目标章节具备
稳定输入、预期输出和清理方法后，可以加入根检查。
