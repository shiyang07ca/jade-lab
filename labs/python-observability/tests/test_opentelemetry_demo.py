from opentelemetry.sdk.trace import TracerProvider

from opentelemetry_demo import add_open_telemetry_spans


def test_reports_no_span_outside_recording_context() -> None:
    event = add_open_telemetry_spans(None, "info", {"event": "outside"})

    assert event["span"] is None


def test_adds_fixed_width_trace_span_and_parent_ids() -> None:
    tracer = TracerProvider().get_tracer(__name__)

    with tracer.start_as_current_span("parent") as parent:
        with tracer.start_as_current_span("child"):
            event = add_open_telemetry_spans(None, "info", {"event": "inside"})

    span = event["span"]
    assert isinstance(span, dict)
    assert len(span["trace_id"]) == 32
    assert len(span["span_id"]) == 16
    assert span["parent_span_id"] == f"{parent.get_span_context().span_id:016x}"
