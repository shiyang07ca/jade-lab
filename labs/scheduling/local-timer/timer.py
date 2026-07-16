import time
import heapq
from collections import namedtuple
from itertools import count
import threading
from time import monotonic as _time
from abc import ABCMeta, abstractmethod


class Timer(metaclass=ABCMeta):
    def __init__(self):
        """Pass."""

    @abstractmethod
    def init_timer(
        self,
    ):
        """Pass."""

    @abstractmethod
    def add_entry(
        self,
    ):
        """Pass."""

    @abstractmethod
    def cancel_entry(
        self,
    ):
        """Pass."""

    @abstractmethod
    def expire_entry(
        self,
    ):
        """Pass."""

    @abstractmethod
    def entrys(self):
        """Pass."""


_sentinel = object()

Event = namedtuple("Event", "time, priority, sequence, action, argument, kwargs")


class HeapSched(Timer):
    def __init__(self, timefunc=_time, delayfunc=time.sleep):
        self._queue = []
        self.timefunc = timefunc
        self.delayfunc = delayfunc
        self._sequence_generator = count()

    def init_timer(self, timefunc=_time, delayfunc=time.sleep):
        return HeapSched(timefunc=_time, delayfunc=time.sleep)

    def add_entry(self, delay, priority, action, argument=(), kwargs=_sentinel):
        if kwargs is _sentinel:
            kwargs = {}

        time = self.timefunc() + delay
        event = Event(
            time, priority, next(self._sequence_generator), action, argument, kwargs
        )
        heapq.heappush(self._queue, event)

        return event

    def cancel_entry(self, event):
        """Pass."""
        self._queue.remove(event)
        heapq.heapify(self._queue)

    def expire_entry(self, blocking=True):
        """Pass."""
        q = self._queue
        delayfunc = self.delayfunc
        timefunc = self.timefunc
        pop = heapq.heappop
        while True:
            if not q:
                break
            (time, priority, sequence, action, argument, kwargs) = q[0]
            now = timefunc()
            if time > now:
                delay = True
            else:
                delay = False
                pop(q)
            if delay:
                if not blocking:
                    return time - now
                delayfunc(time - now)
            else:
                action(*argument, **kwargs)
                delayfunc(0)  # Let other threads run

    def entrys(self):
        """Pass."""


class TimeWheel(Timer):
    def init_timer(
        self,
    ):
        self._queue = []

    def add_entry(
        self,
    ):
        """Pass."""

    def cancel_entry(
        self,
    ):
        """Pass."""

    def expire_entry(
        self,
    ):
        """Pass."""

    def entrys(self):
        """Pass."""


import unittest


class TestHeapSched(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_entry(self):
        l = []
        fun = lambda x: l.append(x)
        hs = HeapSched.init_timer(time.time, time.sleep)
        for x in [0.5, 0.4, 0.3, 0.2, 0.1]:
            z = hs.add_entry(x, 1, fun, (x,))
        hs.expire_entry()
        self.assertEqual(l, [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_cancel(self):
        l = []
        fun = lambda x: l.append(x)
        hs = HeapSched.init_timer(time.time, time.sleep)
        now = time.time()
        event1 = hs.add_entry(0.01, 1, fun, (0.01,))
        event2 = hs.add_entry(0.02, 1, fun, (0.02,))
        event3 = hs.add_entry(0.03, 1, fun, (0.03,))
        event4 = hs.add_entry(0.04, 1, fun, (0.04,))
        event5 = hs.add_entry(0.05, 1, fun, (0.05,))
        hs.cancel_entry(event1)
        hs.cancel_entry(event5)
        hs.expire_entry()
        self.assertEqual(l, [0.02, 0.03, 0.04])

    def test_get_all_entry(self):
        pass


def main():
    import time
    from scheduler import scheduler

    s = scheduler(time.time, time.sleep)

    def print_time(a="default"):
        print("From print_time", time.time(), a)

    def print_some_times():
        print(time.time())
        s.enter(10, 1, print_time)
        s.enter(5, 2, print_time, argument=("positional",))
        s.enter(5, 1, print_time, kwargs={"a": "keyword"})
        s.run()
        print(time.time())

    def print_heap_timer():
        hs = HeapSched.init_timer(time.time, time.sleep)
        print(time.time())
        hs.add_entry(10, 1, print_time)
        hs.add_entry(5, 2, print_time, argument=("positional",))
        hs.add_entry(5, 1, print_time, kwargs={"a": "keyword"})
        hs.expire_entry()
        print(time.time())

    # print_some_times()
    print("================")
    # print_heap_timer()


if __name__ == "__main__":
    # main()

    unittest.main()
