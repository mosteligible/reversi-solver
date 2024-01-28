package board

import (
	"fmt"
	"reversi_solver/config"
	"reversi_solver/constants"
	"reversi_solver/core"
	"reversi_solver/utils"
	"strings"
)

type Board struct {
	Size      int8
	Positions [][]int8
}

func NewBoard(size int8) Board {
	config.BoardSize = size
	var positions [][]int8 = [][]int8{}
	var row []int8
	for i := 0; i < int(size); i++ {
		row = make([]int8, size)
		positions = append(positions, row)
	}
	board := Board{Size: size, Positions: positions}
	board.setupBoard()
	return board
}

func (b *Board) setupBoard() {
	var mid int8 = b.Size / 2
	b.Positions[mid-1][mid-1] = constants.X
	b.Positions[mid-1][mid] = constants.Y
	b.Positions[mid][mid-1] = constants.Y
	b.Positions[mid][mid] = constants.X
}

func (b *Board) GetAvailableMoves(nodeType int8) []core.PositionsManager {
	return utils.FindAvailableMoves(b.Positions, nodeType)
}

func (b *Board) LoadBoard(positions [][]int8) {
	duplicate := make([][]int8, config.BoardSize)
	for index, row := range positions {
		duplicate[index] = make([]int8, config.BoardSize)
		copy(duplicate[index], row)
	}
	b.Positions = duplicate
}

func (b *Board) UpdatePosition(pos core.Position, nodeType int8) {
	b.Positions[pos.RowNum][pos.ColNum] = nodeType
}

func (b *Board) Update(playedPosition core.PositionsManager) {
	posToSwitch := playedPosition.GetPositionsToSwitch()
	for _, pos := range posToSwitch {
		b.UpdatePosition(pos, playedPosition.NodeType)
	}
	b.UpdatePosition(playedPosition.Pos, playedPosition.NodeType)
}

func (b *Board) ToString() string {
	retval := "    "
	for i := 0; i < int(b.Size); i++ {
		retval += fmt.Sprintf("%d   ", i)
	}
	retval = fmt.Sprintf("%s\n", retval)
	var ch string
	for i, row := range b.Positions {
		rowStr := " | "
		for _, val := range row {
			if val == 1 {
				ch = "x"
			} else if val == 2 {
				ch = "o"
			} else {
				ch = " "
			}
			if val != constants.Default {
				rowStr = fmt.Sprintf("%s%s | ", rowStr, ch)
			} else {
				rowStr = fmt.Sprintf("%s%s | ", rowStr, " ")
			}
		}
		rowStr = fmt.Sprintf("%d%s\n%s", i, rowStr, strings.Repeat("-", (int(b.Size)-1)*4+7))
		retval = fmt.Sprintf("%s%s\n", retval, rowStr)
	}
	return retval
}
