import threading


class CountDownLatch:
    def __init__(self, count=1):
        self.count = count
        self.lock = threading.Semaphore(count)

    def wait(self):
        self.lock.acquire()
        self.lock.release()

    def count_down(self):
        if self.count > 0:
            self.count -= 1
            if self.count == 0:
                self.lock.release()


# 使用示例
def worker(latch):
    # 执行一些操作
    print("Worker running")
    latch.count_down()


if __name__ == "__main__":
    latch = CountDownLatch(3)

    for i in range(3):
        t = threading.Thread(target=worker, args=(latch,))
        t.start()

    latch.wait()
    print("All workers completed")
