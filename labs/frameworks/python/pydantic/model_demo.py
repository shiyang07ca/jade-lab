from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Self

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


@dataclass
class NetInfo:
    ip: str
    mac_addr: Optional[str] = None


def t_dataclass():
    ip = NetInfo(ip="a.b.c.d")
    print(ip, ip.__dict__)


def t1():
    class User(BaseModel):
        id: int
        name: str = "BBQ"
        signup_ts: Optional[datetime] = None
        friends: list[int] = []

    external_data = {
        "id": "123",
        # 'name': 'xxx',
        "signup_ts": "2021-09-02 17:00",
        "friends": [1, 2, "3"],
    }
    user = User(**external_data)

    print(user.id)
    # > 123
    print(repr(user.signup_ts))
    # > datetime.datetime(2021, 9, 2, 17, 0)
    print(user.friends)
    # > [1, 2, 3]
    print(user.model_dump())

    print(user.model_dump_json(), type(user.model_dump_json()))

    print(user.model_json_schema(), type(user.model_json_schema()))
    # print(user.schema_json(), type(user.schema_json()))

    """
    {
        'id': 123,
        'signup_ts': datetime.datetime(2021, 9, 2, 17, 0),
        'friends': [1, 2, 3],
        'name': 'John Doe',
    }
    """


def t2():
    from datetime import date
    from enum import Enum
    from uuid import UUID, uuid4

    class Department(Enum):
        HR = "HR"
        SALES = "SALES"
        IT = "IT"
        ENGINEERING = "ENGINEERING"

    class Employee(BaseModel):
        employee_id: UUID = Field(default_factory=uuid4, frozen=True)
        name: str = Field(min_length=1, frozen=True)
        email: EmailStr = Field(pattern=r".+@example\.com$")
        date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
        salary: float = Field(alias="compensation", gt=0, repr=False)
        department: Department
        elected_benefits: bool

        @field_validator("date_of_birth")
        @classmethod
        def check_valid_age(cls, date_of_birth: date) -> date:
            today = date.today()
            eighteen_years_ago = date(today.year - 18, today.month, today.day)

            if date_of_birth > eighteen_years_ago:
                raise ValueError("Employees must be at least 18 years old.")

            return date_of_birth

        @model_validator(mode="after")
        def check_it_benefits(self) -> Self:
            department = self.department
            elected_benefits = self.elected_benefits

            if department == Department.IT and elected_benefits:
                raise ValueError(
                    "IT employees are contractors and don't qualify for benefits"
                )
            return self

    # employee_data = {
    #     "name": "Clyde Harwell",
    #     "email": "charwell@example.com",
    #     "birth_date": "2020-06-12",
    #     "compensation": 100_000,
    #     "department": "ENGINEERING",
    #     "elected_benefits": True,
    # }

    # employee = Employee.model_validate(employee_data)
    # print(employee)

    new_employee = {
        "name": "Alexis Tau",
        "email": "ataue@example.com",
        "birth_date": "2001-04-12",
        "compensation": 100_000,
        "department": "IT",
        "elected_benefits": True,
    }
    print(new_employee)
    print(Employee.model_validate(new_employee))


def main():
    # t_dataclass()

    # t1()

    t2()
    pass


if __name__ == "__main__":
    main()
