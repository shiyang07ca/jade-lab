# Labs

`labs/` 保存可独立运行的语言示例、框架验证、数据结构实验和系统编程练习。

| 目录 | 用途 | 验证方式 |
| --- | --- | --- |
| `btree` | B-Tree 插入、分裂、查找与遍历实验 | `cd labs/btree && uv run pytest && uv run ruff check .` |
| `go-examples` | Go 语言与标准库示例 | `cd labs/go-examples && test -z "$(gofmt -l .)" && go test ./... && go vet ./...` |
| `java-examples` | Java 语言与标准库示例 | `cd labs/java-examples && mvn test` |
| `mapstruct` | MapStruct 与 Lombok 注解处理实验 | `cd labs/mapstruct && mvn test` |
| `mybatis` | MyBatis、Mapper XML 与 MySQL 驱动实验 | `cd labs/mybatis && mvn -q -DskipTests package` |
| `python-examples` | Python 语言与标准库示例 | `cd labs/python-examples && uv run pytest && uv run python -m compileall -q language standard-library testing` |
| `python-observability` | OpenTelemetry 与 Prometheus 示例 | `cd labs/python-observability && uv run pytest && uv run ruff check .` |
| `spring-web` | Spring Boot Web 最小实验 | `cd labs/spring-web && mvn test` |
| `unix-linux-programming` | Unix/Linux 系统编程章节示例 | 按章节编译目标源文件，无统一命令 |
