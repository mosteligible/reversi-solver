class Player:
    seen_names = ["x", "o"]
    def __init__(self, name: str, dhunga: str = "x") -> None:
        if name not in self.seen_names:
            raise ValueError("Invalid name, choose different name!")
        self.name = name
        self.seen_names.append(name)
        self.dhunga = dhunga
