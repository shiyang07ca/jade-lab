# 工程约定

每个独立运行模块自行声明环境、依赖和验证方式，仓库根目录只固定开发工具版本。

- Python 使用 `pyproject.toml` 与 `uv.lock`，不使用 PDM。
- Go 的稳定样本共享 `cookbook/go/go.mod`；独立 lab 或 tool 使用自己的 module。
- Java 核心样本与框架实验使用独立 Maven 项目，默认目标 JDK 21。
- C/C++ 使用 CMake；共享配置进入 `CMakePresets.json`，个人配置不提交。
- Shell 默认兼容 POSIX，使用 Bash 特性时必须明确解释。
- submodule 的 commit 固定与本仓库代码修改分开维护。

独立项目的 README 至少说明目标、适用范围、运行前提和当前限制。锁文件由对应依赖管理器生成，不手工编辑。
