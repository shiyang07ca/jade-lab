# 后端能力实验：任务接纳切片

返回[案例索引](../CASES.md)。本实验不是长期产品，也不虚构用户需求。它是一段完成后可以删除的独立实现，
用来证明学习者能够从空目录构建含 HTTP、PostgreSQL、有限后台任务、取消和优雅退出的后端行为。

## 代码归属

开始实现时在仓库根目录创建 `labs/scheduling/job-intake-go/`，使用独立 Go module 和 README。本课程文件只保存
任务定义；实现、迁移和测试不能复制到 `learning/`。完成 35 小时检查后，可以按实际复用价值保留为 lab；只有
出现代码调用方、提取出明确公开接口并补齐消费方测试的部分，才转入按能力命名的 `packages/<name>/`。

实验不导入 Dagu 内部包，也不仿制完整工作流引擎。它补充 Dagu 默认文件持久化没有集中覆盖的典型事务后端能力。

## 固定行为

- `POST /jobs`：要求 idempotency key；严格验证 JSON 后在 PostgreSQL 18 中创建任务；重复请求返回同一任务。
- `GET /jobs/{id}`：返回任务状态；不存在时返回稳定的用户错误，不暴露内部实现。
- `POST /jobs/{id}/cancel`：记录取消请求；worker 必须观察取消并终止可控工作。
- 固定数量 worker 通过事务领取任务；等待队列有上限；关闭后拒绝新任务并等待或取消现有任务。
- 先用 `net/http`，再只替换 HTTP adapter 为 Gin v1.12.0；应用逻辑、repository 和行为测试不能复制。
- 测试使用真实 PostgreSQL 18，覆盖迁移、约束、幂等、并发领取、取消、队列满和优雅退出。

事务领取可以使用 `SELECT … FOR UPDATE SKIP LOCKED` 或原子 `UPDATE … RETURNING`，但必须先定义重复领取、
饥饿、公平性和失败重试的预期，再用并发测试选择，不能因为示例代码常见就采用。

## 明确不做

- 认证产品化、Web UI、ORM、Redis、Kafka、Kubernetes 或部署。
- 通用任务编排、cron 表达式、插件系统或多租户。
- 用 map、mock repository 或内存数据库替代 PostgreSQL 事务检查。

## 完成标准

1. 三个 API 的成功和无效输入行为通过 `httptest` 验证。
2. 真实 PostgreSQL 约束、幂等写入和并发领取测试通过。
3. 队列饱和、请求取消、服务关闭和 goroutine 结束均有确定结果。
4. `go test -race ./...`、静态分析和构建退出为零。
5. 能现场解释一次失败从 HTTP 输入到数据库或 worker，再返回调用方的完整过程。
