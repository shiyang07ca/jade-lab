# 掌握了 Bash 中处理 JSON/API

用户理解了 curl 的六个核心参数（`-s` 静默、`-f` HTTP 错误转退出码、`-X` 方法、`-H` 头、`-d` 请求体、`--max-time` 超时）及四大典型场景（健康检查 GET、取 JSON 数据、POST JSON 发 Webhook、下载文件）。掌握了 jq 的字段提取（`.field`、`-r` raw 输出）、数组展开（`.[]`）、条件过滤（`select()`）、安全构造 JSON（`--arg` 传变量），以及 curl + jq 组合的四种实战模式（获取 Release 版本号、轮询部署状态、发送通知、批量读配置）。理解了三条黄金法则：curl 永远加 `-f` 和 `--max-time`；jq 赋值给 Bash 永远加 `-r`；永远用 `--arg` 构造 JSON 不拼接字符串。通过了 4 道自检题。

**Implications**：用户现在可以编写和阅读与 HTTP API 交互的 Bash 脚本，这是现代 DevOps 自动化的核心技能。第 12 课将综合前 11 课所学，教授系统化阅读和调试未知脚本的方法论。
