package core

import (
	"fmt"
	"reversi_solver/constants"
)

func GetNextPlayer(currPlayer int8) int8 {
	if currPlayer == constants.X {
		return constants.Y
	} else if currPlayer == constants.Y {
		return constants.X
	} else {
		panic(fmt.Sprintf("Invalid player type: %d\n", currPlayer))
	}
}
