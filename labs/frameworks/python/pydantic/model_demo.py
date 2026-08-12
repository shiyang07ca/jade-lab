"""Validate an employee payload at an HTTP or message-consumer boundary."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Self
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class Department(StrEnum):
    ENGINEERING = "engineering"
    IT = "it"
    SALES = "sales"


class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(pattern=r"^[^@]+@example\.com$")
    date_of_birth: date = Field(alias="birth_date")
    salary: float = Field(alias="compensation", gt=0)
    department: Department
    elected_benefits: bool

    @field_validator("date_of_birth")
    @classmethod
    def require_adult(cls, date_of_birth: date) -> date:
        today = date.today()
        age = today.year - date_of_birth.year
        if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
            age -= 1
        if age < 18:
            raise ValueError("employee must be at least 18 years old")
        return date_of_birth

    @model_validator(mode="after")
    def reject_it_benefits(self) -> Self:
        if self.department is Department.IT and self.elected_benefits:
            raise ValueError("IT contractors are not eligible for benefits")
        return self


def parse_employee(payload: dict[str, object]) -> Employee:
    """Parse untrusted boundary data or raise ``pydantic.ValidationError``."""
    return Employee.model_validate(payload)
