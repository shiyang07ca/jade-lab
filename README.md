# Jade Lab

Jade Lab 是一个个人学习、软件研究和工具开发仓库。目录按内容的用途和验证程度划分；每个模块独立管理依赖与
检查，根目录只负责模块发现、工具版本和公共规则。

## 新机器启动

本机只需先安装 Git 和 [mise](https://mise.jdx.dev/)。普通 clone 不下载外部参考源码：

```sh
git clone https://github.com/shiyang07ca/jade-lab.git
cd jade-lab
mise install python
mise run check tool-repo-manager
mise run modules
```

随后只安装当前模块需要的工具。例如开始 Go 课程：

```sh
mise install go ubi:j178/leetgo
sed -n '1,220p' learning/go/README.md
```

需要研究某个固定外部项目时再初始化对应路径：

```sh
git submodule update --init --recursive references/codeforces-go
```

`mise install` 不带参数会安装完整多语言工具集，只有准备完整工作站时才需要。

## 选择和检查模块

[`modules.toml`](modules.toml) 是唯一模块索引。默认列表只显示 `active` 和 `stable` 模块；显式过滤或 `--all`
可以查看历史实验、外部依赖模块和固定参考源码。

```sh
mise run modules
mise run modules --kind learning
mise run modules --kind package
mise run modules --kind reference
mise run modules --status legacy
mise run modules --all
```

模块检查与公共规则分开运行：

```sh
mise run check package-python-algorithms  # 只检查一个模块
mise run check                            # 检查默认稳定模块
mise run check --all --keep-going
mise run policy                           # 检查目录、索引、文档链接和内容规则
mise run doctor                           # 诊断完整工具集和所有 submodule 工作树
```

修改单个模块时先运行其检查；修改根目录规则、模块索引或公共文档时再运行 `mise run policy`。准备提交公共变更时
运行 `mise run policy && mise run check`。

## 目录职责

| 目录 | 唯一职责 |
| --- | --- |
| [`learning/`](learning/) | 学习使命、课程顺序、筛选资料和已经由表现证明的学习结果 |
| [`packages/`](packages/) | 被其他代码导入、链接或声明为依赖的稳定软件包 |
| [`problems/`](problems/) | 按平台与题目标识符保存的 OJ 解答和未完成尝试 |
| [`labs/`](labs/) | 围绕明确问题、可以独立重做的实验 |
| [`tools/`](tools/) | 由人、CI 或定时任务直接启动，用来完成一个命名的重复工作流程的程序 |
| [`references/`](references/) | 以 Git submodule 固定 commit、按需初始化的外部源码 |
| [`docs/`](docs/) | 跨模块规则、研究结论和架构决定 |
| `.scratch/` | 本机票据、临时 clone、日志、缓存和其他可重建状态 |

`packages/` 与 `tools/` 的分界取决于调用方式：其他代码依赖前者，人或自动化系统作为进程启动后者。课程和题解
产生的代码不会因“以后可能有用”自动进入这两个目录；详细准入与迁移规则见
[`docs/project/architecture.md`](docs/project/architecture.md)。

## 推荐工作流

一次 20–50 分钟的学习或研究只处理一个模块：

1. 从 `mise run modules` 或 `learning/<topic>/README.md` 找到下一项任务。
2. 写下可以被测试推翻的问题和预期结果，运行最窄检查。
3. 一次性验证放 `.scratch/`；需要独立依赖或保留实验条件时进入 `labs/`。
4. 只阅读回答当前问题所需的调用方、测试和实现，不顺序通读大型仓库。
5. 结束前重跑模块检查，记录版本、命令、结果和下一步。

工程修改规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)，Go 课程从
[`learning/go/README.md`](learning/go/README.md) 开始。
