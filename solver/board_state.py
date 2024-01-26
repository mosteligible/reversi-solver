from typing import List
from constants import DhungaType
from .position import Position
from .positions_manager import PositionsManager
from .solution_helpers import SolutionHelper


class BoardState:
    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.positions: List[DhungaType] = [[None] * size for i in range(size)]
        self.__setup_board()

    def __setup_board(self) -> None:
        mid = self.size // 2
        self.positions[mid - 1][mid - 1] = DhungaType.x
        self.positions[mid - 1][mid] = DhungaType.o
        self.positions[mid][mid - 1] = DhungaType.o
        self.positions[mid][mid] = DhungaType.x

    def get_available_moves(self, dhunga: DhungaType) -> List[PositionsManager]:
        return SolutionHelper.find_available_moves(self.positions, dhunga)

    def reset(self) -> None:
        self.positions = [[None] * self.size for i in range(self.size)]
        self.__setup_board()

    def update_position(self, pos: Position, dhunga: DhungaType) -> None:
        self.positions[pos.row_num][pos.col_num] = dhunga

    def update(self, played_position: PositionsManager) -> None:
        for pos_to_update in played_position.get_positions_to_swtich():
            self.update_position(pos_to_update, played_position.dhunga)
        self.update_position(played_position.position, played_position.dhunga)

    def __str__(self) -> str:
        retval = "   ".join([f"{i}" for i in range(self.size)])
        retval = f"    {retval}\n"
        num_dashes = (self.size - 1) * 4 + 7
        for index, row in enumerate(self.positions):
            row_str = " | ".join([" " if i is None else i.name for i in row])
            retval = f"{retval}{index} | {row_str} |\n"
            retval = f"{retval}{'-'*num_dashes}\n"
        return retval
