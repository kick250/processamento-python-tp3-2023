import spec
import exercise_6


def test_get_numbers():
  assert exercise_6.get_numbers() == [
    1,
    8,
    27,
    64,
    125,
    216,
    343,
    512,
    729,
    1000
  ]