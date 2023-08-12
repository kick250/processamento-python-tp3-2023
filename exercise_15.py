def create_city(country, population, fact):
  return {
    'country': country,
    'population': population,
    'fact': fact
  }

def get_cities():
  return {
    "Rio de Janeiro": create_city('Brasil', 6747000, "Tem muitas Praias"),
    "Salvador": create_city('Brasil', 2886698, "Fica na Bahia"),
    "Niteroi": create_city('Brasil', 511786, "Tem muitas Praias"),
  }

def main():
  cities = get_cities()
  for city_name, data in cities.items():
    print(city_name)
    print(data['country'])
    print(data['population'])
    print(data['fact'])


if __name__ == "__main__": main()