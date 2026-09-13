# 按调用方式与验证程度划分模块

## 背景

旧 `cookbook/` 同时保存语法程序、算法实现和少量经过测试的代码。目录名无法说明代码由谁调用，也容易让单纯
编译通过的章节程序被误认为稳定实现。按语言建立长期大目录同样会把不同用途和发布周期的内容混在一起。

## 决定

- 其他代码通过公开接口依赖的稳定模块进入 `packages/<name>/`，一级目录按能力命名。
- 人、CI 或定时任务作为进程直接启动的重复工作流程进入 `tools/<name>/`。
- 尚未满足前两类条件、但有明确学习或研究价值的可执行实现进入 `labs/<area>/<name>/`。
- 题解、学习材料和固定外部源码分别进入 `problems/`、`learning/` 和 `references/`。
- 模块成熟度记录在 `modules.toml`，不能通过目录改名或编译成功推断。

## 影响

- 旧内容不会因验证不足而删除，也不会进入 `.scratch/`；它按实际主题保留在版本化 lab 中。
- 从 lab 迁入 package 或 tool 时只移动已经验证的实现，不复制两份源码。
- `packages/` 可以暂时很小；缺少真实代码调用方时不为了目录完整而制造抽象。
- 根模块列表默认隐藏 `incomplete`、`legacy`、`external` 和 `pinned`，降低日常索引噪声；显式过滤仍可找到它们。

本次迁移的真实位置：

| 原内容 | 新位置 | 当前含义 |
| --- | --- | --- |
| `cookbook/cpp/` | `labs/algorithms/cpp-implementations/` | 可编译、尚无公开 CMake package 和行为测试 |
| `cookbook/go/` | `labs/languages/go-fundamentals/` | 独立运行的语言机制程序 |
| `cookbook/java/` | `labs/languages/java-runtime/` | Java 并发与运行时机制程序 |
| Python 算法与数据结构实现 | `labs/algorithms/python-implementations/` | 集中维护的复习、题解原型和实验代码 |
| 其他 Python 语言代码 | `labs/languages/python-runtime/` | 保留并逐项验证的实验 |
