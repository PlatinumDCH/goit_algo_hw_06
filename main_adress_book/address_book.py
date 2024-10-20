from collections import UserDict
from record import Record
from typing import Optional

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def find(self, name)->Oprional[Record]:
        return self.data.get(name)
    
    def delete(self, name:str):
        record = self.data.pop(name, None)
        if record:
            del record

    def delete_and_cleanup(self, name: str) -> None:
        record = self.data.pop(name, None)
        if record:
            record.name = None
            record.phones = None
            del record  
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
