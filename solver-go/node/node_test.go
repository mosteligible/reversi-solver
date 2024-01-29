package node

import (
	"fmt"
	"reversi_solver/board"
	"reversi_solver/constants"
	"reversi_solver/core"
	"reversi_solver/utils"
	"testing"
)

func TestNewNode(t *testing.T) {
	board := board.NewBoard(8)
	newNode := NewNode(core.Position{RowNum: 1, ColNum: 2}, constants.X, 2, board)
	if newNode.LeafNode == true {
		t.Errorf("New node created with LeafNode as true")
	}
	if !newNode.Pos.Equals(core.Position{RowNum: 1, ColNum: 2}) {
		t.Errorf("New node position allocation issue")
	}
}

func TestAddChildren(t *testing.T) {
	board := board.NewBoard(8)
	avMoves := utils.FindAvailableMoves(board.Positions, constants.Y)
	board.Update(avMoves[0])
	newNode := NewNode(core.Position{RowNum: 3, ColNum: 2}, constants.Y, 1, board)
	newNode.AddChildren()
	if len(newNode.Childrens) != 3 {
		t.Errorf("num of children: %d - expected 3", len(newNode.Childrens))
	}
}

func TestToString(t *testing.T) {
	board := board.NewBoard(8)
	node := NewNode(core.Position{RowNum: 1, ColNum: 2}, constants.X, 1, board)
	expected := fmt.Sprintf(
		"Node(pos: %s, level: %d, nodeType: %d, leafNode: %v, childrens: %v)",
		node.Pos.ToString(), node.Level, node.NodeType, node.LeafNode, node.Childrens,
	)
	if node.ToString() != expected {
		t.Errorf("Node string mismatch:\n%s\n%s", node.ToString(), expected)
	}
}
