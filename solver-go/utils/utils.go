package utils

import (
	"fmt"
	"reversi_solver/config"
	"reversi_solver/constants"
	"reversi_solver/core"

	"golang.org/x/exp/slices"
)

func FindNextMatchingNode(row []int8, nodeType int8) (bool, int8) {
	if len(row) == 0 {
		return false, -1
	}
	if row[0] == constants.Default || row[0] == nodeType {
		return false, -1
	}
	for index, dh := range row[1:] {
		if dh == constants.Default {
			break
		} else if (dh != constants.Default) && (dh == nodeType) {
			return true, int8(index) + int8(1)
		}
	}
	return false, -1
}

func CheckInLine(row []int8, pos int8, nodeType int8) []int8 {
	var matches []int8 = []int8{}
	var match bool
	var index int8
	row_len := len(row)
	if ((pos + 1) < int8(row_len)) && (row[pos+1] != constants.Default) {
		match, index = FindNextMatchingNode(row[pos+1:], nodeType)
		if match {
			matches = append(matches, index+pos+int8(1))
		}
	}

	if !(pos-1 < 0) && row[pos-1] != constants.Default {
		var elemLeftToPos []int8 = make([]int8, pos)
		copy(elemLeftToPos, row[:pos])
		slices.Reverse(elemLeftToPos)
		match, index = FindNextMatchingNode(elemLeftToPos, nodeType)
		if match {
			matches = append(matches, pos-index-int8(1))
		}
	}
	return matches
}

func GetDiaognalsAsRow(positions [][]int8, pos core.Position) ([]int8, int8, []int8, int8) {
	var posToLeftTop, posToRightDown, posToLeftDown, posToRightUp []int8
	var index, leftTopToRightDownIndex, leftDownToRightUpIndex int8
	item := positions[pos.RowNum][pos.ColNum]
	for index = 1; index < config.BoardSize; index++ {
		if pos.RowNum-int8(index) >= 0 && pos.ColNum-int8(index) >= 0 {
			posToLeftTop = append(posToLeftTop, positions[pos.RowNum-index][pos.ColNum-index])
		}
		if pos.RowNum+index < config.BoardSize && pos.ColNum-index >= 0 {
			posToLeftDown = append(posToLeftDown, positions[pos.RowNum+index][pos.ColNum-index])
		}
		if pos.RowNum+index < config.BoardSize && pos.ColNum+index < config.BoardSize {
			posToRightDown = append(posToRightDown, positions[pos.RowNum+index][pos.ColNum+index])
		}
		if pos.RowNum-index >= 0 && pos.ColNum+index < config.BoardSize {
			posToRightUp = append(posToRightUp, positions[pos.RowNum-index][pos.ColNum+index])
		}
	}
	// reverse pos to left top elements and pos to left down elements
	slices.Reverse(posToLeftTop)
	slices.Reverse(posToLeftDown)
	leftTopToRightDownIndex = int8(len(posToLeftTop))
	leftDownToRightUpIndex = int8(len(posToLeftDown))
	posToLeftTop = append(posToLeftTop, item)
	posToLeftTop = append(posToLeftTop, posToRightDown...)
	posToLeftDown = append(posToLeftDown, item)
	posToLeftDown = append(posToLeftDown, posToRightUp...)
	return posToLeftTop, leftTopToRightDownIndex, posToLeftDown, leftDownToRightUpIndex
}

func CheckDiaognals(pos core.Position, positions [][]int8, nodeType int8) ([]core.Position, []core.Position) {
	leftTopToRightDown, pos1Index, leftDownToRightUp, pos2Index := GetDiaognalsAsRow(positions, pos)
	leftTopToRightDownIndexes := CheckInLine(leftTopToRightDown, pos1Index, nodeType)
	leftDownToRightUpIndexes := CheckInLine(leftDownToRightUp, pos2Index, nodeType)
	var intPos core.Position
	var diag1, diag2 []core.Position
	for _, val := range leftTopToRightDownIndexes {
		intPos = core.Position{
			RowNum: pos.RowNum + val - pos1Index,
			ColNum: val,
		}
		diag1 = append(diag1, intPos)
	}
	for _, val := range leftDownToRightUpIndexes {
		intPos = core.Position{
			RowNum: pos.RowNum - (val - pos2Index),
			ColNum: val,
		}
		diag2 = append(diag2, intPos)
	}
	return diag1, diag2
}

func GetPositionsFromIndexes(indexes []int8, rowOrCol string, fixedIndex int8) []core.Position {
	var retval []core.Position
	retval = []core.Position{}
	switch rowOrCol {
	case "row":
		for _, val := range indexes {
			retval = append(retval, core.Position{RowNum: fixedIndex, ColNum: val})
		}
	case "col":
		for _, val := range indexes {
			retval = append(retval, core.Position{RowNum: val, ColNum: fixedIndex})
		}
	}
	return retval
}

func GetColumn(positions [][]int8, colIndex int8) []int8 {
	var column []int8 = []int8{}
	for _, row := range positions {
		column = append(column, row[colIndex])
	}
	return column
}

func PlayableMovesFromPos(positions [][]int8, nodeType int8, pos core.Position) (core.PositionsManager, bool) {
	var match bool = false
	indexesInLine := CheckInLine(positions[pos.RowNum], pos.ColNum, nodeType)
	linearPositions := GetPositionsFromIndexes(indexesInLine, "row", pos.RowNum)
	column := GetColumn(positions, pos.ColNum)
	verticalIndexes := CheckInLine(column, pos.RowNum, nodeType)
	verticalPositions := GetPositionsFromIndexes(verticalIndexes, "col", pos.ColNum)
	leftTopToRightBottom, leftBottomToRightTop := CheckDiaognals(pos, positions, nodeType)
	linearPositions = append(linearPositions, verticalPositions...)
	linearPositions = append(linearPositions, leftTopToRightBottom...)
	linearPositions = append(linearPositions, leftBottomToRightTop...)
	if len(linearPositions) > 0 {
		match = true
	}
	pm := core.PositionsManager{
		Pos:             pos,
		NodeType:        nodeType,
		TargetPositions: linearPositions,
	}
	return pm, match
}

func FindAvailableMoves(positions [][]int8, nodeType int8) []core.PositionsManager {
	var availableMoves []core.PositionsManager = []core.PositionsManager{}
	for rowNum, row := range positions {
		for colNum, col := range row {
			if col == constants.Default {
				currPos := core.Position{RowNum: int8(rowNum), ColNum: int8(colNum)}
				playableMove, isPlayable := PlayableMovesFromPos(positions, nodeType, currPos)
				if isPlayable {
					availableMoves = append(availableMoves, playableMove)
				}
			}
		}
	}
	return availableMoves
}

func GeneratePositions(size int) [][]int8 {
	var positions [][]int8 = [][]int8{}
	var row []int8
	for i := 0; i < size; i++ {
		row = make([]int8, size)
		positions = append(positions, row)
	}
	return positions
}

func AssertPositionSlicesEqual(s1 []core.Position, s2 []core.Position) {
	if len(s1) != len(s2) {
		panic(fmt.Sprintf("Two slices are not equal: %v - %v", s1, s2))
	}
	for index := 0; index < len(s1); index++ {
		if !(s1[index].Equals(s2[index])) {
			panic(fmt.Sprintf("Two slices are not equal: %v - %v", s1, s2))
		}
	}
}
