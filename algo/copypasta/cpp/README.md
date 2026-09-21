# C++ 竞赛算法手册

本目录平铺保存九个历史实现主题：图、二分查找、归并排序、快速排序、并查集、堆、链表、线段树和 Trie。
CMake 为每个 `.cpp` 建立独立目标，只确认代码能够按 C++17 编译；当前没有 C++ 行为测试，示例中的输出也不作为验收结果。

构建输出固定写入仓库的 `.scratch/build/copypasta-cpp`。从仓库根目录执行：

```sh
mise exec -- cmake --preset default -S algo/copypasta/cpp
mise exec -- cmake --build .scratch/build/copypasta-cpp
```
