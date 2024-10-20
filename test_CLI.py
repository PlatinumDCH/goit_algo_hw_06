import unittest

from collections import UserDict
from typing import Optional
from CLI_asistent import Record, Phone, AddressBook



class TestAddressBook(unittest.TestCase):
    
    def setUp(self) -> None:
        self.address_book = AddressBook()
        self.record = Record("John Doe")
        self.record.add_phone("1234567890")
        self.address_book.add_record(self.record)

    def test_add_record(self):
        self.assertIn("John Doe", self.address_book.data)
        self.assertEqual(len(self.address_book.data), 1)

    def test_find_record(self):
        found_record = self.address_book.find("John Doe")
        self.assertIsNotNone(found_record)
        self.assertEqual(found_record.name.value, "John Doe")

    def test_find_record_not_found(self):
        found_record = self.address_book.find("Jane Doe")
        self.assertIsNone(found_record)

    def test_add_phone(self):
        self.record.add_phone("0987654321")
        self.assertEqual(len(self.record.phone), 2)
        self.assertEqual(self.record.phone[1].value, "0987654321")

    def test_add_existing_phone(self):
        with self.assertRaises(ValueError) as e:
            self.record.add_phone("1234567890")
        self.assertEqual(str(e.exception), "Phone 1234567890 already exists in contact")

    def test_remove_phone(self):
        self.record.remove_phone("1234567890")
        self.assertEqual(len(self.record.phone), 0)

    def test_remove_phone_not_found(self):
        with self.assertRaises(ValueError) as e:
            self.record.remove_phone("1111111111")
        self.assertEqual(str(e.exception), "Phone not found")

    def test_edit_phone(self):
        self.record.edit_phone("1234567890", "0987654321")
        self.assertEqual(self.record.phone[0].value, "0987654321")

    def test_edit_phone_not_found(self):
        with self.assertRaises(ValueError) as e:
            self.record.edit_phone("1111111111", "0987654321")
        self.assertEqual(str(e.exception), "Old phone not found")

    def test_delete_record(self):
        self.address_book.delete("John Doe")
        self.assertNotIn("John Doe", self.address_book.data)

    def test_delete_record_not_found(self):
        self.address_book.delete("Jane Doe")
        self.assertEqual(len(self.address_book.data), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
