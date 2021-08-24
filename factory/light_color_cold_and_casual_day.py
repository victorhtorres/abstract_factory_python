from factory.abstract.outfit import Outfit
from factory.sweater_and_corduroy_pants import SweaterAndCorduroyPants
from factory.boots import Boots
from factory.abstract.foot_wear import FootWear
from factory.abstract.mens_clothes import MensClothes


class LightColorColdAndCasualDay(Outfit):

    def __init__(self) -> None:
        super().__init__(name="Light Colored Outfit for a Cold and Casual Day", formality=1)

    def choose_clothes(self) -> MensClothes:
        return SweaterAndCorduroyPants(rt="Cream-colored", rb="Light Brown")

    def choose_shoes(self) -> FootWear:
        return Boots()
