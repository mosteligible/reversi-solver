package board

import (
	"reversi_solver/constants"
	"testing"
)

func TestNewBoard(t *testing.T) {
	newBoard := NewBoard(8)
	if newBoard.Size != 8 {
		t.Errorf("Board size allocation error!")
	}
	if newBoard.Positions[3][3] != constants.X || newBoard.Positions[4][4] != constants.X {
		t.Errorf("Board position allocation error!")
	}
	if newBoard.Positions[3][4] != constants.Y || newBoard.Positions[4][3] != constants.Y {
		t.Errorf("Board position allocation error!")
	}
}
