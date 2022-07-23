# <!-- 3 - Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564 -->

def min_max(spisok):
    max = spisok[0] - int(spisok[0])
    min = spisok[0] - int(spisok[0])
    
    for i in range (len(spisok)):
        num = spisok[i] - int(spisok[i])
        if num > max:
            max = num
        if num < min:
            min = num

    sum = max - min
    i = 0
    while sum != int(sum):
        sum*=10
        i+=1
    return(int(sum))

spisok = [1.1, 1.2, 3.1, 5.567, 10.003]

print(min_max(spisok))