class Results:
    def __init__(self, number):
        if number > 0:
            self.message = "УРА! Я здав екзамен."
        elif number < 0:
            self.message = "Я провалив екзамен."
        else:
            self.message = "Немає результатів для числа 0."

result_positive = Results(5)
print(result_positive.message)

result_negative = Results(-3)
print(result_negative.message)
