from address_book import AddressBook
from note_book import NoteBook
import pickle
import os

FILENAME = "session_data.pkl"


def save_data(data):
    with open(FILENAME, "wb") as file:
        pickle.dump(data, file)


def load_data() -> AddressBook:
    data = {
        "address_book": AddressBook(),
        "note_book": NoteBook()
    }
    if os.path.getsize(FILENAME) > 0:
        try:
            with open(FILENAME, "rb") as file:
                data = pickle.load(file)
        except FileNotFoundError:
            pass
    return data
