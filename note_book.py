from collections import UserDict
from typing import List
from note import Note


class NoteBook(UserDict):
    def add_note(self, title: str, text: str, tags: List[str] = None) -> Note:
        note = Note(title, text)
        self[title] = note
        if tags:
            note.add_tags(tags)
        return note

    def edit_note(self, title: str):
        pass

    def remove_note(self, title: str):
        self.pop(title)

    def find_note(self, title: str) -> Note:
        note = None
        if title in self:
            note = self[title]
        return note

    def get_notes_by_tag(self, tags: List[str]) -> str:
        pass

    def __str__(self):
        notes = ""
        for note in self:
            notes += f"{self[note]}\n\n"
        return notes
