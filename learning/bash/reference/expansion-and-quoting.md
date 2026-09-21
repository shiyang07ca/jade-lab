# 展开与引用速查

普通命令的参数位置默认引用变量展开：`printf '%s\n' "$value"`。先判断语法上下文，再判断参数如何形成。

## 参数形成

| 写法 | 行为 |
| --- | --- |
| `'literal $HOME'` | 保持字面内容，不能在单引号内部用反斜杠转义单引号 |
| `"$value"` | 展开值但不做单词分割或路径名展开；空值仍是一个空参数 |
| `$value` | 普通参数位置可能按 `IFS` 分割，再做路径名展开；空值可能消失 |
| `"$@"`、`"${items[@]}"` | 每个位置参数或数组元素保持独立，空集合产生零个参数 |
| `"$*"` | 按 `IFS` 首字符把位置参数连接为一个字符串 |
| `value=$(command)` | 赋值位置不做单词分割和路径名展开；命令替换删除末尾全部换行 |

`name=value` 的等号两边不能有空格。普通赋值右侧、算术上下文和 `[[ ... ]]` 不执行普通参数位置的
分割与路径名展开，但仍有各自语义：`[[ $value == $pattern ]]` 的右侧是模式，引用右侧则按字面匹配。
`local` 使用动态作用域；函数调用的其他函数也可能看到该局部变量。声明命令可能掩盖命令替换的退出状态，
需要检查状态时将声明和赋值分开。

## 常用参数展开

| 写法 | 含义 |
| --- | --- |
| `${name}`、`${name}_suffix` | 大括号界定变量名，不代替引用 |
| `${name:-word}` | 未设置或为空时使用 `word`，不赋值 |
| `${name:=word}` | 未设置或为空时赋值并使用 `word` |
| `${name:?message}` | 未设置或为空时向 stderr 报错，非交互 Shell 退出 |
| `${name:+word}` | 设置且非空时使用 `word`，否则为空 |
| `${#name}` | 字符串长度，字符解释受 locale 影响 |
| `${name#pattern}`、`${name##pattern}` | 删除开头最短、最长模式匹配 |
| `${name%pattern}`、`${name%%pattern}` | 删除末尾最短、最长模式匹配 |
| `${name/old/new}`、`${name//old/new}` | 替换第一个、全部模式匹配；不是正则表达式 |
| `${name:offset:length}` | 子串；负 offset 前留空格或使用括号，避免与 `:-` 混淆 |

默认值操作中的冒号表示同时检查“未设置”和“空”；省略冒号只检查“未设置”。

## 状态与身份

- `$?` 是上一条命令状态，后续命令会覆盖；`if command; then ...; else ...; fi` 可直接分支处理。
- `$!` 是最近后台作业的 PID，异步管道取最后一条命令的 PID；它不证明最终成功。
- `$$` 在 Bash 子 Shell 中仍保留原值；`BASHPID` 表示当前 Bash 进程。
- `$0` 是调用名称，不能据此定位被 source 的文件；`$#` 是位置参数数目，第十个及以后写 `${10}` 等。

依据：[Quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html)、
[Shell Expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) 和
[Shell Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)。
返回 [Bash 学习工作区](../README.md)。
