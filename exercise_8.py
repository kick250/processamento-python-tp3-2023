NAME_INDEX = 0
NUMBER_INDEX = 1

def create_dict(peoples_name_per_number):
  peoples = {}

  for people in peoples_name_per_number:
    peoples[people[NAME_INDEX]] = people[NUMBER_INDEX]

  return peoples

def main():
  peoples_name_per_number = [
    ["Ana", 7],
    ["Rodrigo", 32],
    ["Pablo", 21]
  ]

  peoples = create_dict(peoples_name_per_number)
  for key in peoples.keys():
    print(f"nome: {key}, numero favorito: {peoples[key]};")



if __name__ == "__main__": main()