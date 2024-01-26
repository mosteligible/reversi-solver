import config
from typing import List
from constants import DhungaType

from .position import Position


class PositionsManager:
    def __init__(
        self,
        position: Position,
        dhunga: DhungaType,
        target_positions: List[Position],
    ) -> None:
        self.position = position
        self.dhunga = dhunga
        self.target_positions = target_positions

    def get_positions_in_between(self, target: Position) -> List[Position]:
        delta = self.position.unit_delta(target)
        pos = Position(self.position.row_num, self.position.col_num)
        pos_in_between = []
        while True:
            pos = Position(pos.row_num + delta.row_num, pos.col_num + delta.col_num)
            if pos == target:
                break
            if (
                pos.row_num >= config.BOARD_SIZE or pos.col_num >= config.BOARD_SIZE
            ) or (pos.row_num < 0 or pos.col_num < 0):
                raise ValueError(f"{self.position} not inline with {target}")

            pos_in_between.append(pos)
        return pos_in_between

    def get_positions_to_swtich(self) -> List[Position]:
        pos_to_change = []
        for target in self.target_positions:
            try:
                pos_in_between = self.get_positions_in_between(target)
                pos_to_change.extend(pos_in_between)
            except ValueError:
                pass
        return pos_to_change

    def __repr__(self) -> str:
        return (
            f"PositionManager({self.position} {self.dhunga.name}\n"
            f"target_positions: {self.target_positions})\n"
        )

    def __eq__(self, __value: "PositionsManager") -> bool:
        return (
            self.position == __value.position
            and self.dhunga == __value.dhunga
            and self.target_positions == __value.target_positions
        )
