# Anki 待确认卡片：Mnemosyne

共 53 张卡。确认后只同步 `approved` 卡片。
检查时先只看 Front/Text：你应该能看出它在说哪种技术或哪篇资料、正在解决什么事情，以及只需要回答哪一个问题。确认后再看答案和来源。

## 学习目标

为看懂、调试和维护服务部署脚本建立 Bash 核心心智模型——能够识别退出码、重定向、管道、变量展开、控制流、函数、文本处理、错误处理、进程生命周期、API/JSON 边界和部署模式，并能验证脚本的真实执行路径。

## approved（51）

### bash-2026-07-22-001

**Front**

在 Bash 中，检查刚执行命令是否成功时，退出码如何解释，应从哪里读取？

**Back**

退出码 0 表示成功，非 0 表示失败；最近一次前台命令的退出状态保存在特殊参数 `$?` 中。

**Extra**

if、&&、||、set -e 等控制流都会利用这个约定。`$?` 会被下一条命令的退出状态覆盖，因此需要及时读取。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0001-how-shell-executes-commands §4
- 为什么值得记：退出码是 Bash 控制流的基石，部署脚本中无处不在。理解这一点是读懂任何脚本的前提。
- 标签：ai_generated, codex, date_2026_07_22, bash, exit-code

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-002

**Front**

为什么 Bash 的 `cd` 必须是 Shell builtin，而不能依赖外部程序？

**Back**

外部命令通常在子进程中运行，只能改变自己的当前工作目录，无法改变父 Shell；`cd` 必须直接更新当前 Shell 的状态，所以由 Shell 作为 builtin 实现。

**Extra**

这是「子进程无法修改父进程状态」的经典例子。以 `./script.sh` 执行脚本时，脚本中的 `cd` 只影响脚本进程；用 `source script.sh` 在当前 Shell 中执行时，才会影响当前目录。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0001-how-shell-executes-commands §3
- 为什么值得记：fork/exec 模型能解释 Bash 中大量「反直觉」行为——cd 为何是 builtin、变量为何不跨脚本传递、后台进程为何独立。属于一旦理解就不需要死记硬背的元知识。
- 标签：ai_generated, codex, date_2026_07_22, bash, process-model

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-003

**Front**

在 Bash 的重定向语境中，stdin、stdout 和 stderr 分别对应哪个文件描述符？

**Back**

stdin = fd 0，stdout = fd 1，stderr = fd 2。

**Extra**

默认 stdin 连键盘，stdout 和 stderr 连终端。重定向就是改变这些 fd 的指向；例如 `2>&1` 将 fd 2 指向 fd 1 当前的目标。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0001-how-shell-executes-commands §5
- 为什么值得记：文件描述符编号是所有重定向语法的基础。不记住 0/1/2 就无法理解 2>&1、1>&2 等写法。
- 标签：ai_generated, codex, date_2026_07_22, bash, file-descriptors

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-004

**Front**

为什么 Bash 中 `cmd > file 2>&1` 能把 stdout 与 stderr 都写入文件，而 `cmd 2>&1 > file` 通常不能？

**Back**

前者先把 fd 1 指向 `file`，再让 fd 2 复制 fd 1 当时的目标，所以两者都进文件；后者先让 fd 2 指向 fd 1 的原目标（通常是终端），再改 fd 1，stderr 仍去原目标。重定向按从左到右处理。

**Extra**

部署脚本常写成 `cmd >> log 2>&1`：先追加 stdout，再把 stderr 合并到同一目标。顺序写反会让错误输出留在原目标，导致日志缺少关键信息。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0003-pipes-and-redirections §2
- 为什么值得记：2>&1 顺序陷阱是部署脚本中最常见的错误之一，也是阅读脚本时最容易误解的写法。属于高频实用知识。
- 标签：ai_generated, codex, date_2026_07_22, bash, redirection

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-005

**Front**

在 Bash 中，如何根据右侧连接对象区分 `|` 与 `>`？

**Back**

`|` 把左侧命令的 stdout 接到右侧命令的 stdin，用来组合命令；`>` 把命令的 stdout 写入文件（通常覆盖）。因此两者右侧分别是命令和文件路径。

**Extra**

例如 `grep ERROR log | wc -l` 把数据交给下一个命令；`grep ERROR log > errors.txt` 则把结果持久化。需要追加时使用 `>>`。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0003-pipes-and-redirections §5-§6
- 为什么值得记：管道是 Bash 区别于其他编程语言的核心特征。区分管道和重定向是写出正确命令的前提。
- 标签：ai_generated, codex, date_2026_07_22, bash, pipe, redirection

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-006

**Front**

在 Bash 部署脚本中，`/dev/null` 的语义是什么，为什么常写 `cmd > /dev/null 2>&1`？

**Back**

`/dev/null` 是特殊设备：写入即丢弃，读取立即得到 EOF。`cmd > /dev/null 2>&1` 把 stdout 和 stderr 都丢弃，但仍可通过命令退出码判断成功或失败。

**Extra**

若只写 `curl -s URL > /dev/null`，stderr 仍会显示；只有明确不需要错误信息时才把 stderr 也合并到 `/dev/null`。调试阶段应保留日志或错误输出。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0003-pipes-and-redirections §3
- 为什么值得记：部署脚本中频繁出现 /dev/null，不理解它就是看天书。
- 标签：ai_generated, codex, date_2026_07_22, bash, devnull

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-007

**Front**

在 Bash 部署脚本中，为什么 `./deploy.sh 2>&1 | tee deploy.log` 能同时显示并保存输出？

**Back**

`2>&1` 先把 stderr 合并到 stdout，`tee` 再把管道输入同时写到 `deploy.log` 和自己的 stdout，因此屏幕和文件都收到输出；`tee -a` 表示追加。

**Extra**

`2>&1` 必须写在管道前，否则 stderr 不会进入 `tee`。本卡只覆盖输出复制；部署脚本还要单独确认管道的失败状态不会被日志命令掩盖。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0003-pipes-and-redirections §7
- 为什么值得记：tee 是部署脚本中日志记录的标配用法，边看边存的需求非常普遍。
- 标签：ai_generated, codex, date_2026_07_22, bash, tee

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-008

**Front**

在 Bash 部署脚本中，什么时候应选择 `mkdir -p a/b/c` 而不是 `mkdir a/b/c`？

**Back**

`mkdir -p` 会创建缺失的父目录，并且目标目录已存在时不报错；普通 `mkdir` 要求父目录已存在，目标已存在也会报错。需要让目录存在且脚本可重复执行时使用 `-p`。

**Extra**

