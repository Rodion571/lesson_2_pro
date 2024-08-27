# Task 2
def geometric_progression_int(a: int, r: int):
    """
    Генератор геометрической прогрессии с целыми числами.

    :param a: Перший член прогресії (початковий член).
    :param r: Співвідношення прогресії (множник).
    :yield: Наступний член геометричної прогресії.
    """
    current = a
    while True:
        yield current
        current *= r

# Приклад використання генератора
# Перший член прогресії = 2, співвідношення = 3
gen_int = geometric_progression_int(2, 3)

for _ in range(10):
    print(next(gen_int))

# Task 3
def my_range(start: int, stop: int = None, step: int = 1):
    """
    Генератор, що реалізує функціональність функції range().

    :param start: Початкове значення (включено в послідовність).
    :param stop: Кінцеве значення (не включено в послідовність).
    :param step: Крок, з яким слід рухатися від start до stop.
    :yield: Числа від start до stop з кроком step.
    """
    if stop is None:
        # Якщо передано тільки одне значення, воно сприймається як stop, а start - 0.
        start, stop = 0, start

    if step == 0:
        raise ValueError("Step must be non-zero")

    # Генеруємо значення в заданому діапазоні
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

# Приклад використання генератора
for number in my_range(5):
    print(number)

print("---")

for number in my_range(1, 10, 2):
    print(number)

print("---")

for number in my_range(10, 0, -1):
    print(number)
# Task 4
def is_prime(num: int) -> bool:
    """
    Перевіряє, чи є число простим.

    :param num: Число для перевірки.
    :return: True, якщо число просте, інакше False.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(limit: int):
    """
    Генератор простих чисел до заданої верхньої межі.

    :param limit: Верхня межа діапазону (не включається в результат).
    :yield: Прості числа до limit.
    """
    for num in range(2, limit):
        if is_prime(num):
            yield num

# Приклад використання генератора
for prime in prime_generator(50):
    print(prime)
# Task 5
from datetime import datetime, timedelta


def date_range(start_date: str, end_date: str, date_format: str = "%Y-%m-%d"):
    """
    Генератор для послідовності дат між заданими початковою і кінцевою датами.

    :param start_date: Початкова дата у форматі date_format.
    :param end_date: Кінцева дата у форматі date_format.
    :param date_format: Формат дат, за замовчуванням "%Y-%m-%d".
    :yield: Дата у форматі date_format.
    """
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)

    current = start
    while current <= end:
        yield current.strftime(date_format)
        current += timedelta(days=1)


# Приклад використання генератора
for date in date_range("2024-08-01", "2024-08-07"):
    print(date)
