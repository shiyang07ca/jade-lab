from datetime import date

import pytest
from pydantic import ValidationError

from model_demo import Department, parse_employee


def valid_payload() -> dict[str, object]:
    return {
        "name": "Alex Tau",
        "email": "alex@example.com",
        "birth_date": "1990-04-12",
        "compensation": 100_000,
        "department": "engineering",
        "elected_benefits": True,
    }


def test_parses_aliases_and_domain_types() -> None:
    employee = parse_employee(valid_payload())

    assert employee.date_of_birth == date(1990, 4, 12)
    assert employee.department is Department.ENGINEERING
    assert employee.salary == 100_000


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("email", "alex@gmail.com", "string_pattern_mismatch"),
        ("birth_date", date.today().isoformat(), "at least 18"),
        ("compensation", 0, "greater_than"),
    ],
)
def test_rejects_invalid_boundary_values(field: str, value: object, message: str) -> None:
    payload = valid_payload()
    payload[field] = value

    with pytest.raises(ValidationError, match=message):
        parse_employee(payload)


def test_rejects_benefits_for_it_contractors() -> None:
    payload = valid_payload()
    payload["department"] = "it"

    with pytest.raises(ValidationError, match="not eligible for benefits"):
        parse_employee(payload)
