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
        EXIT: "Good bye!"
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
        NOTES_EMPTY: "Note book is empty"
    }
