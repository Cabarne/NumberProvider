from NumberProvider import NumberProvider


def positiveAction(number):
    print("Got an positive number >>>", number)
def negativeAction(number):
    print("Got an negative number >>>", number)

provider = NumberProvider()

provider.whenPositive(positiveAction)
provider.whenNegative(negativeAction)

provider.start()

########### Answers to Questions ##############

# Два раза повторяется "NumberProvider", потому что мы вызываем из модуля NumberProvider конкретно class NumberProvider, больше ничего. Одинаковое название файла с классом.

# Ошибка "AttributeError: 'NumberProvider' object has no attribute 'positiveCB'"? говорит что мы должны обратиться к атрибуту positiveCB через функцию whenPositive, чего сделано не было. Если я не ошибаюсь)  