`-p` 不能绕过权限不足，也不能把路径中的普通文件变成目录；它表达的是「目标目录存在即可，重复执行也应成功」。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0002-file-system-operations §4
- 为什么值得记：部署脚本中频繁出现，且体现了脚本编写的一个重要原则——幂等性和对环境的最小假设。
- 标签：ai_generated, codex, date_2026_07_22, bash, mkdir

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-009

**Front**

看到 Bash 命令 `chmod 755 script.sh` 或 `chmod 600 secret.key` 时，如何解读三个数字？

**Back**

三位分别对应 owner、group、other；每位由读 `r`=4、写 `w`=2、执行 `x`=1 相加。755 = `rwxr-xr-x`，600 = `rw-------`。

**Extra**

这些数字描述权限，不代表所有脚本都应设为 755 或所有密钥都恰好设为 600；应按最小权限和实际运行需求设置。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0002-file-system-operations §6
- 为什么值得记：chmod 数字是日常使用中的高频操作，也是看到 755/644/600 这些数字时能理解其含义的基础。
- 标签：ai_generated, codex, date_2026_07_22, bash, permissions

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-011

**Front**

在 Bash 部署脚本中看到 `rm -rf "$DIR"` 时，执行前必须确认哪些安全条件？

**Back**

它会强制递归删除且不可恢复。`DIR` 必须非空、已验证为预期范围内的路径，并拒绝 `/`、`.`、`..` 等危险目标；始终引用变量，可用 `rm -rf -- "$DIR"` 防止路径被当作选项。

**Extra**

仅检查 `[[ -n "$DIR" ]]` 不足以保证安全；不能把未验证的外部输入直接传给 `rm`。能用 `rm -r`、先列出确认或采用可恢复的清理方式时，应优先考虑。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0002-file-system-operations §4
- 为什么值得记：高失败代价的安全知识。写错一次可能造成不可逆的数据损失。属于必须主动回忆而非「用到时再查」的知识。
- 标签：ai_generated, codex, date_2026_07_22, bash, rm, safety

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-013

**Front**

在 Bash 中，为什么在当前目录执行脚本通常写 `./script.sh`，而不是 `script.sh`？

**Back**

`PATH` 是冒号分隔的目录列表。不含 `/` 的命令名会按顺序搜索它；当当前目录不在 `$PATH` 时，`script.sh` 找不到。`./script.sh` 含 `/`，明确从当前目录执行，前提是文件有执行权限。

**Extra**

如果把 `.` 放进 `PATH`，裸写脚本名有时也能工作，但可能受 PATH 顺序影响；显式 `./` 更清楚，也避免意外执行 PATH 中同名程序。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0001-how-shell-executes-commands §2
- 为什么值得记：解释了初学者最常见的困惑——为什么一定要加 ./。背后有安全设计原则。
- 标签：ai_generated, codex, date_2026_07_22, bash, path

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-014

**Front**

若 `APP=myapp`、`VERSION=v2`，Bash 会如何解析 `$APP_$VERSION`，以至于结果只有 `v2`？

**Back**

Bash 把 `APP_` 解析成完整变量名，而它未定义；应写 `${APP}_$VERSION`，用花括号明确第一个变量名的边界。

**Extra**

当变量名后紧跟字母、数字或下划线时，花括号用于消除变量名边界歧义。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0004-variables-quoting-expansion §3
- 为什么值得记：组合路径、版本号和文件名时很常见；错误展开会产生静默的空值或错误路径。
- 标签：ai_generated, codex, date_2026_07_27, bash, parameter-expansion

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-015

**Front**

在 Bash 部署脚本中，为什么路径变量通常写成 `cd "$APP_DIR"`，而不是 `cd $APP_DIR`？

**Back**

`"$APP_DIR"` 把展开结果作为一个参数；无引号时会发生单词分割和路径名展开，可能变成零个或多个参数。

**Extra**

尤其当变量为空时，`cd $APP_DIR` 可能退化为无参数的 `cd` 并进入主目录，而 `cd "$APP_DIR"` 会以空路径失败。除非明确需要分割或通配，默认引用变量。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0004-variables-quoting-expansion §4
- 为什么值得记：未引用的路径变量是部署脚本中高频且代价较高的 bug 来源。
- 标签：ai_generated, codex, date_2026_07_27, bash, quoting

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-016

**Front**

在 Bash 部署脚本中，`TIMESTAMP=$(date +%Y%m%d_%H%M%S)` 里的 `$(...)` 做了什么？

**Back**

Bash 先执行括号内的命令，再用它的 stdout 替换 `$(...)`，因此 `TIMESTAMP` 得到时间戳字符串。

**Extra**

命令替换会删除输出末尾的换行。`$(...)` 比旧式反引号更易读、易嵌套；需要判断内部命令是否成功时，还要检查退出状态。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0004-variables-quoting-expansion §5; manual:Bash Reference Manual §3.5.4 Command Substitution
- 为什么值得记：时间戳、路径和命令结果在部署脚本中经常需要从 stdout 转成字符串。
- 标签：ai_generated, codex, date_2026_07_27, bash, command-substitution

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-017

**Front**

在 Bash 包装脚本或函数中，把参数原样逐个转发时，为什么应写 `"$@"` 而不是 `"$*"`？

**Back**

`"$@"` 将每个原始参数保留为一个独立参数；`"$*"` 把全部参数合并成一个字符串。

**Extra**

例如参数 `a`、`b c`、`d` 经 `"$@"` 仍是三个参数；`"$*"` 默认用空格（准确说是 `$IFS` 的首字符）连接成一个参数。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0004-variables-quoting-expansion §6; manual:Bash Reference Manual §3.4.2 Special Parameters
- 为什么值得记：参数原样传递是脚本包装器、部署入口和函数复用中的高频边界。
- 标签：ai_generated, codex, date_2026_07_27, bash, positional-parameters

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-018

**Front**

在 Bash 控制流中，为什么 `if grep -q "ERROR" app.log; then` 可以直接作为条件？

**Back**

`if` 直接执行 `grep` 并检查退出码：0 进入 `then`，任何非 0 进入 `else`；不需要先构造布尔值。

**Extra**

对 `grep`，0 表示匹配，1 表示无匹配，2 通常表示读取或用法错误；简单的 `if/else` 会把后两者都放进 `else`。`-q` 只抑制匹配输出。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0005-control-flow §1; manual:grep(1) EXIT STATUS
- 为什么值得记：这是从其他语言迁移到 Bash 时最重要的思维转换，也是部署前置检查的基本模式。
- 标签：ai_generated, codex, date_2026_07_27, bash, control-flow

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-019

**Front**

