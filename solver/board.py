class Board:
    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.positions = [[None] * size for i in range(size)]
        self.setup_board()

    def setup_board(self) -> None:
        self.positions[3][3] = "x"
        self.positions[3][4] = "o"
        self.positions[4][3] = "o"
        self.positions[4][4] = "x"

    def update_board(self) -> None:
        ...

    def play_position(self) -> None:
        ...

    def __str__(self) -> str:
        retval = ''
        for row in self.positions:
            row_str = " | ".join([" " if i is None else i for i in row])
            retval = f"{retval}| {row_str} |\n"
        return retval
