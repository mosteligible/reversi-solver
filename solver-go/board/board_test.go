package board

import (
	"reversi_solver/constants"
	"reversi_solver/utils"
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

func TestLoadBoard(t *testing.T) {
	newBoard := NewBoard(8)
	positions := utils.GeneratePositions(8)
	newBoard.LoadBoard(positions)
	if newBoard.Positions[3][3] != 0 && newBoard.Positions[4][4] != 0 {
		t.Errorf("Load Board position error!")
	}
	if newBoard.Positions[4][3] != 0 && newBoard.Positions[3][4] != 0 {
		t.Errorf("Load Board position error!")
	}
}

func TestToString(t *testing.T) {
	newBoard := NewBoard(8)
	expected := `    0   1   2   3   4   5   6   7   
0 |   |   |   |   |   |   |   |   | 
-----------------------------------
1 |   |   |   |   |   |   |   |   | 
-----------------------------------
2 |   |   |   |   |   |   |   |   | 
-----------------------------------
3 |   |   |   | x | o |   |   |   | 
-----------------------------------
4 |   |   |   | o | x |   |   |   | 
-----------------------------------
5 |   |   |   |   |   |   |   |   | 
-----------------------------------
6 |   |   |   |   |   |   |   |   | 
-----------------------------------
7 |   |   |   |   |   |   |   |   | 
-----------------------------------
`
	if newBoard.ToString() != expected {
		t.Errorf("String representation of board does not match:\n%s%s", newBoard.ToString(), expected)
	}
}
