package node

import (
	"fmt"
	"reversi_solver/board"
	"reversi_solver/config"
	"reversi_solver/core"
)

type Node struct {
	Pos       core.Position
	NodeType  int8
	Level     uint32
	LeafNode  bool
	Board     board.Board
	Childrens []Node
}

func NewNode(pos core.Position, nodeType int8, level uint32, parentBoard board.Board) Node {
	nodeBoard := board.NewBoard(parentBoard.Size)
	nodeBoard.LoadBoard(parentBoard.Positions)
	newNode := Node{
		Pos:       pos,
		NodeType:  nodeType,
		Level:     level,
		Board:     nodeBoard,
		Childrens: []Node{},
		LeafNode:  false,
	}
	return newNode
}

func (n *Node) AddChildren() bool {
	var nodeType int8 = core.GetNextPlayer(n.NodeType)
	if len(n.Childrens) > 0 {
		return false
	}
	playableMoves := n.Board.GetAvailableMoves(nodeType)
	if len(playableMoves) == 0 {
		nodeType = core.GetNextPlayer(nodeType)
		playableMoves = n.Board.GetAvailableMoves(nodeType)
	}
	if len(playableMoves) == 0 {
		n.LeafNode = true
		config.NumLeafNodes += 1
		return n.LeafNode
	}
	n.Childrens = []Node{}
	for _, move := range playableMoves {
		childNode := NewNode(move.Pos, nodeType, n.Level+1, n.Board)
		childNode.Board.Update(move)
		n.Childrens = append(n.Childrens, childNode)
	}
	return n.LeafNode
}

func (n *Node) ToString() string {
	return fmt.Sprintf(
		"Node(pos: %s, level: %d, nodeType: %d, leafNode: %v childrens: %v)", n.Pos.ToString(), n.Level, n.NodeType, n.LeafNode, n.Childrens,
	)
}
