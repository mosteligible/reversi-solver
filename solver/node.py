import copy
from .board_state import BoardState
from .player import Player


class RootNode:
    __instances = 0

    def __init__(self) -> None:
        if RootNode.__instances == 0:
            RootNode.__instances += 1
        else:
            raise ValueError("Attempted to make more than 1 root node!")


class Node:
    node_types = []

    def __init__(
        self, player: Player, level: int, board_state: BoardState, prev: "Node"
    ) -> None:
        self.previous_node = prev
        self.childrens = []
        if player.dhunga in self.node_types:
            raise ValueError("Duplicate dhunga selected, choose different dhunga!")
        self.node_type = player.dhunga
        self.level = level
        self.board_state = copy.deepcopy(board_state)

    def add_next_node(self, next_node: "Node") -> None:
        self.next_nodes.append(next_node)
