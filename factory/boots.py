from factory.abstract.foot_wear import FootWear


class Boots(FootWear):

    def __init__(self) -> None:
        print("Wear boots on a cold day")

    def shoespecs(self, c: str = "Brown") -> None:
        print(f"You picked {c} boots")
