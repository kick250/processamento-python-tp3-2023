import spec
import exercise_11

def test_get_message_for_when_name_in_research():
  assert exercise_11.get_message_for("Ana") == "Participe da nossa pesquisa Ana!"

def test_get_message_for_when_name_not_in_research():
  assert exercise_11.get_message_for("Jen") == f"Obrigado por participar da pesquisa Jen!"

