class Position:
    def __init__(self, row_num: int, col_num: int) -> None:
        self.row_num = row_num
        self.col_num = col_num

    def __repr__(self) -> str:
        return f"({self.row_num}, {self.col_num})"
