import spec
import exercise_12

def test_message():
  people = exercise_12.create_people("Ana", "Silva", 32, "Rio de Janeiro")
  assert exercise_12.get_people_message(people) == "name: Ana, sobrenome: Silva, idade: 32, cidade: Rio de Janeiro"