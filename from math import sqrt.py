from math import sqrt

message = """
Добро пожаловать в самую лучшую программу для вычисления
          квадратного корня из заданного числа
"""
print(message)


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверяем чсило."""
    if your_number <= 0:
        return
    i = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. Это будет: {i}')


calc(25.5)


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'