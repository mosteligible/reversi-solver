package utils

import (
	"fmt"
	"reversi_solver/config"
	"reversi_solver/constants"
	"reversi_solver/core"
	"testing"
)

func TestFindNextMatchingNode(t *testing.T) {
	row := []int8{0, 0, 1, 2, 0}
	match, num := FindNextMatchingNode(row, constants.X)
	if match == false && num != -1 {
		t.Errorf("result was incorrect")
	}
	row = []int8{1, 0, 1, 2, 0}
	match, num = FindNextMatchingNode(row, constants.X)
	if match == true && num != -1 {
		t.Errorf("result was incorrect- match: %v - num: %d", match, num)
	}
	row = []int8{0, 1, 1, 2, 0}
	match, num = FindNextMatchingNode(row, constants.X)
	if match == true && num != -1 {
		t.Errorf("result was incorrect- match: %v - num: %d", match, num)
	}
	row = []int8{2, 1, 1, 2, 0}
	match, num = FindNextMatchingNode(row, constants.X)
	if match == false && num != 1 {
		t.Errorf("result was incorrect- match: %v - num: %d", match, num)
	}
	row = []int8{2, 1, 1, 2, 0}
	match, num = FindNextMatchingNode(row, constants.Y)
	if match == true && num != -1 {
		t.Errorf("result was incorrect- match: %v - num: %d", match, num)
	}
	row = []int8{1, 1, 2, 2, 0}
	match, num = FindNextMatchingNode(row, constants.Y)
	if match == true && num != 2 {
		t.Errorf("result was incorrect- match: %v - num: %d", match, num)
	}
}

func TestCheckInLine(t *testing.T) {
	row := []int8{0, 1, 2, 0, 0, 0}
	matches := CheckInLine(row, int8(3), constants.X)
	if matches[0] != int8(1) {
		t.Errorf("result was incorrect- matches: %v - row: %v", matches, row)
	}
	matches = CheckInLine(row, int8(0), constants.X)
	if !(len(matches) == 0) {
		t.Errorf("result was incorrect- matches: %v - row: %v", matches, row)
	}
	row = []int8{0, 1, 2, 0, 2, 1}
	matches = CheckInLine(row, int8(3), constants.X)
	if len(matches) != 2 {
		t.Errorf("result was incorrect- matches: %v - row: %v", matches, row)
	}
	matches = CheckInLine(row, int8(0), constants.Y)
	fmt.Println(matches)
	if matches[0] != int8(2) {
		t.Errorf("result was incorrect- matches: %v - row: %v", matches, row)
	}
}

func assertSlicesEqual[T comparable](slice1 []T, slice2 []T) {
	for index, item := range slice1 {
		if item != slice2[index] {
			panic(fmt.Sprintf("%v slice not equal to\n%v", slice1, slice2))
		}
	}
}

func TestGetDiagonals(t *testing.T) {
	config.BoardSize = 5
	positions := [][]int8{
		{1, 2, 3, 4, 5},
		{6, 7, 8, 9, 10},
		{11, 12, 13, 14, 15},
		{16, 17, 18, 19, 20},
		{21, 22, 23, 24, 25},
	}
	pos := core.Position{RowNum: 0, ColNum: 0}
	expected_diag1 := []int8{1, 7, 13, 19, 25}
	expected_diag2 := []int8{1}
	diag1, pos1, diag2, pos2 := GetDiaognalsAsRow(positions, pos)
	assertSlicesEqual[int8](expected_diag1, diag1)
	assertSlicesEqual[int8](expected_diag2, diag2)
	if pos1 != 0 || pos2 != 0 {
		t.Errorf("index of positional elements wrong!")
	}

	pos = core.Position{RowNum: 0, ColNum: 1}
	expected_diag1 = []int8{2, 8, 14, 20}
	expected_diag2 = []int8{6, 2}
	diag1, pos1, diag2, pos2 = GetDiaognalsAsRow(positions, pos)
	assertSlicesEqual[int8](expected_diag1, diag1)
	assertSlicesEqual[int8](expected_diag2, diag2)
	if pos1 != 0 || pos2 != 1 {
		t.Errorf("index of positional elements wrong!")
	}

	pos = core.Position{RowNum: 0, ColNum: 4}
	expected_diag1 = []int8{5}
	expected_diag2 = []int8{21, 17, 13, 9, 5}
	diag1, pos1, diag2, pos2 = GetDiaognalsAsRow(positions, pos)
	assertSlicesEqual[int8](expected_diag1, diag1)
	assertSlicesEqual[int8](expected_diag2, diag2)
	if pos1 != 0 || pos2 != 4 {
		t.Errorf("index of positional elements wrong! pos1(%d, 0) - pos2(%d, 4)", pos1, pos2)
	}
}

