import config
from constants import DhungaType
from typing import List

from .board_state import BoardState
from .node import Node


class SolutionTree:
    def __init__(self, board_size: int = 8) -> None:
        self.root_node = None
        config.BOARD_SIZE = board_size
        self.board_state = BoardState(board_size)
        self.children: List[Node] = []
        self.levels = 0
        self.__init_childrens()

    def __init_childrens(self) -> None:
        playable_moves = self.board_state.get_available_moves(dhunga=DhungaType.x)
        for move in playable_moves:
            node = Node(
                pos=move.position,
                dhunga=DhungaType.x,
                level=0,
                board_state=self.board_state,
            )
            node.board_state.update(move)
            self.children.append(node)

    def update_children(self, node: Node, level: int) -> bool:
        """
        For given `level`, update the children for nodes at that level.

        params:
            level: int: represents level in solution tree
        """
        if node.leaf_node:
            print(f"level: {node.level} leaf node: {node.leaf_node}")
            return node.leaf_node
        if node.level + 1 == level:
            config.NODES += len(node.childrens)
            for child_node in node.childrens:
                # add children to child node
                child_node.add_childrens()
            return False
        else:
            """If not the required level, iterate through all the childrens
            at this level to get to the required level"""
            num_nodes = len(node.childrens)
            leaf_count = 0
            for child_node in node.childrens:
                leaf = self.update_children(child_node, level)
                if leaf:
                    leaf_count += 1
            if leaf_count == num_nodes:
                node.leaf_node = True
                return True
        return False

    def solve(self, num_levels: int) -> None:
        level = 1
        while level < num_levels:
            print(f"-- level: {level}")
            leaf_counts = 0
            for child_node in self.children:
                leaf = self.update_children(node=child_node, level=level)
                if leaf:
                    leaf_counts += 1
            print(f"-- level: {level} - nodes: {config.NODES}")
            if leaf_counts == len(self.children):
                break
            level += 1
        print(
            f"-- all leaf nodes by level: {level} for {config.BOARD_SIZE}x{config.BOARD_SIZE}"
        )

    def update_childrens_to_current_nodes(self) -> None:
        ...

    def solve_linear(self, num_levels: int) -> None:
        self.current_nodes = self.children
        level = 1
        self.next_nodes: List[Node] = []
        while level < num_levels:
            print(
                f"-- level: {level} - num-curr-nodes: {len(self.current_nodes)} - next_nodes: {len(self.next_nodes)} - leaf_nodes: {config.LEAF_NODES}"
            )
            for child_node in self.current_nodes:
                child_node.add_childrens()
                if child_node.leaf_node:
                    continue
                self.next_nodes.extend(child_node.childrens)
            if self.next_nodes == []:
                print(f"-- level: {level} is last for {config.BOARD_SIZE}")
                break
            self.current_nodes = self.next_nodes
            self.next_nodes: List[Node] = []
            level += 1
