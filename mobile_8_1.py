def add_everything_up(a, b):
    # Проверяем типы аргументов
    if type(a) != type(b):
        return str(a) + str(b)

    # Если оба аргумента являются числами, выполняем сложение
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b

    # Если оба аргумента являются строками, выполняем конкатенацию
    else:
        return a + b
# Число и строка
print(add_everything_up(123.456, 'строка'))  # Вывод: '123.456строка'

# Строка и число
print(add_everything_up('яблоко', 4215))      # Вывод: 'яблоко4215'

# Два числа
print(add_everything_up(123.456, 7))          # Вывод: 130.456
