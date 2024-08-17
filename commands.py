class Commands:
    ADD = "add"
    CHANGE = "change"
    DELETE = "delete"
    PHONE = "phone"
    ALL = "all"
    ADD_BD = "add-birthday"
    SHOW_BD = "show-birthday"
    ADD_NOTE = "add-note"
    CHANGE_NOTE = "change-note"
    DELETE_NOTE = "delete-note"
    SHOW_NOTES = "show-notes"
    ADD_ADR = "add-address"
    UPD_ADR = "upd-address"
    CHANGE_ADR = "change-address"
    BD_SOON = "birthdays"
    BD_FOUND = "bd-found"
    BD_NOT_FOUND = "bd-not-found"
    HELLO = "hello"
    CLOSE = "close"
    EXIT = "exit"
    GENERIC_ERROR = 'error'

    WELCOME = "welcome"
    ENTER_CMD = "enter-command"
    CANCELLED = "cancelled"
    CONTACTS_LIST = "contacts-list"
    ADD_TITLE = "enter-title"
    ADD_TEXT = "enter-text"
    ADD_TAGS = "enter-tags"
    UPD_TITLE = "update-title"
    UPD_TEXT = "update-text"
    UPD_TAGS = "update-tags"
    SORT_NOTES = "sort-notes"
    EMPTY = "empty"
    NOT_FOUND = "not-found"
    PHONE_NOT_FOUND = "phone-not-found"
    PHONE_EXISTS = "phone-exists"
    EXIT_KB = "exit-kb"
    INVALID_CMD = "invalid-command"
    INVALID_PHONE = "invalid-phone"
    INVALID_NUMBER = "invalid-number"
    NO_RECORD = "no-record"
    ADD_CITY = "enter-city"
    UPD_CITY = "update-city"
    NO_CITY = "no-city"
    ADD_STR = "enter-street"
    UPD_STR = "update-street"
    NO_STR = "no-street"
    ADD_BLD = "enter-building"
    UPD_BLD = "update-building"
    NO_BLD = "no-building"
    ADR_EXISTS = "address-exists"
    QUIT = "q"
    QUIT_ADD_ADR = "quit-adding-address"
    QUIT_UPD_ADR = "quit-updating-address"
    QUIT_ADD_NOTE = "quit-adding-note"
    QUIT_UPD_NOTE = "quit-updating-note"
    PROCEED = "proceed"
    NO_TITLE = "no-title"
    NO_TEXT = "no-text"
    NOTE_EXISTS = "note-exists"
    NOTE_NOT_FOUND = "note-not-found"
    NOTES_NOT_FOUND = "notes-not-found"
    NOTES_EMPTY = "notes-empty"
    NO_ARGS = "not-enough-args"

    FIND = "find"
    LIKE = "like"
    NAME = "name"
    BIRTHDAY = "birthday"
    ADDRESS = "address"
    CITY = "city"
    STREET = "street"
    BUILDING = "building"
    EMAIL = "email"

    ADD_EMAIL = "add-email"
    CHANGE_EMAIL = "change-email"
    DELETE_EMAIL = "delete-email"
    SHOW_EMAIL = "show-email"

    EMAIL_EXISTS = "email-exists"
    EMAIL_NOT_FOUND = "email-not-found"
    INVALID_EMAIL = "invalid-email"


    finds = [NAME, PHONE, BIRTHDAY, ADDRESS, CITY, STREET, BUILDING, EMAIL]

    commands = [
        ADD,
        CHANGE,
        DELETE,
        PHONE,
        ALL,
        ADD_BD,
        SHOW_BD,
        BD_SOON,
        ADD_ADR,
        CHANGE_ADR,
        ADD_NOTE,
        CHANGE_NOTE,
        DELETE_NOTE,
        SORT_NOTES,
        SHOW_NOTES,
        HELLO,
        FIND,
        CLOSE,
        EXIT,
        ADD_EMAIL,
        CHANGE_EMAIL,
        DELETE_EMAIL,
        SHOW_EMAIL,
    ]

    messages = {
        WELCOME: "Welcome to the assistant bot!",
        ENTER_CMD: "\nEnter a command: ",
        CANCELLED: "\nCancelled",
        CONTACTS_LIST: "Full contact list:\n\n",
        ADD_TITLE: "Enter note title",
        ADD_TEXT: "Enter note text",
        ADD_TAGS: "Add note tags, comma separated (optional)",
        UPD_TITLE: "Update note title",
        UPD_TEXT: "Update note text",
        UPD_TAGS: "Update note tags, comma separated",
        QUIT_ADD_NOTE: "Quit adding note.",
        QUIT_UPD_NOTE: "Quit updating note.",
        HELLO: "How can I help you?",
        ADD: "Record added successfully.",
        CHANGE: "Record updated successfully.",
        DELETE: "Record deleted successfully.",
        ADD_NOTE: "Note added successfully.",
        CHANGE_NOTE: "Note updated successfully.",
        DELETE_NOTE: "Note deleted successfully.",
        EXIT: "Good bye!",
        EXIT_KB: "Good bye! [session not saved]",
        INVALID_CMD: "Invalid command.",
        ADD_CITY: "Enter city",
        ADD_STR: "Enter street",
        ADD_BLD: "Enter building",
        ADD_ADR: "Address added successfully.",
        UPD_ADR: "Address updated successfully.",
        QUIT: "'q' to quit",
        QUIT_ADD_ADR: "Quit adding address.",
        QUIT_UPD_ADR: "Quit updating address.",
        PROCEED: "'enter' to proceed",
        UPD_CITY: "Update city name",
        UPD_STR: "Update street name",
        UPD_BLD: "Update building number",
        ADD_EMAIL: "Email added successfully.",
        CHANGE_EMAIL: "Email updated successfully.",
        DELETE_EMAIL: "Email deleted successfully.",
        INVALID_EMAIL: "Invalid email address format.",
        BD_FOUND: "The following birthdays found:\n",
        BD_NOT_FOUND: "No upcoming birthdays found.",
    }

    errors = {
        NOT_FOUND: "Record was not found",
        EMPTY: "Address book is empty",
        INVALID_PHONE: "Invalid phone format",
        INVALID_NUMBER: "Invalid number argument",
        PHONE_EXISTS: "Phone already exists",
        PHONE_NOT_FOUND: "Phone was not found",
        NO_TITLE: "Note title is required",
        NO_TEXT: "Note text is required",
        NOTE_EXISTS: "Note already exists",
        NOTE_NOT_FOUND: "Note was not found",
        NOTES_NOT_FOUND: "No notes with provided tags",
        NOTES_EMPTY: "Note book is empty",
        NO_RECORD: "Record name is required",
        NO_CITY: "City name is required",
        NO_STR: "Street name is required",
        NO_BLD: "Building number is required",
        ADR_EXISTS: "Address already exists",
        NO_ARGS: "Not enough arguments",
        EMAIL_EXISTS: "Email already exists",
        EMAIL_NOT_FOUND: "Email was not found",
        INVALID_EMAIL: "Invalid email format",
        GENERIC_ERROR: "An error happened.",
    }
