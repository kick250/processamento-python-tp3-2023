def get_peoples():
  return {
    "Karen": ["Shopping", "Feira", "Praia"],
    "Luana": ["Praia", "Pão de açucar", "Praça"],
    "Joao": ["Pão de açucar", "Casa", "Shopping"]
  }


def main():
  peoples = get_peoples()
  for name, lugares in peoples.items():
    print(f"Os lugares favoritos de {name} são {lugares}")


if __name__ == "__main__": main()