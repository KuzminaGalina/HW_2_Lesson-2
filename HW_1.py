# ; 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# ; стоящих на нечётной позиции.

# ; *Пример:*

# ; - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
random_spisok = [randint(1, 9) for _ in range (randint(3, 10))]
print(random_spisok)

def summ_spisok_nechet(spisok: list) -> int:
    summ_nechet = 0
    for i in range(1, len(spisok), 2):
        summ_nechet += spisok[i]
    return summ_nechet

print(summ_spisok_nechet(random_spisok))