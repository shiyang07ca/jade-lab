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
mise install go github:j178/leetgo
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
mise run check lab-python-implementations  # 只检查一个模块
mise run check                            # 检查默认稳定模块
mise run check --all --keep-going
mise run policy                           # 检查目录、索引、文档链接和内容规则
mise run doctor                           # 诊断完整工具集和所有 submodule 工作树
```

修改单个模块时先运行其检查；修改根目录规则、模块索引或公共文档时再运行 `mise run policy`。准备提交公共变更时
运行 `mise run policy && mise run check`。

## 工作入口

- 学习主题从 [`learning/`](learning/) 选择；Go 课程从 [`learning/go/README.md`](learning/go/README.md) 开始。
- 目录职责、模块准入和迁移只在 [`docs/project/architecture.md`](docs/project/architecture.md) 定义。
- 修改、验证和提交要求见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

一次只处理一个模块：先运行最窄检查，修改后重跑；只有根规则、模块索引或公共文档变化才额外运行
`mise run policy`。完整日志、缓存和一次性验证留在 `.scratch/`。
