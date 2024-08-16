from typing import List, Dict
from commands import Commands
from decorators import input_error, show_message
from session_handler import save_data, load_data
from address import AddressParams, Params
from boterror import BotError
import utils

loaded_data = load_data()
address_book = loaded_data["address_book"]
note_book = loaded_data["note_book"]


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
        case Commands.ADD_ADR:
            add_address(args)
        case Commands.CHANGE_ADR:
            change_address(args)
        case Commands.ADD_NOTE:
            add_note()
        case Commands.CHANGE_NOTE:
            change_note(args)
        case Commands.DELETE_NOTE:
            delete_note(args)
        case Commands.SORT_NOTES:
            sort_notes(args)
        case Commands.SHOW_NOTES:
            show_notes()
        case Commands.FIND:
            find(args)


def save_session():
    save_data({
        "address_book": address_book,
        "note_book": note_book
    })


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
        except IndexError:
            return Commands.messages.get(Commands.INVALID_NUMBER)
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

    record = address_book.find_record(args[0])
    if not record:
        message = Commands.errors[Commands.NOT_FOUND]
        return message

    if record.address:
        message = Commands.errors[Commands.ADR_EXISTS]
        return message

    address_params = {
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
            message = Commands.messages[Commands.QUIT_ADD_ADR]
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

    record = address_book.find_record(args[0])
    if not record:
        message = Commands.errors[Commands.NOT_FOUND]
        return message

    address_params: AddressParams = {
        Params.CITY: record.address.city,
        Params.STREET: record.address.street,
        Params.BUILDING: record.address.building
    }
    messages = {
        Params.CITY: Commands.messages[Commands.UPD_CITY],
        Params.STREET: Commands.messages[Commands.UPD_STR],
        Params.BUILDING: Commands.messages[Commands.UPD_BLD],
    }

    message = Commands.messages[Commands.UPD_ADR]
    for param in address_params:
        user_input = input(f"{messages[param]} [{address_params[param]}] ({Commands.messages[Commands.QUIT]}, "
                           f"{Commands.messages[Commands.PROCEED]}): ")
        if user_input == Commands.QUIT:
            message = Commands.messages[Commands.QUIT_UPD_ADR]
            break

        if user_input:
            address_params[param] = user_input
            record.update_address(address_params)
    return message


@show_message
def add_note() -> str:
    note_params = {"title": "", "text": "", "tags": []}
    messages = {
        "title": {
            "msg": f"{Commands.messages[Commands.ADD_TITLE]} ({Commands.messages[Commands.QUIT]}): ",
            "err": Commands.errors[Commands.NO_TITLE],
            "type": "title"
        },
        "text": {
            "msg": f"{Commands.messages[Commands.ADD_TEXT]} ({Commands.messages[Commands.QUIT]}): ",
            "err": Commands.errors[Commands.NO_TEXT],
            "type": "text"
        }
    }

    result = Commands.messages[Commands.ADD_NOTE]
    while True:
        if note_params["title"] and note_params["text"] and not note_book.find_note(note_params["title"]):
            tags_input = input(f"{Commands.messages[Commands.ADD_TAGS]} ({Commands.messages[Commands.QUIT]}): ")
            note_params["tags"] = tags_input.split(",") if tags_input else []
            note_book.add_note(note_params)
            break

        message = messages["title"] if not note_params["title"] else messages["text"]
        user_input = input(message["msg"])
        if user_input == "q":
            result = Commands.messages[Commands.QUIT_ADD_NOTE]
            break

        if user_input:
            note_params[message["type"]] = user_input
        else:
            print(message["err"])
    return result


@show_message
def change_note(args: List[str]) -> str:
    if len(args) == 0:
        return Commands.errors[Commands.NO_ARGS]

    note = note_book.find_note(args)
    if not note:
        return Commands.errors[Commands.NOTE_NOT_FOUND]

    note_params = {"title": note.title, "text": note, "tags": note.tags}
    messages = {
        "title": f"{Commands.messages[Commands.UPD_TITLE]} ({Commands.messages[Commands.QUIT]}, "
                 f"{Commands.messages[Commands.PROCEED]}): ",
        "text": f"{Commands.messages[Commands.UPD_TEXT]} ({Commands.messages[Commands.QUIT]}, "
                 f"{Commands.messages[Commands.PROCEED]}): ",
        "tags": f"{Commands.messages[Commands.UPD_TAGS]} ({Commands.messages[Commands.QUIT]}, "
                 f"{Commands.messages[Commands.PROCEED]}): ",
    }
    result = Commands.messages[Commands.CHANGE_NOTE]

    for param in note_params:
        user_input = input(messages[param])
        if user_input == "q":
            result = Commands.messages[Commands.QUIT_UPD_NOTE]
            break

        if user_input:
            note_params[param] = user_input

    note.update_note(note_params)
    return result


@show_message
def delete_note(args: List[str]) -> str:
    if len(args) == 0:
        return Commands.errors[Commands.NO_ARGS]

    message = Commands.errors[Commands.NOTE_NOT_FOUND]
    if len(args) > 0 and note_book.find_note(args):
        note_book.remove_note(args)
        message = Commands.messages[Commands.DELETE_NOTE]
    return message


@show_message
def sort_notes(args: List[str]) -> str:
    message = Commands.errors[Commands.NO_ARGS]
    if len(args) > 0:
        trimmed = [tag.strip() for tag in args]
        message = note_book.get_notes_by_tag(trimmed)
    return message


@show_message
def show_notes() -> str:
    message = Commands.errors[Commands.NOTES_EMPTY]
    if bool(note_book):
        message = str(note_book)
    return message


@input_error
@show_message
def find(args: List[str]) -> str:
    # if len(args) < 2: return Commands.messages.get(Commands.INVALID_CMD)
    if len(args) < 2: raise BotError(Commands.messages.get(Commands.INVALID_CMD))
    field = args[0]
    if field not in Commands.finds: raise BotError(Commands.messages.get(Commands.INVALID_CMD))
    perfect_match = False
    if len(args) == 2:
        query = args[1]
        perfect_match = True
    elif len(args) > 2:
        like_keyword = args[1]
        query = ''.join(args[2:])
        if like_keyword != Commands.LIKE: raise BotError(Commands.messages.get(Commands.INVALID_CMD))
    
    results = []
    for record in address_book.values():
        if record.find_match(field, query, perfect_match):
            results.append(record)
    message = "Nothing found"
    if results:
        message = ""
        for record in results:
            message += f"{str(record)}\n"
    return message