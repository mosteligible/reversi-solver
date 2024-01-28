package gameplay

import (
	"fmt"
	"reversi_solver/board"
	"reversi_solver/config"
	"reversi_solver/constants"
	"reversi_solver/node"
)

type SolutionTree struct {
	Children   []node.Node
	BoardState board.Board
}

func NewSolutionTree(size int8) SolutionTree {
	config.BoardSize = size
	board := board.NewBoard(size)
	playableMoves := board.GetAvailableMoves(constants.X)
	var childNodes []node.Node
	for _, move := range playableMoves {
		node := node.NewNode(move.Pos, constants.X, 0, board) // .Node{NodeType: move.NodeType, Level: 0, Board: board}
		node.Board.Update(move)
		// node.AddChildren()
		childNodes = append(childNodes, node)
	}
	return SolutionTree{Children: childNodes, BoardState: board}
}

func (st *SolutionTree) SolveRecursive(toLevel int) {
	for currentLevel := 1; currentLevel <= toLevel; currentLevel++ {

	}
}

func (st *SolutionTree) SolveLinear(toLevel int) {
	currentNodes := st.Children
	nextNodes := []node.Node{}
	fmt.Println(st.BoardState.ToString())
	for level := 1; level < toLevel; level++ {
		fmt.Printf("-- level %d - num-nodes: %d - nextNodes: %d - numLeafNodes: %d\nleaf node: ", level, len(currentNodes), len(nextNodes), config.NumLeafNodes)
		for _, childNode := range currentNodes {

			// fmt.Printf("%v ", childNode.LeafNode)
			if childNode.LeafNode {
				continue
			}
			childNode.AddChildren()
			// fmt.Printf("%d ", len(childNode.Childrens))
			nextNodes = append(nextNodes, childNode.Childrens...)
		}
		fmt.Println("")
		if len(nextNodes) == 0 {
			fmt.Printf("-- level %d is last for %d - num nodes: %d - leafNodes: %d\n", level, st.BoardState.Size, len(nextNodes), config.NumLeafNodes)
			break
		}
		currentNodes = nextNodes
		nextNodes = make([]node.Node, 0)
	}
}
