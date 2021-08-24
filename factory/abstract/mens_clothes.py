from abc import ABC
from factory.abstract.foot_wear import FootWear


class MensClothes(ABC):

    def __init__(self, rt: str, rb: str) -> None:
        self.__colort: str = rt
        self.__colorb: str = rb

    @property
    def get_colorb(self) -> str:
        return self.__colorb

    @property
    def get_colort(self) -> str:
        return self.__colort

    @get_colorb.setter
    def set_colorb(self, colorb: str) -> None:
        self.__colorb = colorb

    @get_colort.setter
    def set_colort(self, colort: str) -> None:
        self.__colort = colort

    def clothespecs(self, foot_w: FootWear):
        pass
