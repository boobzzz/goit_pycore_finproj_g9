from functools import wraps
from boterror import BotError
from commands import Commands


def input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except BotError as e:
            print(str(e))
        except KeyboardInterrupt:
            print(Commands.messages[Commands.CANCELLED])
        except Exception as e:
            print(Commands.errors[Commands.GENERIC_ERROR])

    return inner


def show_message(func):
    @wraps(func)
    def inner(*args):
        message = func(*args)
        print(message)

    return inner
