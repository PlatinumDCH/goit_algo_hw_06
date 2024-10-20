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
        self.phones: list[Phone] = []

    def add_phone(self, phone: str) -> None:
        '''add phone, if phone not in contact'''
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise ValueError(f"Phone {phone} already exists in contact")

    def remove_phone(self, phone: str) -> None:
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError('Phone not found')

    def edit_phone(self, old_phone: str, new_phone: str):
    try:
        new_phone_obj = Phone(new_phone)
    except ValidatePhone:
        raise ValueError("New phone number is invalid")

    for index, p in enumerate(self.phones):
        if p.value == old_phone:
            self.phones[index] = new_phone_obj
            return
    raise ValueError("Old phone not found")

    def find_phone(self, phone: str) -> Optional[Phone]:
        if not self.phones:
            return None
        for p in self.phones:
            if p.value == phone:
                return p
        return None 

    def __str__(self):
        phones = ", ".join([str(phone) for phone in self.phones])
        return f"Contact name: {self.name}, Phones: {phones}"


class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name,None)

    def delete(self, name: str) -> None:
        self.data.pop(name, None)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
