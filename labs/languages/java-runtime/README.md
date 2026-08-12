# Java 并发与运行时实验

本实验保留 JDK 21 下的集合、线程池、同步器、泛型、注解、代理、依赖注入和类加载机制程序。多数类通过
`main` 展示行为，现有 JUnit 测试只覆盖少量基础代码；Maven 测试通过代表编译和现有测试成功，不代表全部实现
可以作为依赖发布。

```sh
mise install java maven
mise run check lab-java-runtime
```

新增工作应围绕一个明确问题选择最小目录，不继续堆积无关章节代码。某项实现只有在出现代码调用方、形成公开 API、
补齐行为测试并能独立发布为 Maven artifact 后，才迁入 `packages/<name>/`。
