# 外部参考源码

本目录通过 Git submodule 固定外部项目，用于阅读、对照和分析。父仓库记录每个项目的 URL 和 gitlink。

| 项目 | 本地路径 | 用途 |
| --- | --- | --- |
| [500 Lines or Less](https://github.com/aosabook/500lines) | `references/500lines` | 阅读小型系统的完整实现 |
| [algorithmbasic2020](https://github.com/algorithmzuo/algorithmbasic2020) | `references/algorithmbasic2020` | 对照算法课程实现 |
| [algorithms](https://github.com/keon/algorithms) | `references/algorithms` | 对照 Python 算法与数据结构实现 |
| [codeforces-go](https://github.com/EndlessCheng/codeforces-go) | `references/codeforces-go` | 阅读 Go 竞赛算法与题解 |
| [Guava](https://github.com/google/guava) | `references/guava` | 阅读 Java 基础库设计与测试 |

按当前研究目标初始化单个项目：

```sh
git submodule update --init --recursive references/codeforces-go
```

更新固定版本时，先在目标路径获取上游提交，再由父仓库记录新的 gitlink；使用 `git submodule status --recursive`
检查当前版本。研究记录保存在本仓库的主题文档中。
