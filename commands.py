class Commands:
    ADD = "add"
    CHANGE = "change"
    DELETE = "delete"
    PHONE = "phone"
    ALL = "all"
    ADD_BD = "add-birthday"
    SHOW_BD = "show-birthday"
    ADD_NOTE = "add-note"
    EDIT_NOTE = "edit-note"
    DELETE_NOTE = "delete-note"
    SHOW_NOTES = "show-notes"
    ADD_ADR = "add-address"
    UPD_ADR = "upd-address"
    CHANGE_ADR = "change-address"
    BD_SOON = "birthdays"
    HELLO = "hello"
    CLOSE = "close"
    EXIT = "exit"

    WELCOME = "welcome"
    ENTER_CMD = "enter-command"
    ENTER_TITLE = "enter-title"
    ENTER_TEXT = "enter-text"
    ENTER_TAGS = "enter-tags"
    EMPTY = "empty"
    NOT_FOUND = "not-found"
    PHONE_NOT_FOUND = "phone-not-found"
    PHONE_EXISTS = "phone-exists"
    INVALID_CMD = "invalid-command"
    INVALID_PHONE = "invalid-phone"
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
    QUIT_ADD = "quit-adding"
    QUIT_UPD = "quit-updating"
    PROCEED = "proceed"
    NO_TITLE = "no-title"
    NO_TEXT = "no-text"
    NOTE_EXISTS = "note-exists"
    NOTE_NOT_FOUND = "note-not-found"
    NOTES_EMPTY = "notes-empty"

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
        EDIT_NOTE,
        DELETE_NOTE,
        SHOW_NOTES,
        HELLO,
        CLOSE,
        EXIT
    ]

    messages = {
        WELCOME: "Welcome to the assistant bot!",
        ENTER_CMD: "Enter a command: ",
        ENTER_TITLE: "Enter note title: ",
        ENTER_TEXT: "Enter note text: ",
        ENTER_TAGS: "Add note tags, comma separated (optional): ",
        HELLO: "How can I help you?",
        ADD: "Record added successfully",
        CHANGE: "Record updated successfully",
        DELETE: "Record deleted successfully",
        ADD_NOTE: "Note successfully added",
        DELETE_NOTE: "Note deleted successfully",
        EXIT: "Good bye!",
        INVALID_CMD: "Invalid command.",
        ADD_CITY: "Enter city",
        ADD_STR: "Enter street",
        ADD_BLD: "Enter building",
        ADD_ADR: "Address added successfully",
        UPD_ADR: "Address updated successfully",
        QUIT: "'q' to quit",
        QUIT_ADD: "Quit adding address",
        QUIT_UPD: "Quit updating address",
        PROCEED: "'enter' to proceed",
        UPD_CITY: "Update city name",
        UPD_STR: "Update street name",
        UPD_BLD: "Update building number"
    }

    errors = {
        INVALID_CMD: "Invalid command.",
        EMPTY: "Address book is empty",
        NOT_FOUND: "Record was not found",
        INVALID_PHONE: "Invalid phone format",
        PHONE_EXISTS: "Phone already exists",
        PHONE_NOT_FOUND: "Phone was not found",
        NO_TITLE: "Note title is required",
        NO_TEXT: "Note text is required",
        NOTE_EXISTS: "Note already exists",
        NOTE_NOT_FOUND: "Note was not found",
        NOTES_EMPTY: "Note book is empty",
        NO_RECORD: "Record name is required",
        NO_CITY: "City name is required",
        NO_STR: "Street name is required",
        NO_BLD: "Building number is required",
        ADR_EXISTS: "Address already exists"
    }
