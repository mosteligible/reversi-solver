import config
from typing import List, Tuple
from constants import DhungaType

from .board_state import BoardState
from .position import Position, PositionsManager


class SolutionHelper:
    @staticmethod
    def find_next_dhunga_match(
        row: List[DhungaType], dhunga: DhungaType
    ) -> Tuple[bool, int]:
        if len(row) == 0:
            return False, -1
        if row[0] == dhunga or row[0] == None:
            return False, -1
        for index, dh in enumerate(row[1:]):
            if dh is not None and dh == dhunga:
                return True, index + 1
        return False, -1

    @staticmethod
    def check_in_line(row: List[DhungaType], pos: int, dhunga: DhungaType) -> List[int]:
        """
        params:
            pos: index of the dhunga that is being checked for validity.
        """
        matches = []
        if pos + 1 < len(row) and row[pos + 1] is not None:
            # do right side lookup
            # if match found, return True
            match, index = SolutionHelper.find_next_dhunga_match(
                row=row[pos + 1 :], dhunga=dhunga
            )
            if match:
                matches.append(index + pos + 1)
        if not (pos - 1 < 0) and row[pos - 1] is not None:
            # do left side lookup
            # if match found, return True
            row_to_check = row[:pos]
            row_to_check.reverse()
            match, index = SolutionHelper.find_next_dhunga_match(
                row=row_to_check, dhunga=dhunga
            )
            if match:
                matches.append(pos - index - 1)
        return matches

    @staticmethod
    def get_diagonals_as_row(
        positions: List[List[str]], pos: Position
    ) -> Tuple[List[DhungaType], int, List[DhungaType], int]:
        reversed_front_elements_up = []
        back_elements_down = []
        reversed_front_elements_down = []
        back_elements_up = []
        position_dhunga = positions[pos.row_num][pos.col_num]
        for index in range(1, config.BOARD_SIZE):
            if pos.row_num - index >= 0 and pos.col_num - index >= 0:
                reversed_front_elements_up.append(
                    positions[pos.row_num - index][pos.col_num - index]
                )
            if pos.row_num + index < config.BOARD_SIZE and pos.col_num - index >= 0:
                reversed_front_elements_down.append(
                    positions[pos.row_num + index][pos.col_num - index]
                )
            if (
                pos.row_num + index < config.BOARD_SIZE
                and pos.col_num + index < config.BOARD_SIZE
            ):
                back_elements_down.append(
                    positions[pos.row_num + index][pos.col_num + index]
                )
            if pos.row_num - index >= 0 and pos.col_num + index < config.BOARD_SIZE:
                back_elements_up.append(
                    positions[pos.row_num - index][pos.col_num + index]
                )
        reversed_front_elements_up.reverse()
        # position of dhunga passed as parameter `pos` has to be tracked
        # as diagonals converted to 1D matrix will not have same number
        # of elements as config.BOARD_SIZE
        index_1 = len(reversed_front_elements_up)
        reversed_front_elements_up.append(position_dhunga)
        reversed_front_elements_up.extend(back_elements_down)

        reversed_front_elements_down.reverse()
        index_2 = len(reversed_front_elements_down)
        reversed_front_elements_down.append(position_dhunga)
        reversed_front_elements_down.extend(back_elements_up)
        return (
            reversed_front_elements_up,
            index_1,
            reversed_front_elements_down,
            index_2,
        )

    @staticmethod
    def check_diaognals(
        pos: Position, positions: List[List[DhungaType]], dhunga: DhungaType
    ) -> Tuple[List[Position], List[Position]]:
        diag1, pos1, diag2, pos2 = SolutionHelper.get_diagonals_as_row(positions, pos)
        diag1_indexes = SolutionHelper.check_in_line(diag1, pos1, dhunga)
        diag1_positions = [
            Position(row_num=pos.row_num + (i - pos1), col_num=i) for i in diag1_indexes
        ]
        diag2_indexes = SolutionHelper.check_in_line(diag2, pos2, dhunga)
        diag2_positions = [
            Position(row_num=pos.row_num - (i - pos2), col_num=i) for i in diag2_indexes
        ]
        return diag1_positions, diag2_positions

    @staticmethod
    def palayable_moves(
        positions: List[List[DhungaType]], dhunga: DhungaType, pos: Position
    ) -> Tuple[PositionsManager, bool]:
        linear_indexes = SolutionHelper.check_in_line(
            positions[pos.row_num], pos.col_num, dhunga
        )
        linear_positions = [Position(pos.row_num, i) for i in linear_indexes]
        column = SolutionHelper.get_matrix_col(positions, pos.col_num)
        vertical_indexes = SolutionHelper.check_in_line(column, pos.row_num, dhunga)
        vertical_positions = [Position(i, pos.col_num) for i in vertical_indexes]
        top_bottom_diagonal, bottom_top_diagonal = SolutionHelper.check_diaognals(
            pos, positions, dhunga
        )
        match = (
            linear_positions
            or vertical_positions
            or top_bottom_diagonal
            or bottom_top_diagonal
        )
        return (
            PositionsManager(
                position=pos,
                next_linears=linear_positions,
                next_verticals=vertical_positions,
                next_diagonals_top_to_bottom=top_bottom_diagonal,
                next_diagonals_bottom_to_top=bottom_top_diagonal,
            ),
            match,
        )

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
