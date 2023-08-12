import spec
import exercise_5


def test_show_multiples_of_3():
  expected_print = "\n".join((
    "3 x 1 = 3",
    "3 x 2 = 6",
    "3 x 3 = 9",
    "3 x 4 = 12",
    "3 x 5 = 15",
    "3 x 6 = 18",
    "3 x 7 = 21",
    "3 x 8 = 24",
    "3 x 9 = 27",
    "3 x 10 = 30\n"
  ))

  spec.expect_print(exercise_5.main, expected_print)