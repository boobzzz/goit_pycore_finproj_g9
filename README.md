# The Contact list bot.

This bot is produced as an educational team assignment. It allows using a command-line interface to interact with the improvized database - all done in Python.


### The bot supports storing contacts, each having all or some of the following attributes:
- Name [this is a mandatory field, which stores the primary identifier of a contact]
- Phones [this optional field stores one, or multiple phone numbers of a contact, in the 12-digit form\*]
- Emails [this optional field stores one, or multiple email addresses of a contact]
- Address [this optional field stores the address of a contact in the form of city, street, building number]
- Birthday [this optional field stores the birthday of a contact, in the following form: DD.MM.YYYY]

_\* The phone numbers support any country code, but default to the Ukrainian country code of **+380**. Thus, if the number is specified not in the full form, but as a local number - it will be converted to a Ukrainian phone number_

### Additionally the bot is able to keep handy text notes, which come with the following attributes:
- Note title [this is a mandatory field, which stores the primary identifier of a note]
- Note body [this is a mandatory field, which stores the main text of the note]
- Note tags [this optional field is used for tagging notes, which can be used for notes filtering]

### Installation and usage:
The bot can be installed in two ways: from its repository or directly from PyPI. The PyPI version might slightly lag behind the version in this repository.
- **Repository:**

  Clone the repository, go to the core folder in your terminal and run: `pip install .`
You can also install in developer mode by using: `pip install -e .`. This mode will allow you see local code changes with your installation.
- **PyPI:**

  Simply use `pip install megabot9` from your terminal. The bot and its dependencies will be automatically obtained from the PyPI servers and installed on your system.

**After installing, type `megabot` or `megabot9` from your terminal to use the bot. This will launch the bot in its command-line interface and show the greeting. If all done successfully, the commands will be auto-suggested to the user on typing.**

**When done with the bot, type `exit` or `close` to exit the bot's command-line interface. This action will store the actual session data, so that you could continue using the same state of contact data on re-launch\*.**

_\* Alternatively, you can make an exit which would purposedly skip saving data - e.g. if some some test or unwanted changes are made. To do that, simply exit the terminal by making an interrupt `Ctrl+C` (EOF `Ctrl+D` also supported if all necessary packages present)._

### The full list of commands supported by the bot are provided below with their explanations:
*NB: The same list can be outputed by typing `help` in the bot's command-line interface.*
```
add - Add a contact or add a phone to a contact
phone - Show a contact's phone number(s)
change - Change a contact's phone
add-email - Add an email address to a contact
show-email - Show a contact's email address(es)
change-email - Change a contact's email address
add-address - Add address data to a contact
change-address - Change address data of a contact
add-birthday - Add a birthday to a contact - in DD.MM.YYYY form
show-address - Show the contact's address
show-birthday - Show contact's birthday, if present, in DD.MM.YYYY form
all - Show all contacts in the address book with their data
find - Search for contacts
delete - Delete a contact by name
delete-email - Delete a contact's email address
birthdays - Show birthdays in the upcoming week, or in N upcoming days
add-note - Add a note
show-notes - Show all notes
change-note - Change a note
sort-notes - Filter notes by tags
delete-note - Delete a note
hello - Show greeting
save - Save the current state of the session
help - Show this help message
exit - Exit the application
```
#### The following section explains how exactly each command works:
- add - Add a contact or add a phone to a contact

  This command allows adding a new contact. It can be done as simply as typing `add Mike` into the bot. You can also add a contact immediately with a phone number, like `add Mike +111222333444`. To add an additional number for an existing contact, all that needs to be done is typing the add command again with specifying the contact's name, e.g.: `add Mike +111222333555`. The user is going to be informed if the same phone number is already present, or if the phone number given is invalid, or if the phone number is not given (like `add Mike`) but the user with that name is already present. Phone numbers can be given in a short form, like `add Mike 0554443322`, too. In such a case, the number is going to be padded with the Ukrainian country code and result in saving +380554443322 in such a case.
- phone - Show a contact's phone number(s)

  This command will return all the phone numbers of a contact - given that such a contact is present and any numbers are assigned to that contact. Example usage: `phone Mike`. The user is going to be informed if the contact is absent or if the contact has no phone numbers saved. This same result can be obtained with the `show-phone Mike`, as an alternative. The bot also reports the amount of phones found in a contact.
- change - Change a contact's phone

  This command allows changing an already saved phone number, example usage is the following: `change Mike 0554443322 0574443322`. The user is going to be informed if the number that is attempted to be changed is not present in contact's data.
- add-email - Add an email address to a contact

  This command allows assigning an email address to an existing contact. For example, one can type: `add-email Mike mike.surname@gmail.com` to assign a corresponding email to Mike. The user is going to be informed if the email is alrady present, or if it is invalid.