func TestGetColumn(t *testing.T) {
	positions := [][]int8{
		{1, 2, 3, 4, 5},
		{6, 7, 8, 9, 10},
		{11, 12, 13, 14, 15},
	}
	expected := [][]int8{
		{1, 6, 11},
		{2, 7, 12},
		{3, 8, 13},
		{4, 9, 14},
		{5, 10, 15},
	}
	col := GetColumn(positions, 2)
	assertSlicesEqual[int8](col, expected[2])
	col = GetColumn(positions, 3)
	assertSlicesEqual[int8](col, expected[3])
	col = GetColumn(positions, 4)
	assertSlicesEqual[int8](col, expected[4])
}

func TestCheckDiagonals(t *testing.T) {
	positions := GeneratePositions(8)
	positions[0][0] = constants.X
	positions[1][1] = constants.Y
	positions[2][2] = constants.Y
	expected1 := []core.Position{{RowNum: 0, ColNum: 0}}
	expected2 := []core.Position{}
	diag1, diag2 := CheckDiaognals(core.Position{RowNum: 3, ColNum: 3}, positions, constants.X)
	AssertPositionSlicesEqual(expected1, diag1)
	AssertPositionSlicesEqual(expected2, diag2)
}

func assertPosMgrEqual(sl1 []core.PositionsManager, sl2 []core.PositionsManager) bool {
	if len(sl1) != len(sl2) {
		return false
	}
	for index, item := range sl1 {
		if !item.Equals(sl2[index]) {
			return false
		}
	}
	return true
}

func TestFindAvailableMoves(t *testing.T) {
	positions := GeneratePositions(8)
	positions[0][0] = 1
	positions[1][1] = 2
	positions[3][3] = 2
	positions[4][4] = 1
	expected := []core.PositionsManager{
		{Pos: core.Position{RowNum: 2, ColNum: 2},
			NodeType:        constants.X,
			TargetPositions: []core.Position{{RowNum: 4, ColNum: 4}, {RowNum: 0, ColNum: 0}}},
	}
	avMoves := FindAvailableMoves(positions, constants.X)
	if !assertPosMgrEqual(expected, avMoves) {
		t.Errorf("Available moves not equal:\n%v\n%v", expected, avMoves)
	}
	positions[0][2] = 1
	positions[1][2] = 2
	expected = []core.PositionsManager{
		{Pos: core.Position{RowNum: 2, ColNum: 0},
			NodeType: constants.X,
			TargetPositions: []core.Position{
				{RowNum: 0, ColNum: 2},
			}},
		{Pos: core.Position{RowNum: 2, ColNum: 2},
			NodeType: constants.X,
			TargetPositions: []core.Position{
				{RowNum: 0, ColNum: 2},
				{RowNum: 4, ColNum: 4},
				{RowNum: 0, ColNum: 0},
			}},
	}
	avMoves = FindAvailableMoves(positions, constants.X)
	if !assertPosMgrEqual(expected, avMoves) {
		t.Errorf("Available moves not equal:\n%v\n%v", expected, avMoves)
	}
	positions[2][0] = 1
	positions[2][1] = 2
	expected = []core.PositionsManager{
		{Pos: core.Position{RowNum: 2, ColNum: 2},
			NodeType: constants.X,
			TargetPositions: []core.Position{
				{RowNum: 2, ColNum: 0},
				{RowNum: 0, ColNum: 2},
				{RowNum: 4, ColNum: 4},
				{RowNum: 0, ColNum: 0},
			}},
	}
	avMoves = FindAvailableMoves(positions, constants.X)
	if !assertPosMgrEqual(expected, avMoves) {
		t.Errorf("Available moves not equal:\n%v\n%v", expected, avMoves)
	}
}
