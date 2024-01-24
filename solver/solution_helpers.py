import config
from typing import List
from constants import DhungaType

from .board_state import BoardState
from .position import Position


class SolutionHelper:
    @staticmethod
    def find_next_dhunga_match(row: List[DhungaType], dhunga: DhungaType) -> bool:
        print(f"row: {row} - dhunga: {dhunga}")
        if row[0] == dhunga:
            return False
        for dh in row:
            if dh is not None and dh != dhunga:
                return True
        return False

    @staticmethod
    def check_in_line(row: List[DhungaType], pos: Position, dhunga: DhungaType) -> bool:
        """
        In row, to get elements before/after given `pos` use `pos.col_num`
        as it is associated with current vertical position in matrix.
        """
        print(f"-- actual row: {row} - pos: {pos}")
        if (
            not (pos.col_num + 1 > config.BOARD_SIZE)
            and row[pos.col_num + 1] is not None
        ):
            # do right side lookup
            # if match found, return True
            print(f"-- processing row: {row[pos.col_num + 1 :]} - dh: {dhunga}")
            return SolutionHelper.find_next_dhunga_match(
                row=row[pos.col_num + 1 :], dhunga=dhunga
            )
        if not (pos.col_num - 1 < 0) and row[pos.col_num - 1] is not None:
            # do left side lookup
            # if match found, return True
            row_to_check = row[: pos.col_num]
            row_to_check.reverse()
            print(f"-- processing row: {row_to_check} - dh: {dhunga}")
            return SolutionHelper.find_next_dhunga_match(
                row=row_to_check, dhunga=dhunga
            )
        return False

    @staticmethod
    def is_playable(
        positions: List[List[DhungaType]], dhunga: DhungaType, pos: Position
    ) -> bool:
        side_check = SolutionHelper.check_in_line(positions[pos.row_num], pos, dhunga)
        column = SolutionHelper.get_matrix_col(positions, pos.col_num)
        col_check = SolutionHelper.check_in_line(column, pos, dhunga)
        return side_check or col_check

    @staticmethod
    def get_matrix_col(
        positions: List[List[DhungaType]], col_index: int
    ) -> List[List[DhungaType]]:
        return [i[0] for i in zip(positions)][col_index]

    @staticmethod
    def find_available_moves(board_state: BoardState, dhunga: DhungaType) -> list:
        available_moves = []
        for row_num, row in enumerate(board_state.positions):
            for col_num, col_val in enumerate(row):
                if col_val is None:
                    cur_pos = Position(row_num, col_num)
