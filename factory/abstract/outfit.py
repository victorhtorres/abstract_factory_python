from abc import ABC


class Outfit(ABC):

    def __init__(self, name: str, formality: int = 0) -> None:
        self.__formality: int = formality
        self.__name: str = name

    @property
    def get_formality(self) -> int:
        return self.__formality

    @property
    def get_name(self) -> str:
        return self.__name

    @get_formality.setter
    def set_formality(self, new_formality: int) -> None:
        self.__formality = new_formality

    def choose_clothes(self):
        pass

    def choose_shoes(self):
        pass
