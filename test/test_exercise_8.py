import spec
import exercise_8


def test_generate_dict():
  peoples_name_per_number = [
    ["Julio", 7],
    ["Yuri", 12],
    ["Pablo", 65]
  ]

  peoples = exercise_8.create_dict(peoples_name_per_number)
  assert peoples == {
    "Julio": 7,
    "Yuri": 12,
    "Pablo": 65
  }