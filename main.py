import os
from typing import Tuple
from handler import get_response, save_session
from commands import Commands
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


def parse_input(user_input: str) -> Tuple:
    if not user_input:
        return Commands.INVALID_CMD

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Commands.messages[Commands.WELCOME])
    advanced_mode = True
    try:
        bot_completer = WordCompleter(Commands.commands + [Commands.FIND + ' ' + find for find in Commands.finds], ignore_case=True, sentence=True)
        session = PromptSession(completer=bot_completer)
    except:
        advanced_mode = False
    while True:
        try:
            if advanced_mode:
                cmd, *args = parse_input(session.prompt(Commands.messages[Commands.ENTER_CMD]))
            else:
                cmd, *args = parse_input(input(Commands.messages[Commands.ENTER_CMD]))
        except KeyboardInterrupt:
            print(('' if advanced_mode else '\n') + Commands.messages[Commands.EXIT_KB])
            break
        except EOFError:
            print(Commands.messages[Commands.EXIT_KB])
            break
        if cmd in [Commands.CLOSE, Commands.EXIT]:
            save_session()
            print(Commands.messages[Commands.EXIT])
            break

        if cmd in Commands.commands:
            get_response(cmd, args)
        else:
            print(Commands.messages[Commands.INVALID_CMD])


if __name__ == "__main__":
    main()
