import spec
import exercise_15


def test_create_city():
  assert exercise_15.create_city('Brasil', 6747000, "Tem muitas Praias") == {
    'country': 'Brasil',
    'population': 6747000,
    'fact': "Tem muitas Praias"
  }