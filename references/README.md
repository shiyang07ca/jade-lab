# External References

本目录只保存不属于本仓库所有权的外部参考源码，并通过 Git submodule 固定到明确 commit，供阅读、对照和分析。

- 项目地址和固定 commit 以根目录 `.gitmodules` 与 Git index 为准。
- 不在 submodule 工作树中记录个人笔记或本地研究结论。
- 个人研究记录统一位于 `docs/open-source/`。

初始化或恢复所有参考源码：

```bash
git submodule update --init --recursive
```

检查当前固定版本：

```bash
git submodule status --recursive
```

参考源码的版本更新应单独评估，并在父仓库中以 gitlink 变更提交。
