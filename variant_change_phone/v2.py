# def edit_phone(self, old_phone: str, new_phone: str) -> None:
#     phone_to_edit = next((p for p in self.phones if p.value == old_phone), None)
#     if phone_to_edit:
#         phone_to_edit.value = new_phone
#     else:
#         raise ValueError("Old phone not found")