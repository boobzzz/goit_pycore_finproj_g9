from typing import List
from commands import Commands
from decorators import input_error, show_message
from session_handler import save_data, load_data
import utils

book = load_data()


def get_response(cmd: str, args: List):
    match cmd:
        case Commands.HELLO:
            say_hello()
        case Commands.ADD:
            add_contact(args)
        case Commands.CHANGE:
            change_contact(args)
        case Commands.DELETE:
            delete_contact(args)
        case Commands.PHONE:
            show_all_phones(args)
        case Commands.ALL:
            show_all_contacts()
        case Commands.ADD_BD:
            add_birthday(args)
        case Commands.SHOW_BD:
            show_birthday(args)
        case Commands.BD_SOON:
            birthdays(args)


def save_session():
    save_data(book)


@show_message
def say_hello() -> str:
    return Commands.messages.get(Commands.HELLO)


@input_error
@show_message
def add_contact(args: List[str]) -> str:
    if len(args) < 2: return Commands.messages.get(Commands.INVALID_CMD)
    name, *rest = args
    record = book.find_record(name)
    message = Commands.messages.get(Commands.CHANGE)
    if not record:
        book.add_record(name)
        message = Commands.messages.get(Commands.ADD)
    if rest:
        record = book.find_record(name)
        error = record.add_phone(rest[0])
        if error:
            message = error
    return message


@input_error
@show_message
def change_contact(args: List[str]) -> str:
    if len(args) < 3: return Commands.messages.get(Commands.INVALID_CMD)
    name, phone, new_phone = args
    record = book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        error = record.edit_phone(phone, new_phone)
        if not error:
            message = Commands.messages.get(Commands.CHANGE)
        else:
            message = error
    return message


@input_error
@show_message
def delete_contact(args: List[str]) -> str:
    if len(args) < 1: return Commands.messages.get(Commands.INVALID_CMD)
    name = args[0]
    record = book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        book.delete_record(name)
        message = Commands.messages.get(Commands.DELETE)
    return message


@input_error
@show_message
def show_all_phones(args: List[str]) -> str:
    if len(args) < 1: return Commands.messages.get(Commands.INVALID_CMD)
    name = args[0]
    record = book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        message = record.phones
    return message


@show_message
def show_all_contacts() -> str:
    message = Commands.errors.get(Commands.EMPTY)
    if bool(book):
        message = str(book)
    return message


@input_error
@show_message
def add_birthday(args: List[str]) -> str:
    if len(args) < 2: return Commands.messages.get(Commands.INVALID_CMD)
    name, birthday = args
    record = book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        record.add_birthday(birthday)
        message = Commands.messages.get(Commands.CHANGE)
    return message


@input_error
@show_message
def show_birthday(args: List[str]) -> str:
    if len(args) < 1: return Commands.messages.get(Commands.INVALID_CMD)
    name = args[0]
    record = book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        if record.birthday is None: return message
        message = record.birthday.bd_date.date()
    return message


@show_message
def birthdays(args: List[str]) -> str:
    delta = None
    if len(args) >= 1:
        try:
            delta = int(args[0])
        except:
            return Commands.messages.get(Commands.INVALID_CMD)
    message = Commands.errors.get(Commands.EMPTY)
    bd_entries = []
    if bool(book):
        message = ""
        for record in book.values():
            record_bd_now = utils.is_bd_in_range(record, delta)
            if record_bd_now:
                dates = utils.get_congrats_date(record_bd_now)
                entry = {
                    "name": record.name,
                    "congrats_date": dates[0],
                    "birthday": dates[1]
                }
                bd_entries.append(entry)
        bd_entries.sort(key=lambda e: e["congrats_date"])

        for entry in bd_entries:
            if entry["congrats_date"] == entry["birthday"]:
                message += f"{entry["name"]}: {entry["congrats_date"].date()}\n"
            else:
                message += f"{entry["name"]}: {entry["congrats_date"].date()} (birthday @ {entry["birthday"].date()})\n"

    return message
