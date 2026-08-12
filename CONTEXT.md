# Jade Lab

本仓库用于把学习材料转化为可重复验证、可持续维护的个人工程资产。

## Language

**学习工作区（Learning Workspace）**:
围绕一个明确学习使命组织、需要版本历史的课程安排、课件、资料索引和学习记录。可执行实验和外部源码不属于
学习工作区。
_Avoid_: Notes Dump, Course Archive

**软件包（Package）**:
由其他代码导入、链接或声明为依赖，具有公开接口、稳定错误类型、构建产物和消费方测试的模块。
_Avoid_: Sample, Demo, Playground, Snippet

**Problem Solution**:
由题目平台和稳定题目标识符定位的一组单语言或多语言解答。
_Avoid_: Algo Folder, OJ Script

**Lab**:
围绕明确问题或假设建立、拥有独立运行环境但尚未晋升为稳定资产的实验。
_Avoid_: Test Project, Playground

**Tool**:
由人、CI 或定时任务作为进程直接启动，用来完成一个命名的重复工作流程，并明确参数、输出、状态变更和退出码的程序。
_Avoid_: Utility, Helper Script

**Template**:
能够重复生成同类工程起点，并包含必要环境、结构和最小验证的脚手架。
_Avoid_: Example Project, Boilerplate Folder

**Reference Source**:
通过 Git submodule 固定版本、用于阅读和分析的外部参考源码。
_Avoid_: Vendor Copy, Others