在明确以 Bash 运行的脚本中，为什么通常优先用 `[[ $A = "$B" ]]` 而不是 `[ "$A" = "$B" ]`？

**Back**

`[[ ]]` 中变量值不会触发单词分割或路径名展开，并原生支持 `&&`、`||` 和 `=~`；`[ ]` 的优势是兼容 POSIX shell。

**Extra**

`[[ ]]` 不是 POSIX 语法；需要由 `sh`、`dash` 等运行时应使用 `[ ]` 等可移植写法。两种写法中的空格都具有语法意义。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0005-control-flow §2
- 为什么值得记：选择测试语法会直接影响部署脚本的可读性、兼容性和对空值的安全处理。
- 标签：ai_generated, codex, date_2026_07_27, bash, tests

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-021

**Front**

在 Bash 部署脚本中，`until curl --fail --silent --show-error URL; do sleep 2; done` 会在什么条件下继续和停止？

**Back**

`curl` 返回非 0 时继续重试，返回 0 时停止；`until` 的循环条件与 `while` 相反。

**Extra**

`--fail` 让 HTTP 4xx/5xx 成为失败；只有 `-s` 时，这些 HTTP 响应仍可能返回 0。实际部署还应限制尝试次数或总时长，并给单次请求设置超时，避免无限等待。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0005-control-flow §5; manual:curl(1) --fail
- 为什么值得记：等待服务就绪是部署脚本的典型场景，`until` 的反向条件很容易读反。
- 标签：ai_generated, codex, date_2026_07_27, bash, loops, deployment

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-022

**Front**

在 Bash `case` 分支中，应如何解释 `*.tar.gz)`，为什么不能按正则表达式读取？

**Back**

`case` 使用 shell 的 Glob 模式而非正则；`*.tar.gz` 表示任意字符串后接字面量 `.tar.gz`。

**Extra**

`case` 中的 `|` 表示多个 Glob 模式的或，例如 `restart|reload)`。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0005-control-flow §6
- 为什么值得记：Glob 与正则的混淆会让环境分支、文件类型分支悄悄匹配错误。
- 标签：ai_generated, codex, date_2026_07_27, bash, case, glob

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-023

**Front**

为什么 Bash 中的 `A && B || C` 不能无条件当作 `if A; then B; else C; fi`？

**Back**

只要 `A` 失败，或 `A` 成功但 `B` 失败，`C` 都会执行；只有 `A`、`B` 均成功才跳过 `C`。

**Extra**

当 `B` 本身可能失败且两种失败需要不同处理时，应写完整的 `if`，不要把短路表达式当成可靠的三元运算符。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0005-control-flow §7
- 为什么值得记：这是 Bash 中很常见的控制流陷阱，可能把中间步骤的失败误报成另一条分支。
- 标签：ai_generated, codex, date_2026_07_27, bash, control-flow, short-circuit

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-024

**Front**

若 Bash 脚本自己的 `$1` 是 `production`，随后调用 `deploy staging v2.0`，函数 `deploy` 内的 `$1` 是什么？

**Back**

函数内 `$1` 是调用时传入的第一个参数 `staging`。

**Extra**

调用函数时，传入的参数会临时成为函数的位置参数；函数结束后，脚本级 `$1` 恢复为 `production`。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0006-functions-and-script-structure §2
- 为什么值得记：区分脚本级与函数级位置参数，是阅读嵌套部署函数和参数转发的关键。
- 标签：ai_generated, codex, date_2026_07_27, bash, functions, positional-parameters

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-025

**Front**

为什么 Bash 函数内部的临时变量应声明为 `local`？

**Back**

未声明 `local` 的赋值可能覆盖调用者的同名变量；`local` 可避免函数意外改写外部脚本状态。

**Extra**

Bash 的 `local` 是动态作用域：变量在当前函数返回前有效，当前函数调用的其他函数也可能看见它；它不是严格的词法封装。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0006-functions-and-script-structure §3; manual:Bash Reference Manual §3.4 Shell Parameters
- 为什么值得记：变量泄漏是 Bash 函数中高频且隐蔽的 bug 来源，会污染后续部署步骤。
- 标签：ai_generated, codex, date_2026_07_27, bash, functions, scope

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-026

**Front**

在 Bash 函数中，为保留 `some_command` 的退出状态，应将 `local result=$(some_command)` 改成什么写法？

**Back**

`$?` 得到的是 `local` 的状态，可能掩盖命令替换的失败；应先 `local result`，再单独执行 `result=$(some_command)` 并立即检查状态。

**Extra**

ShellCheck 将这种声明与赋值合写的问题标为 SC2155。若只需把命令状态交给调用者，也可直接在 `if` 中执行命令，或让它成为函数最后一条命令。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0006-functions-and-script-structure §3
- 为什么值得记：这是维护 Bash 函数时容易忽略的退出码陷阱，直接关系到错误处理是否可靠。
- 标签：ai_generated, codex, date_2026_07_27, bash, functions, exit-code

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-027

**Front**

当 Bash 调用者用 `result=$(get_value)` 接收函数数据时，为什么函数的日志不能也写到 stdout？

**Back**

命令替换会捕获函数的全部 stdout；日志会和数据混在一起，污染 `result`。应让 stdout 只承载数据，把日志写到 stderr。

**Extra**

函数的成功或失败应通过退出码传递。若 `do_backup` 先向 stdout 写日志、再输出备份路径，`backup_file=$(do_backup)` 会把两行都捕获；应让 `log` 写 stderr，或改用其他数据传递方式。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0006-functions-and-script-structure §4–§5
- 为什么值得记：区分状态通道与数据通道，是设计可组合函数和可靠部署流程的核心判断。
- 标签：ai_generated, codex, date_2026_07_27, bash, functions, return-values

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-029

**Front**

在 Bash 中，`. lib/utils.sh` 与 `./lib/utils.sh` 对当前 Shell 状态的影响有何不同？

**Back**

`.`/`source` 在当前 Shell 中执行，变量、函数和目录变更可以保留；`./...` 在独立进程中执行，结束后不能把这些状态改回调用者。

**Extra**

函数库和环境设置常用 `source`，独立程序常用直接执行。`./lib/utils.sh` 通常还要求执行权限和有效的 shebang；`bash lib/utils.sh` 则不要求文件本身可执行。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0006-functions-and-script-structure §6
- 为什么值得记：执行与引入的区别决定变量、函数和目录变化是否能影响调用者，是读脚本时的关键分叉。
- 标签：ai_generated, codex, date_2026_07_27, bash, source, process-model

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-27-030

**Front**

在 Bash 中，`echo '$USER $(date)'` 与 `echo "$USER $(date)"` 的展开行为有何不同？

