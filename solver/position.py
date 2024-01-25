from typing import List


class Position:
    def __init__(self, row_num: int, col_num: int) -> None:
        self.row_num = row_num
        self.col_num = col_num

    def __repr__(self) -> str:
        return f"Position({self.row_num}, {self.col_num})"

    def __eq__(self, __value: "Position") -> bool:
        return self.row_num == __value.row_num and self.col_num == __value.col_num


class PositionsManager:
    def __init__(
        self,
        position: Position,
        next_linears: List[Position],
        next_verticals: List[Position],
        next_diagonals_top_to_bottom: List[Position],
        next_diagonals_bottom_to_top: List[Position],
    ) -> None:
        self.position = position
        self.next_linears = next_linears
        self.next_verticals = next_verticals
        self.next_diagonals_top_to_bottom = next_diagonals_top_to_bottom
        self.next_diagonals_bottom_to_top = next_diagonals_bottom_to_top

    def get_position_of_dhunga_changes(self) -> List[Position]:
        raise NotImplementedError

    def __repr__(self) -> str:
        return (
            f"PositionManager(position: {self.position} - "
            f"linear: {self.next_linears} - "
            f"verticals: {self.next_verticals} - "
            f"diagonals \ : {self.next_diagonals_top_to_bottom} - "
            f"diagonals / : {self.next_diagonals_bottom_to_top})"
        )
