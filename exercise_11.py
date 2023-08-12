def get_research_result():
  return {
    'Jen': 'Python',
    'Sarah': 'C',
    'Edward': 'Ruby',
    'Phil': 'Python'
  }

def get_message_for(name):
  research = get_research_result()
  is_on_research = tuple(research.keys()).count(name) != 0
  if is_on_research:
    return f"Obrigado por participar da pesquisa {name}!"
  else:
    return f"Participe da nossa pesquisa {name}!"

def main():
  names = [ 'Jen', 'Ana', 'Sarah', 'Luciana', 'Paulo', 'Edward', 'Phil', 'Yuri' ]

  for name in names:
    print(get_message_for(name))


if __name__ == "__main__": main()