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

## 初始化环境

仓库根目录的 `mise.toml` 已锁定 Python 3.12.9 和 leetgo 1.4.17。新机器先安装 `mise`，然后在仓库根目录执行：

```sh
brew install mise
mise install python github:j178/leetgo
```

进入本目录后初始化 Python 依赖和题目缓存：

```sh
cd problems/leetcode
mise exec -- uv sync --frozen --python 3.12.9
mise exec -- leetgo cache update
```

`leetgo.yaml` 已设置 LeetCode 中国站，并限定从 Edge 读取登录 Cookie。Cookie 不写入仓库，也不要把
`LEETCODE_SESSION` 或 `LEETCODE_CSRFTOKEN` 保存到 `.env` 或题解文件。使用前请确认 Edge 的当前配置文件已登录
`https://leetcode.cn`；登录失效后重新在 Edge 登录即可。

所有 LeetGo 命令都应在本目录或其子目录执行。为确保使用仓库锁定的工具版本，下面示例统一使用
`mise exec -- leetgo`。

## 编辑器

当前编辑器配置为 Cursor 的自定义命令。生成题目时会打开题面、解答和测试用例；已有题目可以单独打开：

```sh
mise exec -- leetgo edit 1
```

生成题目但不打开 Cursor：

```sh
mise exec -- leetgo pick today --skip-editor
```

Cursor CLI 使用应用内的固定路径 `/Applications/Cursor.app/Contents/Resources/app/bin/cursor`。如果 Cursor
被移动或更换安装位置，需要同步修改 `leetgo.yaml` 的 `editor.command`。

## 日常使用

生成今天的题目，默认生成 Python 目录和文件：

```sh
mise exec -- leetgo pick today
```

也可以按题号或 slug 生成题目：

```sh
mise exec -- leetgo pick 1
mise exec -- leetgo pick two-sum
```

本地测试不会访问远程判题：

```sh
mise exec -- leetgo test 1 --local
```

`leetgo test 1` 默认使用 LeetCode 远程测试；`leetgo test 1 --both` 同时运行本地和远程测试。确认题解后才使用提交命令：

```sh
mise exec -- leetgo submit 1
```

其中 `submit` 会把当前题目文件提交到 LeetCode，不应作为普通测试命令使用。需要查看题面、题目缓存或命令帮助时，可使用：

```sh
mise exec -- leetgo info 1
mise exec -- leetgo cache update
mise exec -- leetgo test --help
```

如果 `.venv` 被 leetgo 重建，重新执行 `mise exec -- uv sync --frozen --python 3.12.9`，让本地运行环境回到
`pyproject.toml` 和 `uv.lock` 定义的依赖集合。

## 检查当前题目

从仓库根目录执行窄检查，只检查指定题目已有的 Python 和 Go 解法：

```sh
mise run leetcode-check 88
```

Python 解法会运行 `basedpyright`、Ruff 和 LeetGo 本地测试；Go 解法会运行 `gofmt` 和 LeetGo 本地测试。
该命令不会扫描其他题目、访问远程判题或提交代码。
