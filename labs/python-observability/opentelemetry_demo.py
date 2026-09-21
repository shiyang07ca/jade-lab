"""Add the active OpenTelemetry span identifiers to a log event."""

from __future__ import annotations

from typing import Any

from opentelemetry import trace


def add_open_telemetry_spans(
    _logger: object,
    _method_name: str,
    event_dict: dict[str, Any],
) -> dict[str, Any]:
    span = trace.get_current_span()
    if not span.is_recording():
        event_dict["span"] = None
        return event_dict

    context = span.get_span_context()
    parent = getattr(span, "parent", None)
    event_dict["span"] = {
        "span_id": f"{context.span_id:016x}",
        "trace_id": f"{context.trace_id:032x}",
        "parent_span_id": None if parent is None else f"{parent.span_id:016x}",
    }
    return event_dict
