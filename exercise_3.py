LIMITE = 1000000


def get_numbers():
  return tuple(range(1, (LIMITE + 1)))

def main():
  numbers = get_numbers()

  for number in numbers: print(number)

  print(sum(numbers))


if __name__ == "__main__": main()