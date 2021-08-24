from factory.abstract.outfit import Outfit
from factory.button_down_shirt_and_dress_pants import ButtonDownShirtAndDressPants
from factory.loafers import Loafers
from factory.abstract.foot_wear import FootWear
from factory.abstract.mens_clothes import MensClothes


class DarkColorWarmSemiFormalDay(Outfit):

    def __init__(self) -> None:
        super().__init__(name='Dark Colored Outfit for a Semi-Formal Day', formality=2)

    def choose_clothes(self) -> MensClothes:
        return ButtonDownShirtAndDressPants(rt='burgundy', rb='black')

    def choose_shoes(self) -> FootWear:
        return Loafers()
