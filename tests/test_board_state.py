from constants import DhungaType
from solver.board_state import BoardState
from solver.position import Position
from solver.positions_manager import PositionsManager


def test_init() -> None:
    board_state = BoardState()
    assert (
        board_state.positions[3][3] == DhungaType.x
        and board_state.positions[4][4] == DhungaType.x
    )
    assert (
        board_state.positions[3][4] == DhungaType.o
        and board_state.positions[4][3] == DhungaType.o
    )


def test_update_position() -> None:
    board_state = BoardState()
    board_state.update_position(Position(3, 4), None)
    board_state.update_position(Position(4, 4), -1)
    assert board_state.positions[3][4] is None
    assert board_state.positions[4][4] == -1


def test_get_available_moves() -> None:
    board_state = BoardState()
    board_state.update_position(Position(3, 4), None)
    board_state.update_position(Position(4, 4), None)
    dh = DhungaType.x
    print(board_state, dh)
    available_moves = board_state.get_available_moves(dh)
    print(available_moves)
    expected = [
        PositionsManager(
            dhunga=dh, position=Position(5, 3), target_positions=[Position(3, 3)]
        )
    ]
    assert available_moves == expected


def test_reset() -> None:
    board_state = BoardState()
    board_state.update_position(Position(3, 4), None)
    board_state.update_position(Position(4, 4), None)
    assert board_state.positions[4][4] is None
    assert board_state.positions[3][4] is None
    board_state.reset()
    assert (
        board_state.positions[3][3] == DhungaType.x
        and board_state.positions[4][4] == DhungaType.x
    )
    assert (
        board_state.positions[3][4] == DhungaType.o
        and board_state.positions[4][3] == DhungaType.o
    )
