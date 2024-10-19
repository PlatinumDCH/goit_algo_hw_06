from collections import UserDict
from typing import Optional


class ValidatePhone(Exception):
    """Custom exception for invalid phone numbers."""

    pass


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field): ...


class Phone(Field):
    def __init__(self, value: str) -> None:
        if not value.isdigit() or len(value) != 10:
            raise ValidatePhone("Phone number must be 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phone: list[Phone] = []

    def add_phone(self, phone: str) -> None:
        self.phone.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.phone = [p for p in self.phone if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for p in self.phone:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError("Old phone not found")

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phone:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = ", ".join([str(phone) for phone in self.phone])
        return f"Contact name: {self.name}, Phones: {phones}"


class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
