def get_numbers():
  return [i**3 for i in range(1, (10 + 1))]

def main():
  numbers = get_numbers()
  for number in numbers: print(number)


if __name__ == "__main__": main()