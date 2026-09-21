import pytest
from prometheus_client import CollectorRegistry

from prometheus_demo import create_request_timer, process_request


def test_records_one_request_with_controlled_elapsed_time() -> None:
    registry = CollectorRegistry()
    metric = create_request_timer(registry)
    times = iter([10.0, 10.25])
    sleeps: list[float] = []

    process_request(
        0.1,
        metric=metric,
        sleeper=sleeps.append,
        clock=lambda: next(times),
    )

    assert sleeps == [0.1]
    assert registry.get_sample_value("request_processing_seconds_count") == 1
    assert registry.get_sample_value("request_processing_seconds_sum") == pytest.approx(0.25)


def test_rejects_negative_delay_without_recording() -> None:
    registry = CollectorRegistry()
    metric = create_request_timer(registry)

    with pytest.raises(ValueError, match="non-negative"):
        process_request(-1, metric=metric)

    assert registry.get_sample_value("request_processing_seconds_count") == 0
