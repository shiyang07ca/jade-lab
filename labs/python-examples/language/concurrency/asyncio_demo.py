"""
https://www.liujiangblog.com/course/python/83
"""

import inspect
import asyncio
import datetime


def simple_coroutine():
    print("-> 启动协程")
    y = 5
    x = yield y
    print("-> 协程接收到了x的值:", x)


def t_yield_send():
    my_coro = simple_coroutine()
    import pdb

    pdb.set_trace()
    ret = next(my_coro)
    import pdb

    pdb.set_trace()
    print(ret)
    my_coro.send(10)


# @asyncio.coroutine  # 声明一个协程
# def display_date(num, loop):
#     end_time = loop.time() + 10.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) >= end_time:
#             break
#         yield from asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果


async def display_date(num, loop):  # 注意这一行的写法
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果


def t_display_date():
    loop = asyncio.get_event_loop()  # 获取一个event_loop
    tasks = [display_date(1, loop), display_date(2, loop)]
    loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
    loop.close()


"""

asyncio的使用可分三步走：

- 创建事件循环
- 指定循环模式并运行
- 关闭循环

通常我们使用asyncio.get_event_loop()方法创建一个循环。

运行循环有两种方法：
一是调用run_until_complete()方法，
二是调用run_forever()方法。
run_until_complete()内置add_done_callback回调函数，run_forever()则可以自定义
add_done_callback()，具体差异请看下面两个例子。

使用run_until_complete()方法：
"""


async def func(future):
    await asyncio.sleep(1)
    future.set_result("Future is done!")


def call_result(future):
    print(future.result())
    asyncio.get_running_loop().stop()


def t_func1():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    print(loop.is_running())  # 查看当前状态时循环是否已经启动
    loop.run_until_complete(future)
    print(future.result())
    loop.close()


def t_func2():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func(future))
    future.add_done_callback(call_result)  # 注意这行
    try:
        loop.run_forever()
    finally:
        loop.close()


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def call_factorial():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


def main():
    # t_yield_send()

    # t_display_date()

    # t_func1()

    # t_func1()

    # Expected output:
    #
    #     Task A: Compute factorial(2), currently i=2...
    #     Task B: Compute factorial(3), currently i=2...
    #     Task C: Compute factorial(4), currently i=2...
    #     Task A: factorial(2) = 2
    #     Task B: Compute factorial(3), currently i=3...
    #     Task C: Compute factorial(4), currently i=3...
    #     Task B: factorial(3) = 6
    #     Task C: Compute factorial(4), currently i=4...
    #     Task C: factorial(4) = 24
    #     [2, 6, 24]
    asyncio.run(call_factorial())

    pass


if __name__ == "__main__":
    main()
