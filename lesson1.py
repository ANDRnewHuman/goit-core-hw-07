from datetime import datetime, timedelta

class Field:
    pass

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number. Please enter a 10-digit number.")
        self.value = value

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

class AddressBook:
    def __init__(self):
        self.records = []
    
    def add_record(self, record):
        self.records.append(record)
    
    def find(self, name):
        for record in self.records:
            if record.name.value.lower() == name.lower():
                return record
        return None

def get_upcoming_birthdays(book):
    today = datetime.today()
    upcoming_birthdays = []
    for record in book.records:
        if record.birthday:
            birthday_this_year = record.birthday.value.replace(year=today.year)
            if birthday_this_year >= today and birthday_this_year <= today + timedelta(days=7):
                upcoming_birthdays.append((record.name.value, birthday_this_year))
    return upcoming_birthdays

def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact '{name}' not found."

def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    elif record:
        return f"{name} doesn't have a birthday set."
    else:
        return f"Contact '{name}' not found."

def birthdays(args, book):
    upcoming_birthdays = get_upcoming_birthdays(book)
    if upcoming_birthdays:
        message = "Upcoming birthdays:\n"
        for name, birthday in upcoming_birthdays:
            message += f"{name}: {birthday.strftime('%d.%m.%Y')}\n"
        return message.strip()
    else:
        return "No upcoming birthdays in the next week."

def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
