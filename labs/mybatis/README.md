# MyBatis 实验

本实验验证 MyBatis 配置、Mapper XML 和 MySQL 驱动能够共同读取 `student` 表。运行环境是 Java 21、Maven 3.9 和
MySQL 8；数据库地址和凭证通过本地环境变量提供。

## 编译检查

数据库服务处于关闭状态时，可以在本目录完成编译检查：

```sh
cd labs/mybatis
mise exec -- mvn -q -DskipTests package
```

该命令覆盖 Java 编译、依赖解析和 Mapper XML 资源打包。Mapper XML 解析和 SQL 执行由下一节的数据库验证覆盖。

## 数据库验证

在专用测试数据库中准备最小表结构：

```sql
CREATE TABLE student (
    sid INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    sex VARCHAR(32) NOT NULL
);

INSERT INTO student (name, sex) VALUES ('Ada', 'female');
```

运行账号至少需要该表的 `SELECT` 权限；验证 Mapper 中的写入语句时还需要 `INSERT` 权限。设置连接信息：

- `LAB_MYSQL_URL`：JDBC URL，例如 `jdbc:mysql://127.0.0.1:3306/lab`
- `LAB_MYSQL_USERNAME`：数据库用户名
- `LAB_MYSQL_PASSWORD`：数据库密码

然后构建运行时 classpath 并启动现有入口：

```sh
cd labs/mybatis
mise exec -- mvn -q -DskipTests package dependency:copy-dependencies -DincludeScope=runtime
mise exec -- java -cp 'target/classes:target/dependency/*' org.example.sql.TestMybatis
```

程序会查询 `student` 表并为每行输出一个 `Student` 实例。缺少环境变量、连接失败、表不存在或账号权限不足时，进程应
以非零状态退出并保留 MyBatis 或 JDBC 的原始错误。
