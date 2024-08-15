from field import Field
from enum import Enum
from typing import TypedDict


class Params(str, Enum):
    CITY = "city"
    STREET = "street"
    BUILDING = "building"


class AddressParams(TypedDict):
    city: str
    street: str
    building: str


class Address(Field):
    def __init__(self, params: AddressParams):
        self.__city = params["city"].lower().capitalize()
        self.__street = params["street"].lower().capitalize()
        self.__building = params["building"]

        value = f"{self.__city}, {self.__street}, {self.__building}"
        super().__init__(value)

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def building(self):
        return self.__building
