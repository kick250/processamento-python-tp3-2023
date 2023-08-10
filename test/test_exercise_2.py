import spec
import exercise_2

def test_print_all_numbers_positive_before_21():
  numbers = '\n'.join([str(i) for i in range(1, 21)]) + '\n'
  spec.expect_print(exercise_2.main, numbers)