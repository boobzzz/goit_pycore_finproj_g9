from typing import List
from field import Field


class Note(Field):
    def __init__(self, title: str, value: str):
        super().__init__(value)
        self.__title: str = title
        self.__tags: List[str] = []

    @property
    def title(self):
        return self.__title

    @property
    def tags(self):
        return self.__tags

    def add_tags(self, tags: List[str]):
        if len(tags) > 0:
            trimmed = [tag.strip() for tag in tags]
            self.__tags.extend(list(set(trimmed)))

    def remove_tag(self, tag: str):
        self.__tags.remove(tag)

    def edit_note(self, title: str, text: str, tags):
        pass

    def __str__(self):
        return (
            f"{self.__title}\n"
            f"{self.value}\n"
            f"tags: {", ".join(self.__tags) if len(self.__tags) > 0 else "none"}"
        )
