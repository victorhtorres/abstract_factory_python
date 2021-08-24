from factory.abstract.outfit import Outfit
from factory.abstract.mens_clothes import MensClothes
from factory.abstract.foot_wear import FootWear


class Look:

    def __init__(self, factory: Outfit) -> None:
        self.factory: Outfit = factory
        print(factory.get_name)
        self.clo: MensClothes = factory.choose_clothes()
        self.sho: FootWear = factory.choose_shoes()

    def dress(self) -> None:
        self.clo.clothespecs(self.sho)

    def __eq__(self, m) -> bool:
        return self.factory.get_formality == m.factory.get_formality

    def __gt__(self, m) -> bool:
        return self.factory.get_formality > m.factory.get_formality
