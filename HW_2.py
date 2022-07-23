# # ; 2 - Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # ; *Пример:*

# # ; - [2, 3, 4, 5, 6] => [12, 15, 16];
# # ; - [2, 3, 5, 6] => [12, 15]



from random import randint
random_spisok = [randint(1, 9) for _ in range (randint(3, 10))]
print(random_spisok)

def product_of_two_numbers(spisok: list) -> int:
    result_spisok = []
    f_index = 0
    l_index = len(spisok) - 1
    while l_index - f_index >= 0:
        result_spisok.append(spisok[f_index] * spisok [l_index])
        f_index += 1
        l_index -= 1
    return result_spisok

print(product_of_two_numbers(random_spisok))