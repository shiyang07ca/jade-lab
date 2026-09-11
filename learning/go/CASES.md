# Go 课程案例索引

本页保存版本和检索入口，不是逐项必修清单。leetgo 与 Dagu 按当前问题选择路径，第一轮共完成至少一项
真实修改即可；Gin、Nuclei、Dagu 分布式 worker/gRPC 和深入性能诊断为选修。使用顺序以
[课程路线](CURRICULUM.md)为准，不要求先获取全部源码。

> 核实日期：2026-08-12。课程不得把 tag、commit、依赖版本或源码路径替换为浮动分支。

## 固定版本

| 案例或依赖 | 课程作用 | Tag/版本 | Commit | 模块声明的 Go 版本 |
| --- | --- | --- | --- | --- |
| [j178/leetgo](https://github.com/j178/leetgo) | 语言、CLI 与真实修改候选 | `v1.4.17` | `393d4219207884c675fc0e3557ff64f86f5c61de` | `go 1.25.0` |
| [dagucloud/dagu](https://github.com/dagucloud/dagu) | 主要后端与系统案例；实际个人自动化工具 | `v2.13.0` | `13745bb8811de8e1cdbe116561e4a4e491edbed5` | `go 1.26.5` |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 高并发网络程序比较案例 | `v3.11.1` | `a8c88feb4a1c8e961b7902534ce3af97e9d524a4` | `go 1.26` |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | HTTP adapter 对照 | `v1.12.0` | `73726dc606796a025971fe451f0aa6f1b9b847f6` | 以固定源码为准 |
| [jackc/pgx](https://github.com/jackc/pgx) | PostgreSQL 驱动；与 Dagu 固定依赖一致 | `v5.9.2` | `0aeabbcf11d859229c1f0b20e710d3596c76bf27` | 以固定源码为准 |

课程统一使用 Go 1.26.5 构建。较新的工具链可以构建声明较早语言版本的模块，但不应修改案例的 `go.mod` 来
伪造兼容结果。PostgreSQL 固定为 18 主版本，补丁版本跟随同一主版本的安全和缺陷修复。

## 案例文件

| 文件 | 负责内容 |
| --- | --- |
| [cases/leetgo.md](cases/leetgo.md) | CLI、配置、HTTP/GraphQL、缓存、文件、子进程和真实修改选择 |
| [cases/dagu.md](cases/dagu.md) | 本地工作流、YAML、执行引擎、HTTP、持久化、队列、恢复、gRPC 和 PostgreSQL action |
| [cases/backend-capability-lab.md](cases/backend-capability-lab.md) | 从零实现后端切片的行为、范围和代码归属 |
| [cases/nuclei.md](cases/nuclei.md) | Runner、Engine、WorkPool、限速、HTTP client pool 和安全限制 |

## 获取源码

案例源码按需获取到仓库外或 `.scratch/`。以下命令固定 commit，不使用 `@latest`、`master`、`main` 或 `dev`：

```sh
git clone https://github.com/j178/leetgo.git
git -C leetgo checkout 393d4219207884c675fc0e3557ff64f86f5c61de

git clone https://github.com/dagucloud/dagu.git
git -C dagu checkout 13745bb8811de8e1cdbe116561e4a4e491edbed5

git clone https://github.com/projectdiscovery/nuclei.git
git -C nuclei checkout a8c88feb4a1c8e961b7902534ce3af97e9d524a4

git -C leetgo rev-parse HEAD
git -C dagu rev-parse HEAD
git -C nuclei rev-parse HEAD
```

三个输出必须与版本表一致。课程修改在个人分支或独立 worktree 中完成；未经明确授权不推送、不创建 PR，
也不代表学习者联系项目维护者。

## 工具链和依赖核验

首次构建前记录工具链、平台、依赖代理、校验服务和磁盘状态。`GOPRIVATE` 与 `GONOSUMDB` 可能包含内部域名，
只在本机核对，不复制到公开日志：

```sh
mise exec go@1.26.5 -- env GOTOOLCHAIN=local go version
mise exec go@1.26.5 -- env GOTOOLCHAIN=local \
  go env GOOS GOARCH GOPROXY GOSUMDB GOPRIVATE GONOSUMDB GOMODCACHE GOCACHE
df -h .
```

显式指定 `go@1.26.5`，避免案例 clone 位于仓库外时意外使用系统 `go`；`GOTOOLCHAIN=local` 又避免 `go` 命令根据
模块声明静默切换到另一个工具链。

- 保持 `GOSUMDB` 启用。出现 checksum mismatch 时停止，核对仓库 `go.sum`、
  [Go checksum database](https://sum.golang.org/) 和代理返回内容，不能关闭校验绕过问题。
- 如需避开已经观察到异常的第三方代理，只使用命令级
  `GOPROXY=https://proxy.golang.org,direct GOSUMDB=sum.golang.org`，不修改全局 Go 配置。
- 冷缓存下载和编译不计主动学习时间。后续只运行当前目标包和目标测试。
- Dagu 首次准备前建议至少保留 12 GiB、Nuclei 至少保留 8 GiB 可用空间；空间不足时先停止，不删除来源不明
  或不可重建的数据。

## 当前验证状态

- 五个 tag 与 commit 已通过项目 Git remote 核对；案例文件列出的源码路径均存在于对应 commit。
- leetgo v1.4.17 已在 Go 1.26.5 下通过全量 `go test -mod=readonly ./...` 和
  `go vet -mod=readonly ./...`。
- Dagu v2.13.0 和 Nuclei v3.11.1 的课程目标包已在空模块缓存、空构建缓存和 Go 1.26.5 下编译通过；环境、命令、
  耗时和限制见[冷缓存编译记录](evidence/0001-pinned-case-cold-builds.md)。
- 实际开始使用某个案例时仍须执行其开始前验证。已有记录不能替代当前 clone 的 commit、工具链、依赖
  和目标包状态；更不能替代课程单元列出的业务测试。

## 使用规则

- 先从可观察行为和失败情况提出问题，再进入固定源码；不按目录顺序通读大型仓库。
- 先读调用方和测试，再读实现。第三方项目中的局部写法只有经过实际限制、失败行为和修改成本检查后才值得采用。
- 性能结论必须保存 Go 版本、平台、输入规模、benchmark 次数和原始结果；使用 `benchstat` 时还要记录其版本。
- 示例只使用假凭证、本地测试凭证或明确授权的目标；日志、课件和公开 issue 不包含敏感原值。
- 升级任一案例时，重新核验 tag、commit、代码路径、依赖、发布说明、磁盘需求和目标测试，不能只改版本表。
