"""Measure request work with an injectable Prometheus Summary."""

from __future__ import annotations

import time
from collections.abc import Callable

from prometheus_client import CollectorRegistry, Summary, generate_latest


REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")


def create_request_timer(registry: CollectorRegistry) -> Summary:
    return Summary(
        "request_processing_seconds",
        "Time spent processing request",
        registry=registry,
    )


def process_request(
    delay: float,
    *,
    metric: Summary = REQUEST_TIME,
    sleeper: Callable[[float], None] = time.sleep,
    clock: Callable[[], float] = time.perf_counter,
) -> None:
    if delay < 0:
        raise ValueError("delay must be non-negative")

    started = clock()
    try:
        sleeper(delay)
    finally:
        metric.observe(clock() - started)


def render_demo() -> str:
    registry = CollectorRegistry()
    metric = create_request_timer(registry)
    process_request(0.001, metric=metric)
    return generate_latest(registry).decode("utf-8")


if __name__ == "__main__":
    print(render_demo(), end="")
