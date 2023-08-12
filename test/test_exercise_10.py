import spec
import exercise_10

def test_get_biggest_rivers():
  assert exercise_10.get_biggest_rivers() == {
    'Rio Nilo': 'Egito',
    'Rio Amazonas': 'Brasil',
    'Rio Yangtzé': 'China',
  }

def test_main():
  expected_result = '\n'.join([
    "O Rio Nilo atravessa o Egito",
    "O Rio Amazonas atravessa o Brasil",
    "O Rio Yangtzé atravessa o China\n"
  ])

  spec.expect_print(exercise_10.main, expected_result)
