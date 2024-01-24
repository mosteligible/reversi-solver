import config
from typing import List

from .board_state import BoardState
from .node import Node, RootNode


class SolutionTree:
    def __init__(self, board_size: int = 8) -> None:
        self.root_node = RootNode()
        config.BOARD_SIZE = board_size
        self.board_state = BoardState(board_size)
        self.children: List[Node] = []
        self.levels = 0

    def add_children(self, childrens: List[Node]) -> None:
        """
        Add children nodes. Children nodes previous node will
        be pointing to current level's children.
        """

    def solve(self) -> None:
        ...
