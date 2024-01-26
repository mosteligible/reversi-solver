import pytest
from typing import List

from constants import DhungaType
from solver.position import Position
from solver.positions_manager import PositionsManager


@pytest.fixture
def get_positions() -> List[Position]:
    positions = [
        Position(*[0, 0]),
        Position(*[4, 4]),
        Position(*[2, 0]),
        Position(*[0, 2]),
    ]
    return positions


def test_get_positions_in_between(get_positions) -> None:
    pm = PositionsManager(
        Position(2, 2), dhunga=DhungaType.x, target_positions=get_positions
    )
    assert pm.get_positions_to_swtich() == [
        Position(1, 1),
        Position(3, 3),
        Position(2, 1),
        Position(1, 2),
    ]
    pm = PositionsManager(
        Position(2, 3), dhunga=DhungaType.x, target_positions=get_positions
    )
    assert pm.get_positions_to_swtich() == [Position(2, 2), Position(2, 1)]

    # when position manager is built with a position not in line with targets
    pm = PositionsManager(
        Position(3, 7), dhunga=DhungaType.x, target_positions=get_positions
    )
    assert pm.get_positions_to_swtich() == []
