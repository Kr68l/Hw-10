from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record():
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, phone_index, new_phone):
        self.phones[phone_index] = new_phone

    def delete_phone(self, phone_index):
        del self.phones[phone_index]


class Field:
    def __init__(self, value=None):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)

    def __eq__(self, other):
        return self._value == other._value

    def __hash__(self):
        return hash(self._value)
        
    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    pass