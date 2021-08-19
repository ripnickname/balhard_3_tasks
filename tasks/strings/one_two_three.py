"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дана строка.
    - цифры 1 заменить на uno
    - Цифры 2 заменить на two
    - Цифры 3 удалить

ПРИМЕРЫ
--------------------------------------------------------------------------------
'13512' -> 'uno5unotwo'
'35285' -> '5two85'
"""


def process_numbers(numbers: str) -> str:
    """Обрабатывает строку в зависимости от вхождения цифр 1, 2, 3.

    Если есть 1, то заменяет 1 на uno.
    Если есть 2, то заменяет 2 на two.
    Если есть 3, то их удаляет

    :param numbers: строка для обработки

    :return: обработанная строка
    """

    result = None

    result = numbers.replace('1', 'uno')
    result = result.replace('2', 'two')
    result = result.replace('3', '')

    return result


if __name__ == '__main__':
    string = input('Введите строку: ')
    print(f"Результат: {process_numbers(string)}")
