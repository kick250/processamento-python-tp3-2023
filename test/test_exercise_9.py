import spec
import exercise_9


def test_main():
  expected_print = '\n'.join([
    "Variavel",
    "Nomes que apontam para um local da memória que guarda um valor que definimos.\n",
    "Array",
    "Conjunto de elementos.\n",
    "Dicionario",
    "Conjunto de elementos organizados por chave valor.\n",
    "função",
    "Termo que guarda um conjunto de instruções de código.\n",
    "Linguagem de programação",
    "Metodo padronizado usado para passar instruções para o computador\n\n",
  ])

  spec.expect_print(exercise_9.main, expected_print)
