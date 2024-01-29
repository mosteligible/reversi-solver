package core

import (
	"reversi_solver/constants"
	"testing"
)

func TestEquals(t *testing.T) {
	targets := []Position{{1, 2}, {2, 3}, {3, 4}}
	nType := constants.X
	pos := Position{0, 0}
	second := PositionsManager{
		Pos:             Position{0, 0},
		NodeType:        constants.X,
		TargetPositions: targets,
	}
	new := PositionsManager{
		Pos:             pos,
		NodeType:        nType,
		TargetPositions: targets,
	}
	if !new.Equals(second) {
		t.Errorf("PositionManager equality operation issue!")
	}
}
