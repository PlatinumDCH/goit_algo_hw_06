# def edit_phone(self, old_phone: str, new_phone: str) -> None:
#     if any(p.value == old_phone for p in self.phones):  # Проверяем, существует ли старый телефон
#         self.phones = [Phone(new_phone) if p.value == old_phone else p for p in self.phones]
#     else:
#         raise ValueError("Old phone not found")