**Back**

单引号中的内容完全按字面保留；双引号允许变量展开和命令替换，但抑制单词分割与路径名展开。

**Extra**

引号是 Shell 的解析语法，处理后会被移除；外部命令收到的是展开后的参数，而不是原始引号。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0004-variables-quoting-expansion §1、§4
- 为什么值得记：单引号与双引号的区别是读懂变量、命令替换和命令参数边界的基础，且原草稿未直接考查这一核心规则。
- 标签：ai_generated, codex, date_2026_07_27, bash, quoting, expansion

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-032

**Front**

在 `sed` 替换命令中，`s/old/new/` 与 `s/old/new/g` 的关键差异是什么？

**Back**

前者每行只替换第一个匹配；后者用 `g` 替换该行的所有匹配。

**Extra**

`g` 的作用范围是每一行中的匹配，不是把文件当成一个整体只处理一次。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0007-text-processing-trio §2
- 为什么值得记：误把默认替换当成全局替换，会让配置文件只改掉部分目标值。
- 标签：ai_generated, codex, date_2026_08_04, bash, sed

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-033

**Front**

在 Bash 配置修改脚本中，`sed 's/port=80/port=8080/' config.ini` 与 `sed -i 's/port=80/port=8080/' config.ini` 的文件效果有何不同？

**Back**

不带 `-i` 只把修改后的内容输出到 stdout，不改原文件；`-i` 原地修改文件，也可用 `-i.bak` 先保留备份。

**Extra**

跨 macOS/BSD 与 GNU sed 编写脚本时要确认 `-i` 参数语法；原地修改前也应评估备份和回滚需要。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0007-text-processing-trio §2
- 为什么值得记：区分 stdout 输出和原地修改，能避免“看起来改了但文件没变”以及误改配置的事故。
- 标签：ai_generated, codex, date_2026_08_04, bash, sed, file-editing

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-034

**Front**

在 Bash 日志分析中，`awk -F: '{print $NF}'` 里的 `-F:` 与 `$NF` 分别表示什么？

**Back**

`-F:` 指定冒号为字段分隔符；`$NF` 表示当前行的最后一列。

**Extra**

`$0` 是整行，`$1` 是第一列；`-F` 让 awk 能按日志或 `/etc/passwd` 等实际格式切分。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0007-text-processing-trio §3
- 为什么值得记：字段引用和分隔符是部署脚本中 awk 提取日志、用户或磁盘信息的核心语义。
- 标签：ai_generated, codex, date_2026_08_04, bash, awk

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-035

**Front**

经典日志管道中，为什么 `awk '{print $1}' | sort | uniq -c` 要先 `sort` 再 `uniq -c`？

**Back**

`uniq` 只合并相邻的重复行；先排序让相同值相邻，才能统计完整的出现次数。

**Extra**

统计后再用 `sort -rn` 按次数降序排列，最后用 `head` 取 Top N。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0007-text-processing-trio §4
- 为什么值得记：理解 `sort` 与 `uniq -c` 的前置关系，才能正确阅读和构造日志统计管道。
- 标签：ai_generated, codex, date_2026_08_04, bash, awk, pipeline

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-036

**Front**

在 Bash 开启 `set -e` 后，为什么 `if grep 'ERROR' app.log; then` 中的 `grep` 失败通常不会让脚本退出？

**Back**

`if`、`while`、`until` 的条件命令属于显式测试场景；`set -e` 对这些条件失败有例外。

**Extra**

`set -e` 也有管道和 `&&`/`||` 相关例外，因此它不是“任何非零退出码都立即退出”的绝对保证。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0008-error-handling-and-debugging §2
- 为什么值得记：部署脚本同时使用测试条件和严格模式时，理解例外规则是避免误判的关键。
- 标签：ai_generated, codex, date_2026_08_04, bash, error-handling, set-e

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-037

**Front**

在 Bash `set -u` 的配置处理中，`${VAR:-default}` 与 `${VAR-default}` 有什么区别？

**Back**

`${VAR:-default}`：变量未设置或为空字符串时使用 `default`；`${VAR-default}`：只有变量未设置时使用 `default`，变量已设置但为空时保留空字符串。

**Extra**

未设置时两种写法都用默认值；非空时两种写法都保留原值。空字符串是否等价于缺失，决定应选带冒号还是不带冒号的形式。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0008-error-handling-and-debugging §3
- 为什么值得记：这是严格模式下处理可选配置的稳定边界，能防止变量拼写错误和空配置静默传播。
- 标签：ai_generated, codex, date_2026_08_04, bash, set-u, parameter-expansion

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-038

**Front**

在 Bash 管道 `cat huge.log | grep 'ERROR' | wc -l` 中，为什么 `cat` 失败时管道默认仍可能返回 0？

**Back**

默认管道退出码取最后一个命令 `wc -l` 的状态；开启 `set -o pipefail` 后，任一环节失败都会使管道失败。

**Extra**

`pipefail` 让上游读取失败不会被下游成功退出码掩盖，是日志处理和部署检查的重要防护。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0008-error-handling-and-debugging §4
- 为什么值得记：管道吞掉上游失败是部署脚本中隐蔽且高代价的错误来源。
- 标签：ai_generated, codex, date_2026_08_04, bash, pipefail, error-handling

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-039

**Front**

在 Bash 部署脚本中，为什么用 `trap cleanup EXIT` 清理临时目录或锁文件？

**Back**

`EXIT` trap 会在脚本退出时自动执行 cleanup，覆盖正常结束、`exit` 和 `set -e` 触发等路径，比在每个退出点手写清理更可靠。

**Extra**

`SIGKILL`（`kill -9`）无法被捕获，因此 EXIT trap 不是所有进程终止方式下都能执行。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0008-error-handling-and-debugging §6
- 为什么值得记：统一退出清理是临时文件、锁文件和资源回收的高频可靠性模式。
- 标签：ai_generated, codex, date_2026_08_04, bash, trap, cleanup

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-040

**Front**

怀疑 Bash 部署脚本的变量展开或执行顺序异常时，`bash -x deploy.sh` 能帮助你看到什么？

**Back**

它把 Bash 实际执行的每条命令及其展开后的参数输出到 stderr，便于逐行追踪；脚本内也可用 `set -x`/`set +x` 局部开关。

**Extra**

追踪输出默认走 stderr，可用 `bash -x deploy.sh 2>debug.log` 保存后分析。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0008-error-handling-and-debugging §7
- 为什么值得记：`bash -x` 是阅读陌生脚本和定位展开/顺序问题的直接调试入口。
- 标签：ai_generated, codex, date_2026_08_04, bash, debugging, set-x

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-041

