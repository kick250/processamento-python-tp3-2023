import spec
import exercise_4


def test_print_all_not_pair_numbers_up_20():
  result = '\n'.join((str(i) for i in range(1, 21, 2))) + '\n'
  spec.expect_print(exercise_4.main, result)