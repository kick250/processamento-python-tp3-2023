def get_biggest_rivers():
  return {
    'Rio Nilo': 'Egito',
    'Rio Amazonas': 'Brasil',
    'Rio Yangtzé': 'China',
  }
def main():
  for river, country in get_biggest_rivers().items():
    print(f"O {river} atravessa o {country}")


if __name__ == "__main__": main()