**Front**

在严格模式 Bash 脚本中，什么时候用 `cmd || die "msg"`，什么时候用 `cmd || true`？

**Back**

关键命令失败应终止脚本并报错用 `|| die`；明确允许失败且不应影响后续流程时才用 `|| true`。

**Extra**

`|| true` 会主动掩盖失败，只能用于有明确恢复或忽略语义的可选步骤。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0008-error-handling-and-debugging §8–§9
- 为什么值得记：这是把严格模式转成业务级失败策略的核心判断，直接影响部署是否会带错继续。
- 标签：ai_generated, codex, date_2026_08_04, bash, error-handling, short-circuit

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-042

**Front**

部署脚本为什么用 `flock -n` 获取锁，而不是先 `[ -f lock ]` 再 `touch lock`？

**Back**

`flock` 是操作系统级原子加锁，可避免两个进程同时通过检查的竞态；`-n` 表示非阻塞，拿不到锁立即失败。

**Extra**

常见写法是先用 `exec 200>"$LOCK_FILE"` 打开文件描述符，再执行 `flock -n 200`，并在 EXIT 时清理资源。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0009-deployment-patterns §2
- 为什么值得记：手动检查加 touch 存在竞态条件，可能让两个部署同时修改同一环境；这是高失败代价的并发防护。
- 标签：ai_generated, codex, date_2026_08_04, bash, deployment, locking

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-043

**Front**

为什么部署脚本更新配置时常用 `mktemp` 写临时文件，再用同一文件系统上的 `mv` 替换目标？

**Back**

写入过程在临时文件中完成，`mv` 原子替换目录项；中途失败不会把目标文件留在半写状态，只会保留旧文件或未完成的临时文件。

**Extra**

原子性依赖临时文件与目标位于同一文件系统；临时文件失败路径仍需清理。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0009-deployment-patterns §4
- 为什么值得记：直接覆盖配置可能留下半个文件；临时写入再替换是部署配置的通用可靠性模式。
- 标签：ai_generated, codex, date_2026_08_04, bash, deployment, atomic-write

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-04-044

**Front**

在版本化部署中，`current -> releases/v2.0` 符号链接为什么有利于切换和回滚？

**Back**

服务始终通过 `current` 指向当前版本；切换只需原子更新链接，回滚只需把链接改回旧版本，旧版本目录仍完整保留。

**Extra**

典型切换命令是 `ln -sfn "$release_dir" "$current_link"`；旧版本保留也便于排查。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0009-deployment-patterns §8
- 为什么值得记：符号链接把版本切换和回滚从复制大量文件简化为切换一个指针，是部署架构中的高价值设计。
- 标签：ai_generated, codex, date_2026_08_04, bash, deployment, symlink

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-045

**Front**

部署脚本把三台主机的健康检查并行放到后台，并需要汇总每台结果。为什么不能只用 `wait "$p1" "$p2" "$p3"` 判断哪一台失败？

**Back**

`wait id...` 会等待列出的任务，但最终只返回最后一个 `id` 的退出状态；前面任务的失败可能被覆盖。每次执行 `cmd &` 后应立刻保存 `$!`，再逐个 `wait "$pid"` 并记录该任务的状态。

**Extra**

在 `set -e` 脚本中可写 `if wait "$pid"; then rc=0; else rc=$?; fi`，既避免意外退出，也能把状态与任务名称对应起来。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0010-process-management §2；GNU Bash Reference Manual: Special Parameters、Job Control Builtins (`wait`)
- 为什么值得记：并行部署或健康检查必须知道具体失败项；误把最后一个任务的状态当成整体状态会产生静默漏报。
- 标签：ai_generated, codex, date_2026_08_11, bash, process, wait, exit-code

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-046

**Front**

脚本想统计命令输出的行数，并在循环后使用 `count`。为什么 `count=0; printf '%s\n' a b | while read -r _; do count=$((count + 1)); done; echo "$count"` 通常打印 `0`，应如何改写？

**Back**

Bash 通常让管道的每个阶段在各自的子 shell 中运行，循环修改的是子 shell 的 `count`。让循环在当前 shell 中读取进程替换即可：`while IFS= read -r _; do count=$((count + 1)); done < <(printf '%s\n' a b)`。

**Extra**

启用 `lastpipe` 且关闭 job control 时，Bash 可以让管道最后一段在当前 shell 运行；脚本不应默认依赖这个非默认设置。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0010-process-management §3；GNU Bash Reference Manual: Pipelines、The Shopt Builtin (`lastpipe`)
- 为什么值得记：管道子 shell 会让循环中的计数、数组追加和状态标记在循环结束后消失，是数据处理脚本中的高频隐蔽错误。
- 标签：ai_generated, codex, date_2026_08_11, bash, process, pipeline, subshell

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-047

**Front**

部署函数需要进入 `$release_dir` 运行构建，但不能改变调用者的当前目录。为什么 `(cd "$release_dir" && build)` 比 `{ cd "$release_dir" && build; }` 更符合目标？

**Back**

圆括号组在子 shell 中执行，`cd` 和其他 shell 状态修改在组结束后不会影响调用者；花括号组在当前 shell 中执行，目录变化会保留下来。

**Extra**

使用 `cd ... && build` 很重要：如果进入目录失败，就不能在错误目录中继续构建。圆括号组的退出状态是组内最后执行命令的状态。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0010-process-management §3；GNU Bash Reference Manual: Grouping Commands
- 为什么值得记：临时切换目录是构建和部署函数的常见需求；理解两种分组的状态边界可避免污染调用者环境。
- 标签：ai_generated, codex, date_2026_08_11, bash, process, subshell, working-directory

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-048

**Front**

停止后台服务时，为什么通常应先发送 `SIGTERM`、等待限定时间，仍未退出才发送 `SIGKILL`？

**Back**

`SIGTERM` 可被程序捕获和处理，使其有机会停止接收请求、刷盘并清理资源；`SIGKILL` 不能被捕获、阻塞或忽略，会立即终止进程，所以只适合作为超时后的最后手段。

**Extra**

对脚本直接创建的子进程，发送信号后还应 `wait "$pid"` 回收并取得最终状态。优先使用信号名而不是数字，可读性和可移植性更好。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0010-process-management §4–§5；GNU C Library Manual: Termination Signals
- 为什么值得记：终止策略直接影响数据完整性和服务恢复；需要理解优雅退出与强制终止的不可替代差异。
- 标签：ai_generated, codex, date_2026_08_11, bash, process, signal, shutdown

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-049

**Front**

PID 文件存在且 `kill -0 "$pid"` 成功，为什么仍不能证明该 PID 就是目标服务？

