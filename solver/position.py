from typing import List


class Position:
    def __init__(self, row_num: int, col_num: int) -> None:
        self.row_num = row_num
        self.col_num = col_num

    def unit_delta(self, target: "Position") -> "Position":
        return Position(
            row_num=Position.unit_movement(self.row_num, target.row_num),
            col_num=Position.unit_movement(self.col_num, target.col_num),
        )

    @staticmethod
    def unit_movement(origin: int, target: int) -> int:
        if origin < target:
            return 1
        elif origin > target:
            return -1
        else:
            return 0

    def __repr__(self) -> str:
        return f"Position({self.row_num}, {self.col_num})"

    def __eq__(self, __value: "Position") -> bool:
        return self.row_num == __value.row_num and self.col_num == __value.col_num
