from .player import Player


class Node:
    node_types = []
    def __init__(self, player: Player, prev: "Node" = None) -> None:
        self.previous_node = prev
        self.next_nodes = []
        if player.dhunga in self.node_types:
            raise ValueError("Duplicate dhunga selected, choose different dhunga!")
        self.node_type = player.dhunga

    def add_next_node(self, next_node: "Node") -> None:
        self.next_nodes.append(next_node)
