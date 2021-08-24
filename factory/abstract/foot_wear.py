from abc import ABC


class FootWear(ABC):

    def __init__(self) -> None:
        self.__color: str = 'Brown'

    def shoespecs(self, c: str) -> None:
        pass