**Back**

`kill -0` 不发送信号，只检查该 PID 是否存在且当前用户是否有权限；PID 文件可能陈旧，而操作系统会复用 PID，因此它可能指向另一个进程。

**Extra**

优先交给服务管理器跟踪进程身份。Linux 上检查可执行文件、启动时间等只能降低误判，检查与发送信号之间仍有竞态；使用 pidfd 的工具才能避免 PID 复用竞态。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0010-process-management §7；Linux man-pages: kill(2)；Linux kernel procfs documentation
- 为什么值得记：依据陈旧 PID 文件终止进程可能误杀无关服务，失败代价高；这是自制守护脚本必须理解的身份问题。
- 标签：ai_generated, codex, date_2026_08_11, bash, process, pid-file, race-condition

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-050

**Front**

部署脚本从 Release API 的 `response.json`（内容为 `{"version":"v1.2.3"}`）提取版本号，用于比较和拼接发布路径。为什么 `version=$(jq '.version' response.json)` 不合适？

**Back**

默认输出仍是 JSON，字符串包含双引号；变量得到的是 `"v1.2.3"`。使用 `jq -r '.version' response.json` 输出供文本工具和 Bash 使用的原始字符串 `v1.2.3`。

**Extra**

`-r` 只改变字符串的输出格式，不验证字段是否存在或类型是否正确。需要验证时可用 `jq -er '.version | strings' response.json`。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0011-json-api-curl-jq §2；jq Manual: `--raw-output`、`--exit-status`
- 为什么值得记：JSON 字符串与 shell 文本的边界很容易产生肉眼不明显的引号错误，直接影响版本比较、URL 和文件路径。
- 标签：ai_generated, codex, date_2026_08_11, bash, json, jq, raw-output

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-051

**Front**

部署脚本要把可能含双引号、反斜杠或换行的 Bash 变量 `$msg` 放进 webhook 请求体的 `text` 字段。应如何安全构造 JSON？

**Back**

shell 字符串拼接不会按 JSON 规则转义数据，可能生成无效 JSON 或改变字段结构。应写 `payload=$(jq -n --arg text "$msg" '{text: $text}')`，让 jq 把变量作为字符串并正确编码。

**Extra**

jq 程序使用单引号，避免 shell 展开其中的 `$text`。需要传入数字、布尔值或对象时才使用 `--argjson`，且传入内容必须本身是合法 JSON。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0011-json-api-curl-jq §3；jq Manual: `--null-input`、`--arg`、`--argjson`
- 为什么值得记：手工拼 JSON 会在真实通知内容出现特殊字符时失效；让 JSON 工具负责编码是稳定且可迁移的边界处理原则。
- 标签：ai_generated, codex, date_2026_08_11, bash, json, jq, escaping

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-052

**Front**

健康检查 API 的 `response.json` 含 `.ready` 字段，脚本用 `jq -e '.ready' response.json` 决定是否进入成功分支。退出状态 `0`、`1`、`4` 分别表示什么？

**Back**

最后一个输出值既不是 `false` 也不是 `null` 时返回 `0`；最后一个输出值是 `false` 或 `null` 时返回 `1`；没有产生有效结果时返回 `4`。

**Extra**

jq 中只有 `false` 和 `null` 为假，`0`、空字符串、空数组和空对象都为真。不要把所有非 0 都当成业务 false；应保留 stderr，并区分无结果、解析或程序错误。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0011-json-api-curl-jq §2；jq Manual: `--exit-status`
- 为什么值得记：教材对 `jq -e` 的无结果状态有简化；准确区分状态能避免把数据缺失或解析失败误判为正常的业务假值。
- 标签：ai_generated, codex, date_2026_08_11, bash, json, jq, exit-code

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-054

**Front**

接手一个由许多函数组成的部署脚本时，为什么应先找 `main "$@"` 或其他顶层入口，再深入每个函数的实现？

**Back**

函数定义只注册函数体，不会执行其中命令；入口及顶层命令才决定实际调用顺序和可达代码。从入口追踪调用，可先确认正常路径、分支、外部副作用和失败处理。

**Extra**

先记录脚本解释器、严格模式、输入来源和顶层命令；再沿关心的调用路径查命令参数，能避免在未调用的辅助函数上过早消耗时间。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0012-reading-and-debugging-scripts §2–§3；GNU Bash Reference Manual: Shell Functions
- 为什么值得记：陌生脚本阅读的关键产出是实际执行路径和副作用，而不是记住文件排版；这一方法能直接提高审查效率。
- 标签：ai_generated, codex, date_2026_08_11, bash, reading, control-flow

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-055

**Front**

脚本末尾无条件执行 `main "$@"` 时，怎样改造入口，才能在 `source deploy.sh` 测试函数时不执行 `main`？

**Back**

`source` 会在当前 shell 中执行整个文件，因此加载函数后还会立即执行 `main`。应把入口放进守卫：`if [[ ${BASH_SOURCE[0]} == "$0" ]]; then main "$@"; fi`。

**Extra**

直接执行脚本时，`${BASH_SOURCE[0]}` 与 `$0` 指向同一脚本；被 source 时，前者仍是该文件，后者是调用者。这个守卫是 Bash 写法。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0012-reading-and-debugging-scripts §5；GNU Bash Reference Manual: Bourne Shell Builtins (`source`)、Bash Variables (`BASH_SOURCE`)
- 为什么值得记：教材建议 source 后手工调用函数，但示例脚本会无条件执行入口；入口守卫是实现可测试脚本的必要边界。
- 标签：ai_generated, codex, date_2026_08_11, bash, testing, source, entry-point

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-056

**Front**

在 Bash 数据库迁移脚本中，`applied.txt` 每行记录一个已执行的迁移文件名。怎样用 `grep` 检查 `$name`，避免 `1.sql` 被 `11.sql` 的记录误判为已执行？

**Back**

使用 `grep -Fqx -- "$name" applied.txt`。`-F` 按字面匹配，`-x` 要求匹配整行，因此 `1.sql` 不会匹配 `11.sql`。

**Extra**

`-q` 不输出匹配行，只用退出状态表示是否找到；`--` 结束选项解析，防止以 `-` 开头的名称被当成选项。前提是记录已规范化为一行一个非空文件名。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：file:learning/bash/lessons/0012-reading-and-debugging-scripts.html §6；GNU grep 3.12 Manual: https://www.gnu.org/s/grep/manual/grep.html (`-F`、`-x`、`-q`)
- 为什么值得记：迁移脚本会据此决定是否跳过文件；子串误判会导致迁移漏执行。
- 标签：ai_generated, codex, date_2026_08_11, bash, grep, exact-match, migration

