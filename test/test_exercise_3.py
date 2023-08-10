import spec
import exercise_3


def test_return_all_numbers_up_1000000():
  assert exercise_3.get_numbers() == tuple(range(1, 1000000 + 1))

def test_print_sum():
  expected_print = '\n'.join((str(i) for i in exercise_3.get_numbers())) + "\n"
  expected_print += "500000500000\n"
  spec.expect_print(exercise_3.main, expected_print)
