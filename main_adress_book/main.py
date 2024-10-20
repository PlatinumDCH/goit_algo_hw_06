from address_book import AddressBook
from record import Record

def main():
    book = AddressBook()
    record1 = Record("John")
    record1.add_phone("1234567890")
    record1.add_phone("9876543210")

    record2 = Record('Dima')
    record2.add_phone("0987654321")
    record2.add_phone("1234567890")

    book.add_record(record1)
    book.add_record(record2)

    book.delete('Dima')
    print(record1)
    print(book)

if __name__ == "__main__":
    main()