确认：`approved` / `needs_review` / `rejected`

### bash-2026-08-11-057

**Front**

调试会处理令牌或密码的 Bash 脚本时，使用 `set -x` / `bash -x` 有什么泄露风险？

**Back**

`set -x` / `bash -x` 会打印变量展开后的命令，可能把 secret 写入终端或日志。

**Extra**

在处理 secret 前关闭 xtrace，或使用明确脱敏的调试输出；`2>trace.log` 只会改变泄露位置。

**卡片信息**

- 类型：`basic`
- 优先级：`1`
- 来源：lesson:0012-reading-and-debugging-scripts §5；GNU Bash Reference Manual: The Set Builtin (`-x`)
- 为什么值得记：xtrace 会输出展开后的值；需要记住这一条高风险边界，避免调试时泄露凭证。
- 标签：ai_generated, codex, date_2026_08_11, bash, debugging, xtrace, secrets

确认：`approved` / `needs_review` / `rejected`

## needs_review（0）

## draft（0）

## rejected（2）

### bash-2026-07-22-010

**Front**

在 Bash 中，`tail` 与 `tail -f` 对日志文件的行为有何不同，何时使用 `tail -f`？

**Back**

`tail` 输出当前文件末尾（默认 10 行）后退出；`tail -f` 输出末尾后持续等待并显示追加内容，适合实时观察日志，按 Ctrl+C 停止。

**Extra**

部署或排查服务时，可在一个终端运行 `tail -f /var/log/app.log`，再触发请求观察日志变化。日志轮转等更复杂场景另行学习 `tail -F`。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0002-file-system-operations §3
- 为什么值得记：日志分析是用户三大目标之一，tail -f 是日志分析的第一工具。
- 标签：ai_generated, codex, date_2026_07_22, bash, tail

确认：`approved` / `needs_review` / `rejected`

### bash-2026-07-22-012

**Front**

在 Bash 中，如何根据退出码区分 `cmdA && cmdB` 与 `cmdA || cmdB`？

**Back**

`cmdA && cmdB` 仅在 `cmdA` 返回 0（成功）时执行 `cmdB`；`cmdA || cmdB` 仅在 `cmdA` 返回非 0（失败）时执行。两者都按短路逻辑执行。

**Extra**

常见模式：make && ./deploy（编译成功才部署），make || exit 1（编译失败则退出），cmd || true（强制返回成功，常用于 set -e 环境中忽略某个命令的失败）。

**卡片信息**

- 类型：`basic`
- 优先级：`2`
- 来源：lesson:0001-how-shell-executes-commands §4
- 为什么值得记：部署脚本中频繁使用 && 串接步骤、|| 处理失败，是读脚本的基本语法单元。
- 标签：ai_generated, codex, date_2026_07_22, bash, control-flow

确认：`approved` / `needs_review` / `rejected`

## rejected_candidates（仅供审查）

1. which 命令用于查找可执行文件在 PATH 中的位置
   - 拒绝原因：低价值细节，使用时随手 which 即可，不值得占用记忆空间。
   - 来源：lesson:0001 §2
2. ls 的 -l, -a, -h, -t, -r 等选项
   - 拒绝原因：属于查阅类知识，man ls 或 ls --help 随时可查，不需要主动回忆。
   - 来源：lesson:0002 §1
3. cd - 回到上一个目录
   - 拒绝原因：过于简单，一次使用即可记住，不需要制卡。
   - 来源：lesson:0002 §2
4. file 命令用于识别文件类型
   - 拒绝原因：按需检索即可，不属于需要主动回忆的核心知识。
   - 来源：lesson:0002 §7
5. head 命令显示文件前若干行
   - 拒绝原因：tail 的对偶命令，理解了 tail 自然懂得 head，不值得单独制卡。
   - 来源：lesson:0002 §3
6. 输入重定向 < 的用法
   - 拒绝原因：使用频率远低于管道和输出重定向，且大部分命令直接接受文件名参数，无需通过 < 重定向 stdin。
   - 来源：lesson:0003 §4
7. 变量赋值时等号两边不能有空格
   - 拒绝原因：这是需要理解的基础语法，但规则短且报错后容易定位；本批优先把记忆空间留给更容易误判的展开、控制流和函数边界。
   - 来源：lesson:0004-variables-quoting-expansion §2
8. 第 4 课预告的 `${VAR:-default}`、`${VAR:=default}` 等参数展开变体
   - 拒绝原因：教材只做了存在性预告，尚未形成完整练习和边界理解；等专门学习参数展开后再制卡，避免把未充分理解的语法固化。
   - 来源：lesson:0004-variables-quoting-expansion §8
9. `for f in *.log` 没有匹配文件时得到字面量通配符，以及 `nullglob` 的开关细节
   - 拒绝原因：这是重要但偏边界的文件批处理陷阱，本批先保留 `for` 的主语义；在学习文件批处理或 `shopt` 时再单独复习。
   - 来源：lesson:0005-control-flow §4
10. `for item in ...` 会遍历展开后的词列表
   - 拒绝原因：语义正确，但完成练习后可直接从语法识别，单独主动回忆的收益较低；以后遇到真实文件遍历需求时，更值得为无匹配 Glob、空白文件名等失败模式制卡。
   - 来源：lesson:0005-control-flow §4
11. 成熟部署脚本的六层骨架清单
   - 拒绝原因：完整清单更适合作为速查模板，不适合一次性主动回忆六个条目；卡片只保留其中可独立判断的入口、作用域和返回机制。
   - 来源：lesson:0006-functions-and-script-structure §5
12. `function name {}` 与 `name() {}` 的具体写法差异
   - 拒绝原因：两种写法都能完成函数定义，精确语法可按需查阅；更值得长期记忆的是参数、作用域和返回通道。
   - 来源：lesson:0006-functions-and-script-structure §1
13. `main "$@"` 中双引号用于原样转发脚本参数
   - 拒绝原因：与保留的 `"$@"` 对比卡和函数位置参数卡重复；单独保留会增加复习负担，却没有增加新的判断能力。
   - 来源：lesson:0006-functions-and-script-structure §2、§5
14. grep 的 `-i`、`-v`、`-r`、`-n`、`-c` 等选项清单
   - 拒绝原因：属于查阅类细节；本批保留工具选择和管道语义，具体选项可在使用时查 `grep --help`。
   - 来源：lesson:0007-text-processing-trio §1
15. grep 的 Perl 正则 `-P` 及不同系统支持情况
   - 拒绝原因：平台支持不一致且当前课程只需理解三种正则口味；具体兼容性应在目标环境验证，不适合固化为通用卡片。
   - 来源：lesson:0007-text-processing-trio §1
