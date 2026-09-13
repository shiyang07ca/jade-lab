# Repository Manager

这个仓库内工具供维护者和 CI 读取根 `modules.toml`，完成模块发现、完整工作站诊断、公共规则检查和模块原生命令
转发。稳定入口是根 `mise` 任务；直接运行 `repo.py` 只用于维护该工具本身。

```sh
mise install python
mise run modules
mise run modules --all
mise run doctor
mise run policy
mise run check lab-python-implementations
mise run check --all --keep-going
```

- `modules` 默认只显示 `active` 与 `stable`；显式类型、状态或 `--all` 可以查看其余模块。
- `check <id>` 只调用目标模块在 `modules.toml` 中声明的 argv，不运行公共规则，也不经过额外 Shell 求值。
- 不带参数的 `check` 运行 `default_check = true` 的模块；`--all` 运行所有明确声明检查的模块。
- `policy` 检查目录与模块类型、索引、相对链接、submodule 记录、Bash 课件复核标记和 `packages/` 未完成标记。
- `doctor` 检查完整 mise 工具集、模块目录、submodule 工作树和课程运行时；它不会初始化或修改 submodule。

`modules`、`policy` 和 `doctor` 只读取仓库与本机状态。`check` 本身不写文件，但被调用的构建工具可能创建模块已忽略
的虚拟环境、缓存，或写入 `.scratch/` 中声明的构建目录。成功返回 `0`；规则错误、诊断失败或模块检查失败返回
`1`；命令行用法错误由 `argparse` 返回 `2`。

验证：

```sh
mise run check tool-repo-manager
```

需要数据库、容器、常驻进程或公网的模块不进入默认检查。Python 的空 `__init__.py` 是允许的软件包标记。
