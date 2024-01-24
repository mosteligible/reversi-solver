from typing import List
from constants import DhungaType
from .position import Position


class BoardState:
    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.positions: List[DhungaType] = [[None] * size for i in range(size)]
        self.__setup_board()

    def __setup_board(self) -> None:
        self.positions[3][3] = DhungaType.x
        self.positions[3][4] = DhungaType.o
        self.positions[4][3] = DhungaType.o
        self.positions[4][4] = DhungaType.x

    def reset_board(self) -> None:
        self.positions = [[None] * self.size for i in range(self.size)]
        self.__setup_board()

    def update_board(self, pos: Position, dhunga: DhungaType) -> None:
        self.positions[pos.row_num][pos.col_num] = dhunga

    def __str__(self) -> str:
        retval = ""
        for row in self.positions:
            row_str = " | ".join([" " if i is None else i.name for i in row])
            retval = f"{retval}| {row_str} |\n"
        return retval
