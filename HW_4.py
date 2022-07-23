# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from audioop import reverse


def conversion_to_binary_number(decimal_number):
    spisok = []
    while decimal_number > 0:
        if decimal_number % 2 == 0:
            spisok.append("0")
        elif decimal_number % 2 == 1 or decimal_number == 1:
            spisok.append("1")
        decimal_number//=2
    spisok.reverse()
    spisok = "".join(spisok)
    return spisok

print(conversion_to_binary_number(2))