- show-email - Show a contact's email address

  This command will return all the email addresses of a contact - given that such a contact is present and any email addresses are assigned to that contact. Example usage: `show-email Mike`. The user is going to be informed if the contact is absent or if the contact has no email addresses saved. The bot also reports the amount of email addresses found in a contact.
- change-email - Change a contact's email address

  This command allows changing an already saved email address, example usage is the following: `change-email Mike mike.surname@gmail.com mike.lastname@gmail.com`. The user is going to be informed if the number that is attempted to be changed is not present in contact's data.
- add-address - Add address data to a contact

  This command allows to add address data to the contact. Typing `add-address Mike` would open an interactive dialogue where the bot would ask the following consequence of data pieces: city, street, building number. All fields are mandatory, and it is allowed to quit from the process midway without saving anything.
- change-address - Change address data of a contact

  This command allows to change the address data saved in the contact. Typing `change-address Mike` would open an interactive dialogue where the bot would ask the following consequence of data pieces: city, street, building number. All fields can be skipped, in which case the old address would remain, and it is allowed to quit from the process midway without changing anything. The user is going to be informed if the address data is not present in the contact.
- add-birthday - Add a birthday to a contact - in DD.MM.YYYY form

  This command allows adding birthday data to a contact in the specified DD.MM.YYYY form. Example: `add-birthday Mike 01.02.1990`. The user is going to be informed if the birth date is given in a wrong format.
- show-address - Show contact's birthday, if present, in DD.MM.YYYY form

  This command returns the address of a contact, if any found. Example: `show-address Mike`. The user is going to be informed, if the requested contact is not found or has no address data saved.
- show-birthday - Show contact's birthday, if present, in DD.MM.YYYY form

  This command returns the birthday data of a contact, if any, in the specified DD.MM.YYYY form. Example: `show-birthday Mike`. The user is going to be informed, if the requested contact is not found or has no birthday data saved.
- all - Show all contacts in the address book with their data

  This command returns all the contacts currently present, including all their data: name, all phones, all email addresses, address and birth date. The bot also reports the amount of contacts found.
- find - Search for contacts

  This command allows finding contacts by matching with the query. There are multiple ways to carry this out: one can look for a specific phone number like `find phone 0574443322`, but wildcard search is also supported - when the like keyword is used, for instance `find phone like 057444_322` would try to find any contacts which have a phone number where the `_` in the middle is any digit. A broader wildcard search is to be used with the '%' symbol. For instance, following the same example, one can try: `find phone like 057%`. The functionality allows similar usage for searching for the following contact attributes: **name**, **phone**, **email address**, **address** (any field), **city**, **street**, **building**, **birthday**. The bot also reports the amount of contacts found that match the query.
- delete - Delete a contact by name

  This command allows deletion of an existing contact, specified by name. For example: `delete Mike`. The user is going to be informed if the contact is not present in the system.
- delete-email - Delete a contact's email address

  This command allows deleting the email address from the contact. For example: `delete-email Mike mike.lastname@gmail.com`. The user is going to be informed if the contact is absent or the specified email address is not found.
- birthdays - Show birthdays in the upcoming week, or in N upcoming days

  This command returns all the users who have their birthdays in the next **n** days. By default, n is **7**, so that's a week. So, one can use it like `birthdays` for the next week's birthdays or like `birthdays 30` for the upcoming birthdays in the next 30 days. If the birthday is on a weekend (Saturday or Sunday), then the congratulation date is moved to the next Monday and reported, correspondingly, together with the original birthday date.
- add-note - Add a note

  This command allows to add a note to the bot. Typing the command would open an interactive dialogue where the bot would ask the following consequence of data pieces: note title, note body and note tags. Note tags are optional, but can be provided, separated by comma, to allow filtering notes by them later on.
- show-notes - Show notes

  This command returns all the saved notes.
- change-note - Change a note

  This command allows changing an existing note by referring to it by its note title. For example: `change-note MyFirstNote` (the note title is case insensitive in this case).
- sort-notes - Sort notes

  This command allows filtering the notes by tags, which can be supplied separated by comma. For example, `sort-notes food, reminder, sport` would return any notes which had either of the **food**, **reminder** or **sport** tags added to them.
- delete-note - Delete a note

  This command allows deleting an existing note by referring to it by its note title. For example: `change-note MyFirstNote` (the note title is case insensitive in this case).
- hello - Show greeting

  This command simply outputs a greeting and a hint for getting help.
- save - Save the current state of the session

  This command can be used to save the updates to the session data on demand. Otherwise, the saving happens only on the bot exit.
- help - Show this help message

  This command outputs a simple help message, where it shows the commands and their short descriptions.
- exit - Exit the application

  This command will do a proper exit from the bot - i.e. with saving the session data for later use. An alternative way to do this is to type `close` instead.
