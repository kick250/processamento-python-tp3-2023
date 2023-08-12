import spec
import exercise_14

def test_generate_dict():
  peoples_name_per_numbers = [
    ["Ana", [7, 1, 2]],
    ["Rodrigo", [32, 5, 22]],
    ["Pablo", [21, 24, 69]]
  ]

  peoples = exercise_14.create_dict(peoples_name_per_numbers)
  assert peoples == {
    "Ana": [7, 1, 2],
    "Rodrigo": [32, 5, 22],
    "Pablo": [21, 24, 69]
  }