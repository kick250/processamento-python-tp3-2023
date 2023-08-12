def create_people(first_name, last_name, age, city):
  return {
    "first_name": first_name,
    "last_name": last_name,
    "age": age,
    "city": city
  }

def main():
  people = create_people(
    "Ana",
    "Silva",
    32,
    "Rio de Janeiro"
  )
  print(people["first_name"])
  print(people["last_name"])
  print(people["age"])
  print(people["city"])


if __name__ == "__main__": main()