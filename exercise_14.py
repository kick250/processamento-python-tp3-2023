NAME_INDEX = 0
NUMBERS_INDEX = 1

def create_dict(peoples_name_per_numbers):
  peoples = {}

  for people in peoples_name_per_numbers:
    peoples[people[NAME_INDEX]] = people[NUMBERS_INDEX]

  return peoples

def main():
  peoples_name_per_numbers = [
    ["Ana", [7, 1, 2]],
    ["Rodrigo", [32, 5, 22]],
    ["Pablo", [21, 24, 69]]
  ]

  peoples = create_dict(peoples_name_per_numbers)
  for key in peoples.keys():
    print(f"nome: {key}, numero favorito: {peoples[key]};")



if __name__ == "__main__": main()