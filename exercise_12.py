from exercise_7 import create_people


def get_peoples():
  return [
    create_people("Ana", "Silva", 32, "Rio de Janeiro"),
    create_people("Breno", "Lobato", 23, "São Paulo"),
    create_people("Yuri", "Silveira", 12, "Niteroi")
  ]

def get_people_message(people):
  message = ""
  message += f"name: {people['first_name']}, "
  message += f"sobrenome: {people['last_name']}, "
  message += f"idade: {people['age']}, "
  message += f"cidade: {people['city']}"

  return message

def main():
  peoples = get_peoples()
  for people in peoples:
    print(get_people_message(people))



if __name__ == "__main__": main()