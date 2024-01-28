package core

import "fmt"

type Position struct {
	RowNum int8
	ColNum int8
}

type CoreSignature interface {
	Equals(CoreSignature) bool
	ToString() string
}

func (pos *Position) UnitDelta(target Position) Position {
	return Position{
		unitMovement(pos.RowNum, target.RowNum),
		unitMovement(pos.ColNum, target.ColNum),
	}
}

func (pos *Position) Equals(target Position) bool {
	return pos.RowNum == target.RowNum && pos.ColNum == target.ColNum
}

func (pos *Position) ToString() string {
	return fmt.Sprintf("Position(%d, %d)", pos.RowNum, pos.ColNum)
}

func unitMovement(origin int8, target int8) int8 {
	if origin < target {
		return 1
	} else if origin > target {
		return -1
	} else {
		return 0
	}
}
