package main

import (
	"fmt"
	"reversi_solver/gameplay"
	"time"
)

func main() {
	fmt.Println("-------------- BEGIN --------------")
	start := time.Now()
	st := gameplay.NewSolutionTree(5)
	st.SolveLinear(15)
	fmt.Printf("taken time: %v", time.Since(start))
}
