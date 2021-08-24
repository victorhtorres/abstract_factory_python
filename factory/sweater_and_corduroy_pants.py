from factory.abstract.mens_clothes import MensClothes
from factory.abstract.foot_wear import FootWear


class SweaterAndCorduroyPants(MensClothes):

    def __init__(self, rt: str = "Brown", rb: str = "Brown") -> None:
        super().__init__(rt, rb)
        print(f"You picked the {rt} sweater and the {rb} corduroy pants")

    def clothespecs(self, foot_w: FootWear) -> None:
        foot_w.shoespecs(c=self.get_colorb)
