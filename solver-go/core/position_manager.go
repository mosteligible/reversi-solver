package core

import (
	"fmt"
	"reversi_solver/config"
)

type PositionsManager struct {
	Pos             Position
	NodeType        int8
	TargetPositions []Position
}

func (pm *PositionsManager) GetPositionsInBetween(target Position) []Position {
	var delta Position = pm.Pos.UnitDelta(target)
	var currentPosition Position = Position{pm.Pos.RowNum, pm.Pos.ColNum}
	var posInBetween []Position = []Position{}
	count := 0
	for {
		currentPosition = Position{
			RowNum: currentPosition.RowNum + delta.RowNum,
			ColNum: currentPosition.ColNum + delta.ColNum,
		}
		if currentPosition.Equals(target) || count > 20 {
			break
		}
		if (currentPosition.RowNum >= config.BoardSize || currentPosition.ColNum >= config.BoardSize) || (currentPosition.RowNum < 0 || currentPosition.ColNum < 0) {
			return []Position{}
		}
		posInBetween = append(posInBetween, currentPosition)
		count++
	}
	return posInBetween
}

func (pm *PositionsManager) GetPositionsToSwitch() []Position {
	var positionsToSwitch []Position = []Position{}
	var inBetween []Position
	for _, target := range pm.TargetPositions {
		inBetween = pm.GetPositionsInBetween(target)
		positionsToSwitch = append(positionsToSwitch, inBetween...)
	}
	return positionsToSwitch
}

func (pm *PositionsManager) ToString() string {
	return fmt.Sprintf("PositionManager(%v %d \nTargetPositions: %v)", pm.Pos, pm.NodeType, pm.TargetPositions)
}

func (pm *PositionsManager) Equals(target PositionsManager) bool {
	if len(target.TargetPositions) != len(pm.TargetPositions) {
		return false
	}
	for index := 0; index < len(pm.TargetPositions); index++ {
		if pm.TargetPositions[index] != target.TargetPositions[index] {
			return false
		}
	}
	return pm.Pos.Equals(target.Pos) && pm.NodeType == target.NodeType
}
