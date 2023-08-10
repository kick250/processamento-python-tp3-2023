import spec
import exercise_1


def test_show_messages():
  messages = [
    "Eu gosto de pizza de calabresa",
    "Eu gosto de pizza de 4 queijos",
    "Eu gosto de pizza de banana",
    "Eu amo pizza!"
  ]

  spec.expect_print(exercise_1.main, "\n".join(messages) + "\n")