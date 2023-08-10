def i_like_message(flavor):
  return f"Eu gosto de pizza de {flavor}"

def main():
  flavors = ["calabresa", "4 queijos", "banana"]
  for flavor in flavors:
    print(i_like_message(flavor))
  print("Eu amo pizza!")


if __name__ == "__main__": main()