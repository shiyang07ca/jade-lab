# Packages

`packages/` 只保存由其他代码直接导入、链接或声明为依赖的软件包。每个一级子目录是一个能够独立构建和测试的
发布单元，名称描述它提供的能力，而不是笼统地按语言归档代码。

模块必须有具体复用场景、稳定公开接口、语言原生依赖产物和隔离消费方测试。仓库内可以暂时没有真实调用方，但不能
只凭“以后可能有用”进入这里；完整准入条件见 [仓库架构](../docs/project/architecture.md)。

当前没有独立维护的软件包。算法复习实现位于
[`labs/algorithms/python-implementations/`](../labs/algorithms/python-implementations/)。

只有命令行入口的程序属于 `tools/`；研究实现属于 `labs/`。目录选择不表示删除未晋升代码，也不把源码移入
`.scratch/`。
