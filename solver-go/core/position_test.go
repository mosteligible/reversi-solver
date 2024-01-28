package core

import "testing"

func TestPositionToString(t *testing.T) {
	newPos := Position{1, 2}
	expected := "Position(1, 2)"
	if newPos.ToString() != expected {
		t.Errorf("Position strings not equal:\nexp: %s\ngot: %s", expected, newPos.ToString())
	}
}

func TestPositionEquals(t *testing.T) {
	newPos := Position{1, 2}
	target := Position{1, 2}
	if !(newPos.Equals(target)) {
		t.Errorf("Positions should be equal:\n%s\n%s", newPos.ToString(), target.ToString())
	}
}

func TestUnitDelta(t *testing.T) {
	pos := Position{2, 2}
	target := Position{0, 0}
	expected := Position{-1, -1}
	obtained := pos.UnitDelta(target)
	if !expected.Equals(obtained) {
		t.Errorf(
			"unit delta between %s and %s did not match.\n%s\n%s",
			pos.ToString(),
			target.ToString(),
			expected.ToString(),
			obtained.ToString(),
		)
	}

	target = Position{2, 0}
	expected = Position{0, -1}
	obtained = pos.UnitDelta(target)
	if !expected.Equals(obtained) {
		t.Errorf(
			"unit delta between %s and %s did not match.\n%s\n%s",
			pos.ToString(),
			target.ToString(),
			expected.ToString(),
			obtained.ToString(),
		)
	}

	target = Position{7, 0}
	expected = Position{1, -1}
	obtained = pos.UnitDelta(target)
	if !expected.Equals(obtained) {
		t.Errorf(
			"unit delta between %s and %s did not match.\n%s\n%s",
			pos.ToString(),
			target.ToString(),
			expected.ToString(),
			obtained.ToString(),
		)
	}

	target = Position{7, 7}
	expected = Position{1, 1}
	obtained = pos.UnitDelta(target)
	if !expected.Equals(obtained) {
		t.Errorf(
			"unit delta between %s and %s did not match.\n%s\n%s",
			pos.ToString(),
			target.ToString(),
			expected.ToString(),
			obtained.ToString(),
		)
	}
}
