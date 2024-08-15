class Commands:
    ADD = "add"
    CHANGE = "change"
    DELETE = "delete"
    PHONE = "phone"
    ALL = "all"
    ADD_BD = "add-birthday"
    SHOW_BD = "show-birthday"
    ADD_ADR = "add-address"
    UPD_ADR = "upd-address"
    CHANGE_ADR = "change-address"
    HELLO = "hello"
    CLOSE = "close"
    EXIT = "exit"
    INVALID_CMD = "invalid-command"
    INVALID_PHONE = "invalid-phone"
    PHONE_EXISTS = "phone-exists"
    PHONE_NOT_FOUND = "phone-not-found"
    NOT_FOUND = "not-found"
    EMPTY = "empty"
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

    commands = [ADD, CHANGE, DELETE, PHONE, ALL, ADD_BD, SHOW_BD, ADD_ADR, CHANGE_ADR, HELLO, CLOSE, EXIT]

    messages = {
        HELLO: "How can I help you?",
        ADD: "Record added successfully",
        CHANGE: "Record updated successfully",
        DELETE: "Record deleted successfully",
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
        NOT_FOUND: "Record was not found",
        EMPTY: "Address book is empty",
        INVALID_PHONE: "Invalid phone format",
        PHONE_EXISTS: "Phone already exists",
        PHONE_NOT_FOUND: "Phone was not found",
        NO_RECORD: "Record name is required",
        NO_CITY: "City name is required",
        NO_STR: "Street name is required",
        NO_BLD: "Building number is required",
        ADR_EXISTS: "Address already exists"
    }