16. sed 的行范围、删除匹配行、追加文本等高级命令
   - 拒绝原因：课程明确将这些标为“需要时再查”；它们不是本阶段部署脚本中最稳定的主动回忆点。
   - 来源：lesson:0007-text-processing-trio §2
17. awk 的完整语言能力：变量、循环、函数和数组
   - 拒绝原因：超出本课程的部署脚本目标；当前只保留字段提取、分隔符和管道统计的高频模式。
   - 来源：lesson:0007-text-processing-trio §3
18. `IFS=$'\n\t'` 的所谓严格模式变体
   - 拒绝原因：全局修改 IFS 会改变多处拆分语义，不是固定错误选项组合的一部分；应在具体 `read` 或拆分位置局部设置。
   - 来源：lesson:0008-error-handling-and-debugging §5
19. `ERR`、`INT`、`TERM` 的 trap 信号清单
   - 拒绝原因：把多个信号名称堆在一张卡中会变成裸列表；本批先保留更通用、可迁移的 `EXIT` 清理机制。
   - 来源：lesson:0008-error-handling-and-debugging §6
20. 第 9 课的八种部署模式完整清单
   - 拒绝原因：这是速查摘要，不适合一次性主动回忆；本批只制卡其中具有明确失败模式或设计取舍的部分。
   - 来源：lesson:0009-deployment-patterns §1–§8
21. 结构化日志的时间戳、级别、tee 和 stderr 全部细节
   - 拒绝原因：已有卡片覆盖 `tee`、stdout/stderr 数据通道和函数日志输出；再次制卡会造成重复。
   - 来源：lesson:0009-deployment-patterns §1
22. 通知 webhook 的 JSON 模板替换与平台格式
   - 拒绝原因：课程示例明确提示第 11 课会用 jq 深入处理 JSON；当前先不固化临时字符串替换方案。
   - 来源：lesson:0009-deployment-patterns §6
23. 部署目录布局中 releases、backups、config、logs、shared 的完整目录清单
   - 拒绝原因：目录名是项目约定，完整清单更适合作为模板查阅；本批保留符号链接切换这一可迁移设计。
   - 来源：lesson:0009-deployment-patterns §8
24. 用 `grep` 筛选 ERROR 日志行时应选择 grep
   - 拒绝原因：问题只考工具职责的直接映射，过于浅显；在真实命令上下文中可由语义和管道结构判断，主动回忆收益不足。
   - 来源：lesson:0007-text-processing-trio §1–§3
25. 第 9 课示例中环境变量、配置文件和默认值的固定优先级
   - 拒绝原因：这是单个课程示例的配置约定，不是 Bash 的通用语义；只背顺序没有形成可迁移的设计判断，且问题过于浅。
   - 来源：lesson:0009-deployment-patterns §7
26. 第 9 课示例中用 ROLLBACK_NEEDED 配合 trap EXIT 的具体编排
   - 拒绝原因：问题过度绑定示例变量名和实现步骤，且与 `trap EXIT` 清理卡、备份/回滚模式重复；不值得单独占用一张卡。
   - 来源：lesson:0009-deployment-patterns §5
27. `jobs`、`fg`、`bg`、`nohup`、`disown` 的命令和选项清单
   - 拒绝原因：大部分是交互式 job control 或按需查询的工具细节；生产服务应由服务管理器管理。`disown` 也不是把进程改成真正脱离父子关系，照搬教材表述会固化错误模型。
   - 来源：lesson:0010-process-management §6
28. SIGTERM=15、SIGKILL=9 等信号编号
   - 拒绝原因：脚本应优先使用信号名；背编号没有增加终止策略的判断能力，且完整编号表属于速查信息。
   - 来源：lesson:0010-process-management §4
29. 用后台命令、sleep 和 kill 手写 `timeout` 的完整模板
   - 拒绝原因：模板包含 PID 复用、子进程树和竞态等边界，容易形成虚假的可靠性；保留 TERM→限定等待→KILL 的设计判断，具体实现优先使用目标环境的成熟工具。
   - 来源：lesson:0010-process-management §7
30. curl 的 `-s`、`-f`、`-X`、`-H`、`-d`、`--max-time` 参数清单
   - 拒绝原因：参数表适合查阅，且现有健康检查卡已覆盖 `--fail`、错误显示和超时；本批只保留总轮询期限与单次请求期限的设计区别。
   - 来源：lesson:0011-json-api-curl-jq §1
31. jq 最常用表达式的完整速查表
   - 拒绝原因：字段索引、数组索引、length、keys 等语法可随用随查；本批只保留 shell/JSON 边界和退出状态这些容易造成错误判断的语义。
   - 来源：lesson:0011-json-api-curl-jq §4
32. 为 `curl | jq` 再制作一张通用 `pipefail` 卡
   - 拒绝原因：现有卡片已覆盖管道默认只看末段状态以及 `pipefail` 的作用；更换为 API 示例不会增加新的回忆点，只会重复复习。
   - 来源：lesson:0011-json-api-curl-jq §3
33. 按固定次数和分钟数背诵陌生脚本的四遍阅读法
   - 拒绝原因：遍数和时间是教学组织方式，不是稳定原理；保留从入口追踪真实执行路径这一可迁移方法即可。
   - 来源：lesson:0012-reading-and-debugging-scripts §1–§4
34. 运行 `shellcheck deploy.sh` 这一单独操作
   - 拒绝原因：命令本身过于直接，且 ShellCheck 规则可按诊断结果查阅；单独制卡不能训练对脚本行为或失败模式的判断。
   - 来源：lesson:0012-reading-and-debugging-scripts §5
35. `get_applied` 查询失败后用 `|| echo ""` 返回空列表
   - 拒绝原因：这个写法会把数据库失败伪装成“没有已执行迁移”，但其核心判断已由现有 `cmd || die` 与 `cmd || true` 卡覆盖；不再重复制卡。
   - 来源：lesson:0012-reading-and-debugging-scripts §6
36. 直接 `source deploy.sh` 后手工调用函数，且假定不会执行 main
   - 拒绝原因：示例脚本末尾无条件调用 `main "$@"`，该假定不成立；已改为入口守卫卡，避免把错误调试步骤写进卡片。
   - 来源：lesson:0012-reading-and-debugging-scripts §5–§6
37. 轮询部署 API 时区分成功、失败终态并设置总截止时间
   - 拒绝原因：用户判定为常识，主动回忆收益不足，明确要求删除，不占用复习次数。
   - 来源：lesson:0011-json-api-curl-jq §3
