import json
from collections import deque
from datetime import datetime
from enum import Enum
from time import sleep
from typing import Deque

from CountDownLatch import CountDownLatch
from decoder import RedBeatJSONDecoder, RedBeatJSONEncoder, to_timestamp
from redis import StrictRedis


class TIMEOUT_ST(Enum):
    ST_INIT = 0
    ST_EXPIRED = 1
    ST_CANCELLED = 2


class HashedWheelTimeout:
    def __init__(self):
        pass


class HashedWheelBucket:
    def __init__(self):
        pass


class HashedWheelTimer:
    timeouts: Deque[HashedWheelTimeout] = deque()

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass

    def newTimeout(self):
        pass


def get_redis():
    conn = StrictRedis.from_url("redis://127.0.0.1/0", decode_responses=True)
    return conn


from datetime import datetime, timedelta, tzinfo

from celery.schedules import schedule


def maybe_schedule(s: int | float | timedelta, relative: bool = False):
    """Return schedule from number, timedelta, or actual schedule."""
    if s is not None:
        if isinstance(s, (float, int)):
            s = timedelta(seconds=s)
        if isinstance(s, timedelta):
            return schedule(s, relative)
    return s


SCHEDULE_KEY_PREFIX = "timer::"

SCHEDULE_KEY = SCHEDULE_KEY_PREFIX + "schedule"


class RedTimerEntry:
    def __init__(
        self,
        name=None,
        task=None,
        schedule=None,
        args=None,
        kwargs=None,
        enabled=True,
        options=None,
        **clsargs,
    ):
        self.name = name
        self.task = task
        self.args = args
        self.kwargs = kwargs if kwargs else {}
        self.options = options if options else {}
        self.schedule = maybe_schedule(schedule)
        # TODO:
        # import ipdb
        # ipdb.set_trace()
        self.last_run_at = self.schedule.now()
        self.total_run_count = 0

        self.enabled = enabled

    @classmethod
    def from_key(cls, key):
        with get_redis().pipeline() as pipe:
            pipe.hget(key, "definition")
            pipe.hget(key, "meta")
            definition, meta = pipe.execute()

        if not definition:
            raise KeyError(key)

        definition = json.loads(definition, cls=RedBeatJSONDecoder)
        meta = json.loads(meta, cls=RedBeatJSONDecoder)
        definition.update(meta)

        entry = cls(**definition)
        entry.last_run_at = meta["last_run_at"]

        return entry

    @property
    def score(self):
        """return UTC based UNIX timestamp"""
        return to_timestamp(self.due_at)

    @property
    def due_at(self):
        # never run => due now
        if self.last_run_at is None:
            return self.schedule.now()

        delta = self.schedule.remaining_estimate(self.last_run_at)
        # if no delta, means no more events after the last_run_at.
        if delta is None:
            return None

        # overdue => due now
        if delta.total_seconds() < 0:
            return self.schedule.now()

        return self.last_run_at + delta

    def is_due(self):
        rem_delta = self.schedule.remaining_estimate(self.last_run_at)
        remaining_s = max(rem_delta.total_seconds(), 0)
        if remaining_s == 0:
            return True, 0
        else:
            return False, remaining_s

    @property
    def key(self):
        return SCHEDULE_KEY_PREFIX + self.name

    def save(self):
        definition = {
            "name": self.name,
            "task": self.task,
            "args": self.args,
            "kwargs": self.kwargs,
            "options": self.options,
            "schedule": self.schedule,
            "enabled": self.enabled,
        }
        meta = {
            "last_run_at": self.last_run_at,
        }
        with get_redis().pipeline() as pipe:
            pipe.hset(
                self.key, "definition", json.dumps(definition, cls=RedBeatJSONEncoder)
            )
            pipe.hsetnx(self.key, "meta", json.dumps(meta, cls=RedBeatJSONEncoder))
            pipe.zadd(SCHEDULE_KEY, {self.key: self.score})
            pipe.execute()

        return self


SCHEDULE_DICT = {
    "test_every_5_seconds": {
        "name": "test_every_5_seconds",
        "task": "test_every_5_seconds_task",
        "schedule": timedelta(seconds=5),
        "args": ["param1", "param2"],  # optional
        "kwargs": {"max_targets": 100},  # optional
        "enabled": True,  # optional
    }
}


# TODO: redis 分布式锁
class RedTimer:
    max_interval = 5

    def install_entries(self):
        for name, entry in SCHEDULE_DICT.items():
            try:
                entry = RedTimerEntry(**entry)
            except Exception as e:
                print("Add entry error", name, e)
                continue
            entry.save()
            print(f"Sotred entry: {entry}")

    def start(self):
        self.install_entries()

        pass

    def stop(self):
        """释放锁, 退出进程"""
        pass

    @property
    def schedule(self):
        print("Timer: Get tasks")

        client = get_redis()
        max_due_at = int(datetime.now().timestamp())
        with client.pipeline() as pipe:
            pipe.zrangebyscore(SCHEDULE_KEY, 0, max_due_at)
            pipe.zrangebyscore(
                SCHEDULE_KEY,
                "({}".format(max_due_at),
                max_due_at + RedTimer.max_interval,
                start=0,
                num=1,
            )

            due_tasks, maybe_due = pipe.execute()
        print(f"Loadding {len(due_tasks)} tasks, {due_tasks}, {maybe_due}")

        s = {}
        for key in due_tasks + maybe_due:
            try:
                entry = RedTimerEntry.from_key(key)
                print(f"entry: {entry}")
            except Exception as e:
                print("Add entry error", key, e)
                continue
            s[entry.name] = entry
        return s

    def tick(self):
        remaining_times = []
        try:
            for entry in self.schedule.values():
                is_due, next_time_to_run = entry.is_due()
                print(f"tick: {entry.name}, {is_due}, {next_time_to_run}")
                if is_due:
                    print(f"Call due task: {entry.name}")

                if next_time_to_run:
                    remaining_times.append(next_time_to_run)
        except Exception as e:
            print(f"An exception occurred {e}")
        return min(remaining_times + [RedTimer.max_interval])

    def newTimeout(self):
        pass

    ...


import unittest

from celery.utils.time import maybe_timedelta

# def testScheduleTimeoutShouldRunAfterDelay(self):
#     print('================ Timer test')
#     timer = HashedWheelTimer()
#     barrier = CountDownLatch(1)
#     # timeout = timer.newTimeout(barrier.count_down())
#     pass


class mocked_schedule(schedule):
    def __init__(self, remaining):
        self._remaining = maybe_timedelta(remaining)
        self.run_every = timedelta(seconds=1)
        self.nowfun = datetime.utcnow

    def remaining_estimate(self, last_run_at):
        return self._remaining


due_now = mocked_schedule(0)
due_next = mocked_schedule(1)


class ResTimerTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.s = RedTimer()

    # def testRedis(self):
    #     print("================ Test Timer Redis ================")
    #     client = get_redis()

    def testGetSchedule(self):
        schedule = RedTimer().schedule
        print(schedule)

    # def testTimerStart(self):
    #     RedTimer().start()

    def testTimerTick(self):
        entry = RedTimerEntry(
            name="next",
            task="test",
            schedule=due_next,
        )
        entry.save()

        sleep = self.s.tick()
        # print(f"sleep: {sleep}")


def main():
    print("main")


if __name__ == "__main__":
    # main()

    unittest.main()
