import spec
import exercise_13


def test_create_peoples_dict():
  peoples = exercise_13.get_peoples()

  assert len(peoples.keys()) == 3
  assert str(type(peoples)) == "<class 'dict'>"



