from constants import DhungaType


class Player:
    def __init__(self, name: str, dhunga: DhungaType) -> None:
        if name not in DhungaType:
            raise ValueError("Invalid name, choose different name!")
        self.name = name
        self.dhunga = dhunga
