# Jade Lab

Jade Lab 是一个个人学习与工程实验仓库，用可执行代码、课程材料和验证记录保存能够重复检查的成果。算法与在线判题
是当前重点；仓库同时保留 Go、Bash 等学习工作区、独立实验和外部参考源码。

各项目按用途独立管理依赖和验证周期，根目录负责固定开发工具并组合常用检查。

## 从哪里开始

| 目标 | 入口 |
| --- | --- |
| 编写题解或查阅竞赛算法 | [`algo/README.md`](algo/README.md) |
| 继续一门课程 | [`learning/README.md`](learning/README.md) |
| 运行独立实验或语言示例 | [`labs/README.md`](labs/README.md) |
| 增加可重复执行的工具 | [`tools/README.md`](tools/README.md) |
| 阅读固定版本的外部项目 | [`references/README.md`](references/README.md) |
| 判断新内容应该放在哪里 | [`docs/project/architecture.md`](docs/project/architecture.md) |

具体项目的准备步骤和最窄检查由其目录中的 README 说明。学习进度只记录在对应主题目录，不在本页复制。

## 准备环境

需要 Git、[mise](https://mise.jdx.dev/) 和能够运行 Linux 容器的 Docker。当前日常验证环境是 macOS arm64，CI 环境是
Ubuntu 24.04 x64。Bash 课程检查要求 Docker daemon 正在运行。

```sh
git clone https://github.com/shiyang07ca/jade-lab.git
cd jade-lab
mise trust
mise install
mise run check
```

`mise run ...` 会自动使用仓库固定的工具。项目目录中的 `python`、`uv`、`go` 或 `mvn` 命令可以通过
`mise exec -- <command>` 运行，也可以按 [mise shell activation](https://mise.jdx.dev/getting-started.html#activate-mise)
配置当前 shell。

首次运行需要网络下载 mise 工具、语言依赖和 Bash 容器镜像。根检查执行本地构建与测试；MySQL 集成和远程 OJ 操作
由对应项目单独启动。

`references/` 中的 Git submodule 按需初始化，具体命令见 [`references/README.md`](references/README.md)。

## 常用命令

```sh
mise tasks                 # 查看根任务
mise run check             # 运行根目录配置的全部检查
mise run check:algo        # 算法分区
mise run check:learning    # 学习工作区分区
mise run check:labs        # 根任务列出的实验
```

根任务在 `mise.toml` 中显式列出项目。准确的检查内容和新增项目要求见
[`docs/project/architecture.md`](docs/project/architecture.md)。单独检查 LeetCode 题目 88：

```sh
cd algo/leetcode
mise exec -- python check.py 88
```

GitHub Actions 会在 pull request 和 `master` push 上使用 Ubuntu 24.04 执行同一个 `mise run check`。

## 项目文档

- [`docs/project/architecture.md`](docs/project/architecture.md)：目录分类、项目组成、依赖关系和根检查范围。
- [`CONTEXT.md`](CONTEXT.md)：本仓库长期使用、容易混淆的领域名称。
- [`AGENTS.md`](AGENTS.md)：维护 Agent 的读取顺序、修改流程和验证要求。

本项目使用 [MIT License](LICENSE)。
