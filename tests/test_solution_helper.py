import config
from constants import DhungaType
from solver.board_state import BoardState
from solver.position import Position
from solver.solution_helpers import SolutionHelper


def test_find_next_dhunga_match() -> None:
    row = [None] * 5
    assert SolutionHelper.find_next_dhunga_match(row, DhungaType.o) == (False, -1)
    row[0] = DhungaType.x
    assert SolutionHelper.find_next_dhunga_match(row, DhungaType.o) == (False, -1)
    row[1] = DhungaType.o
    assert SolutionHelper.find_next_dhunga_match(row, DhungaType.o) == (True, 1)
    row = [None] * 5
    row[0] = DhungaType.x
    row[1] = DhungaType.x
    row[2] = DhungaType.o
    assert SolutionHelper.find_next_dhunga_match(row, DhungaType.o) == (True, 2)


def test_check_in_line_edges() -> None:
    row = [None] * 8
    assert SolutionHelper.check_in_line(row, 0, DhungaType.x) == []
    assert SolutionHelper.check_in_line(row, 1, DhungaType.x) == []
    assert SolutionHelper.check_in_line(row, 2, DhungaType.x) == []
    assert SolutionHelper.check_in_line(row, 3, DhungaType.x) == []
    row[1] = DhungaType.x
    row[2] = DhungaType.x
    row[3] = DhungaType.o
    row[4] = DhungaType.o
    assert SolutionHelper.check_in_line(row, 0, DhungaType.x) == []
    assert SolutionHelper.check_in_line(row, 0, DhungaType.o) == [3]
    assert SolutionHelper.check_in_line(row, 5, DhungaType.o) == []
    assert SolutionHelper.check_in_line(row, 5, DhungaType.x) == [2]
    row[5] = DhungaType.x
    assert SolutionHelper.check_in_line(row, 6, DhungaType.o) == [4]


def test_check_in_line_between() -> None:
    row = [None] * 8
    row[0] = DhungaType.x
    row[1] = DhungaType.o
    row[2] = DhungaType.o
    row[5] = DhungaType.x
    row[6] = DhungaType.x
    row[7] = DhungaType.o
    assert SolutionHelper.check_in_line(row, 3, DhungaType.x) == [0]
    assert SolutionHelper.check_in_line(row, 3, DhungaType.o) == []
    assert SolutionHelper.check_in_line(row, 4, DhungaType.o) == [7]
    assert SolutionHelper.check_in_line(row, 4, DhungaType.x) == []


def test_check_diagonals() -> None:
    board = BoardState()
    board.update_position(Position(5, 5), DhungaType.o)
    assert SolutionHelper.check_diaognals(
        Position(2, 2), board.positions, DhungaType.o
    ) == ([Position(5, 5)], [])
    assert SolutionHelper.check_diaognals(
        Position(2, 2), board.positions, DhungaType.x
    ) == ([], [])

    board.update_position(Position(5, 4), DhungaType.x)
    assert SolutionHelper.check_diaognals(
        Position(3, 2), board.positions, DhungaType.x
    ) == ([Position(5, 4)], [])
    board.update_position(Position(5, 2), DhungaType.x)
    assert SolutionHelper.check_diaognals(
        Position(2, 5), board.positions, DhungaType.x
    ) == ([], [Position(5, 2)])
    board.update_position(Position(1, 6), DhungaType.o)
    board.update_position(Position(0, 7), DhungaType.x)
    assert SolutionHelper.check_diaognals(
        Position(2, 5), board.positions, DhungaType.x
    ) == ([], [Position(0, 7), Position(5, 2)])

    # edges check
    board = BoardState()
    board.update_position(Position(0, 0), DhungaType.x)
    board.update_position(Position(1, 1), DhungaType.o)
    print(board)
    assert SolutionHelper.check_diaognals(
        Position(0, 0), board.positions, DhungaType.x
    ) == ([], [])
    assert SolutionHelper.check_diaognals(
        Position(2, 2), board.positions, DhungaType.x
    ) == ([Position(0, 0)], [])
    # switch dhungas
    board.update_position(Position(0, 7), DhungaType.o)
    board.update_position(Position(1, 6), DhungaType.x)
    print(board)
    assert SolutionHelper.check_diaognals(
        Position(0, 7), board.positions, DhungaType.o
    ) == ([], [])
    assert SolutionHelper.check_diaognals(
        Position(2, 5), board.positions, DhungaType.o
    ) == ([], [Position(0, 7)])


def test_get_diagolans_as_row() -> None:
    config.BOARD_SIZE = 5
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    # non-edge position to get row from
    pos = Position(1, 1)
    expected = ([1, 7, 13, 19, 25], 1, [11, 7, 3], 1)
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected
    pos = Position(0, 1)
    expected = ([2, 8, 14, 20], 0, [6, 2], 1)
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected
    pos = Position(1, 2)
    expected = ([2, 8, 14, 20], 1, [16, 12, 8, 4], 2)
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected

    # edge position to get row from
    pos = Position(0, 0)
    expected = ([1, 7, 13, 19, 25], 0, [1], 0)
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected
    pos = Position(4, 4)
    expected = ([1, 7, 13, 19, 25], 4, [25], 0)
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected
    pos = Position(0, 4)
    expected = ([5], 0, [21, 17, 13, 9, 5], 4)
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected
    pos = Position(4, 0)
    expected = (
        [21],
        0,
        [21, 17, 13, 9, 5],
        0,
    )
    assert SolutionHelper.get_diagonals_as_row(matrix, pos) == expected


def test_get_column_as_row() -> None:
    matrix = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 0]]
    expected = [[1, 5, 6], [2, 4, 7], [3, 3, 8], [4, 2, 9], [5, 1, 0]]
    assert SolutionHelper.get_matrix_col(matrix, 2) == expected[2]
