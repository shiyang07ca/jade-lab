from threading import Thread
from random import randint
from time import sleep

# Sleep a random number of seconds (between 1 and 5)

cnt = 0
lst = [1] * 20000000


def add():
    global cnt

    sleep(randint(1, 5) / 1000)
    for _ in range(100000):
        # cnt += 1
        cnt = cnt + 1
        # lst.append(1)
        lst.pop()


def test_thread():
    print(f"before: {cnt}")

    threads = []

    for i in range(100):
        t = Thread(target=add)
        t.start()
        # t.join()
        threads.append(t)

    for thread in threads:
        thread.join()

    print(f"after: {cnt}")
    print(f"after: {len(lst)}")


def test_lamda():
    from collections import defaultdict
    from functools import partial

    def factory(x):
        return x * 2

    my_dict = defaultdict(partial(factory, 2))
    my_dict[2]
    print(my_dict)
    my_dict[3] = 5
    print(my_dict)

    # dic = defaultdict(lambda: {'x': x, 'y': y})
    # for i in range(3):
    #     x = y = i
    #     dic[i]['q'] = 2
    # print(dic)

    # fn = lambda x, y: x + y
    # print(fn)
    # print(fn(2, 3))


def main():
    """ """

    # test_lamda()

    import config

    import ipdb

    ipdb.set_trace()


if __name__ == "__main__":
    main()
