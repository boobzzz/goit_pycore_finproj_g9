from typing import List, Dict
from commands import Commands
from decorators import input_error, show_message
from session_handler import save_data, load_data
from note_book import NoteBook
from address import AddressParams, Params
import utils

address_book = load_data()
note_book = NoteBook()


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
            birthdays()
        case Commands.ADD_NOTE:
            add_note()
        case Commands.EDIT_NOTE:
            change_note(args)
        case Commands.DELETE_NOTE:
            delete_note(args)
        case Commands.SHOW_NOTES:
            show_notes(args)
            show_birthday(args)
        case Commands.BD_SOON:
            birthdays(args)
        case Commands.ADD_ADR:
            add_address(args)
        case Commands.CHANGE_ADR:
            change_address(args)


def save_session():
    save_data(address_book)


@show_message
def say_hello() -> str:
    return Commands.messages.get(Commands.HELLO)


@input_error
@show_message
def add_contact(args: List[str]) -> str:
    if len(args) < 1: return Commands.messages.get(Commands.INVALID_CMD)
    name, *rest = args
    record = address_book.find_record(name)
    message = Commands.messages.get(Commands.CHANGE)
    if not record:
        address_book.add_record(name)
        message = Commands.messages.get(Commands.ADD)
    if rest:
        record = address_book.find_record(name)
        error = record.add_phone(rest[0])
        if error:
            message = error
    return message


@input_error
@show_message
def change_contact(args: List[str]) -> str:
    if len(args) < 3: return Commands.messages.get(Commands.INVALID_CMD)
    name, phone, new_phone = args
    record = address_book.find_record(name)
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
    record = address_book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        address_book.delete_record(name)
        message = Commands.messages.get(Commands.DELETE)
    return message


@input_error
@show_message
def show_all_phones(args: List[str]) -> str:
    if len(args) < 1: return Commands.messages.get(Commands.INVALID_CMD)
    name = args[0]
    record = address_book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        message = record.phones
    return message


@show_message
def show_all_contacts() -> str:
    message = Commands.errors.get(Commands.EMPTY)
    if bool(address_book):
        message = str(address_book)
    return message


@input_error
@show_message
def add_birthday(args: List[str]) -> str:
    if len(args) < 2: return Commands.messages.get(Commands.INVALID_CMD)
    name, birthday = args
    record = address_book.find_record(name)
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
    record = address_book.find_record(name)
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
    if bool(address_book):
        message = ""
        for record in address_book.values():
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


@show_message
def add_address(args: List[str]) -> str:
    message = Commands.errors[Commands.NO_RECORD]
    if len(args) == 0:
        return message

    record = book.find_record(args[0])
    if not record:
        message = Commands.errors[Commands.NOT_FOUND]
        return message

    if record.address:
        message = Commands.errors[Commands.ADR_EXISTS]
        return message

    address_params: AddressParams = {
        Params.CITY: None,
        Params.STREET: None,
        Params.BUILDING: None
    }

    message = Commands.messages[Commands.ADD_ADR]
    while True:
        if address_params["city"] and address_params["street"] and address_params["building"]:
            record.update_address(address_params)
            break

        messages = get_messages(address_params)
        user_input = input(messages["message"])
        if user_input == Commands.QUIT:
            message = Commands.messages[Commands.QUIT_ADD]
            break

        if user_input:
            address_params[messages["param"]] = user_input
        else:
            print(messages["error"])
    return message


def get_messages(address_params: AddressParams) -> Dict:
    messages: Dict = {}
    if not address_params["city"]:
        messages["message"] = f"{Commands.messages[Commands.ADD_CITY]} ({Commands.messages[Commands.QUIT]}): "
        messages["error"] = Commands.errors[Commands.NO_CITY]
        messages["param"] = Params.CITY
    if address_params["city"] and not address_params["street"]:
        messages["message"] = f"{Commands.messages[Commands.ADD_STR]} ({Commands.messages[Commands.QUIT]}): "
        messages["error"] = Commands.errors[Commands.NO_STR]
        messages["param"] = Params.STREET
    if address_params["city"] and address_params["street"] and not address_params["building"]:
        messages["message"] = f"{Commands.messages[Commands.ADD_BLD]} ({Commands.messages[Commands.QUIT]}): "
        messages["error"] = Commands.errors[Commands.NO_BLD]
        messages["param"] = Params.BUILDING

    return messages


@show_message
def change_address(args: List[str]) -> str:
    message = Commands.errors[Commands.NO_RECORD]
    if len(args) == 0:
        return message

    record = book.find_record(args[0])
    if not record:
        message = Commands.errors[Commands.NOT_FOUND]
        return message

    address_params: AddressParams = {
        Params.CITY: record.address.city,
        Params.STREET: record.address.street,
        Params.BUILDING: record.address.building
    }

    update_messages = {
        Params.CITY: Commands.messages[Commands.UPD_CITY],
        Params.STREET: Commands.messages[Commands.UPD_STR],
        Params.BUILDING: Commands.messages[Commands.UPD_BLD],
    }

    message = Commands.messages[Commands.UPD_ADR]
    for param in address_params:
        user_input = input(f"{update_messages[param]} [{address_params[param]}] ({Commands.messages[Commands.QUIT]}, "
                           f"{Commands.messages[Commands.PROCEED]}): ")
        if user_input == Commands.QUIT:
            message = Commands.messages[Commands.QUIT_UPD]
            break

        if user_input:
            address_params[param] = user_input
            record.update_address(address_params)

    return message


@show_message
def add_note() -> str:
    note_params = {"title": "", "text": "", "tags": List[str]}

    messages = {
        "title": {
            "msg": Commands.messages[Commands.ENTER_TITLE],
            "err": Commands.errors[Commands.NO_TITLE],
            "type": "title"
        },
        "text": {
            "msg": Commands.messages[Commands.ENTER_TEXT],
            "err": Commands.errors[Commands.NO_TEXT],
            "type": "text"
        }
    }

    result = Commands.messages[Commands.ADD_NOTE]
    while True:
        if note_params["title"] and note_params["text"] and not note_book.find_note(note_params["title"]):
            tags_input = input(Commands.messages[Commands.ENTER_TAGS])
            note_params["tags"] = tags_input.split(",") if tags_input else None
            note_book.add_note(note_params["title"], note_params["text"], note_params["tags"])
            break

        message = messages["title"] if not note_params["title"] else messages["text"]
        user_input = input(message["msg"])
        if user_input == "q":
            result = "Quit adding note"
            break

        if user_input:
            note_params[message["type"]] = user_input
        else:
            print(message["err"])

    return result


@show_message
def change_note(args: List[str]) -> str:
    pass


@show_message
def delete_note(args: List[str]) -> str:
    message = Commands.errors[Commands.NOTE_NOT_FOUND]
    if len(args) > 0 and note_book.find_note(args[0]):
        note_book.remove_note(args[0])
        message = Commands.messages[Commands.DELETE_NOTE]
    return message


@show_message
def show_notes(args: List[str]) -> str:
    message = Commands.errors[Commands.NOTES_EMPTY]
    if bool(note_book):
        message = str(note_book)
    return message
