from address_book import AddressBook
from note_book import NoteBook
import pickle

FILENAME = "session_data.pkl"


def save_data(data):
    with open(FILENAME, "wb") as file:
        pickle.dump(data, file)


def load_data() -> AddressBook:
    data = {
        "address_book": AddressBook(),
        "note_book": NoteBook()
    }
    try:
        with open(FILENAME, "rb") as file:
            data = pickle.load(file)
    except Exception:
        pass
    return data
