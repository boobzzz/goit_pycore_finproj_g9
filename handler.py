from typing import List, Dict
from commands import Commands
from decorators import input_error, show_message
from session_handler import save_data, load_data
from address import AddressParams, Params
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
            birthdays()
        case Commands.ADD_ADR:
            add_address(args)
        case Commands.CHANGE_ADR:
            change_address(args)


def save_session():
    save_data(book)


@show_message
def say_hello() -> str:
    return Commands.messages.get(Commands.HELLO)


@input_error
@show_message
def add_contact(args: List[str]) -> str:
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
    name = args[0]
    record = book.find_record(name)
    message = Commands.errors.get(Commands.NOT_FOUND)
    if record:
        message = record.birthday.strftime(record.birthday.format)
    return message


@show_message
def birthdays() -> str:
    message = Commands.errors.get(Commands.EMPTY)
    bd_entries = []
    if bool(book):
        message = ""
        for record in book.values():
            record_bd_now = utils.is_bd_in_range(record)
            if record_bd_now:
                entry = {
                    "name": record.name,
                    "congrats_date": utils.get_congrats_date(record_bd_now)
                }
                bd_entries.append(entry)
        bd_entries.sort(key=lambda e: e["congrats_date"])

        for entry in bd_entries:
            message += f"{entry["name"]}: {entry["congrats_date"].date()}\n"

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
