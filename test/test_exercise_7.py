import spec
import exercise_7


def test_create_people():
  people = exercise_7.create_people(
    "Ana",
    "Silva",
    32,
    "Rio de Janeiro"
  )
  assert people["first_name"] == "Ana"
  assert people["last_name"] == "Silva"
  assert people["age"] == 32
  assert people["city"] == "Rio de Janeiro"