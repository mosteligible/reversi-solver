import config
from constants import DhungaType
from typing import List

from .board_state import BoardState
from .node import Node, RootNode
from .solution_helpers import SolutionHelper


class SolutionTree:
    def __init__(self, board_size: int = 8) -> None:
        self.root_node = RootNode()
        config.BOARD_SIZE = board_size
        self.board_state = BoardState(board_size)
        self.children: List[Node] = []
        self.levels = 0
        self.__init_childrens()

    def __init_childrens(self) -> None:
        playable_moves = self.board_state.get_available_moves(dhunga=DhungaType.x)
        for move in playable_moves:
            node = Node(
                dhunga=DhungaType.x,
                level=0,
                board_state=self.board_state,
            )
            node.board_state.update(move)
            node.add_childrens()
            self.children.append(node)

    def update_children(self, node: Node, level: int) -> bool:
        """
        For given `level`, update the children for nodes at that level.

        params:
            level: int: represents level in solution tree
        """
        if node.leaf_node:
            print(f"level: {level} leaf node: {node.leaf_node}")
            print(node.board_state)
            print(f"{'x'*60}")
            return node.leaf_node
        if node.level + 1 == level:
            for child_node in node.childrens:
                # add children to child node
                child_node.add_childrens()
            return False
        else:
            """If not the required level, iterate through all the childrens
            at this level to get to the required level"""
            for child_node in node.childrens:
                self.update_children(child_node, level)
        return False

    def solve(self) -> None:
        level = 1
        while level < 61:
            print(f"-- level: {level}")
            for child_node in self.children:
                self.update_children(node=child_node, level=level)

            level += 1
