from factory.abstract.foot_wear import FootWear


class Loafers(FootWear):

    def __init__(self) -> None:
        print("Shoes for a nice day")

    def shoespecs(self, c: str = "Brown") -> None:
        print(f"You picked {c} loafers")
