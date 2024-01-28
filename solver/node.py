import time
import copy
import config
from constants import DhungaType
from typing import List
from .board_state import BoardState
from .position import Position


class RootNode:
    __instances = 0

    def __init__(self) -> None:
        if RootNode.__instances == 0:
            RootNode.__instances += 1
        else:
            raise ValueError("Attempted to make more than 1 root node!")


class Node:
    def __init__(
        self, pos: Position, dhunga: DhungaType, level: int, board_state: BoardState
    ) -> None:
        """
        A node in a SolutionTree.

        params:
            dhunga: DhungaType: represents the dhunga being played on current Node
            level: int: represents level of current Node in SolutionTree
            board_state: BoardState: represents state of board au current Node
        """
        self.childrens: List["Node"] = []
        self.pos = pos
        self.node_type = dhunga
        self.level = level
        start = time.time()
        self.board_state = copy.deepcopy(board_state)
        config.COPY_TIME += time.time() - start
        self.leaf_node = False

    def add_childrens(self) -> bool:
        self.childrens: List["Node"] = []
        dhunga = DhungaType.x if self.node_type == DhungaType.o else DhungaType.o
        playable_moves = self.board_state.get_available_moves(dhunga=dhunga)
        if not playable_moves:
            dhunga = self.node_type
            playable_moves = self.board_state.get_available_moves(dhunga=dhunga)
        if playable_moves == []:
            self.leaf_node = True
            config.LEAF_NODES += 1
        for move in playable_moves:
            child_node = Node(move.position, dhunga, self.level + 1, self.board_state)
            child_node.board_state.update(move)
            self.childrens.append(child_node)
        return self.leaf_node

    def __repr__(self) -> str:
        return f"Node(pos: {self.pos}, level:{self.level}, dhunga: {self.node_type}, childrens: {self.childrens})"
