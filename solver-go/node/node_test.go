package node

import (
	"reversi_solver/board"
	"reversi_solver/constants"
	"reversi_solver/core"
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
