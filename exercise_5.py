def main():
  numbers = []
  number = 1
  while len(numbers) < 10:
    if number % 3 == 0:
      numbers.append(number)
    number += 1

  for index, number in enumerate(numbers):
    print(f"3 x {index + 1} = {number}")


if __name__ == "__main__": main()