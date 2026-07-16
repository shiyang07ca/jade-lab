# LeetCode

本目录使用 leetgo 管理题目生成、本地测试和提交。题目以 LeetCode 标识符聚合，语言作为题目下的第二层目录。

```text
<problem-id>/
├── python/
├── go/
├── cpp/
├── rust/
└── java/
```

每个语言目录保留 leetgo 生成的题面、解答和测试用例。竞赛题先进入 `contests/`，获得正式题号后再迁入标准题目目录，并删除重复副本。

Python 项目的依赖真源是 `pyproject.toml` 和 `uv.lock`。leetgo 自身可能临时生成 `requirements.txt` 并重建 `.venv`；该文件不进入版本库，发生重建后需要重新按 uv 锁文件同步环境。
