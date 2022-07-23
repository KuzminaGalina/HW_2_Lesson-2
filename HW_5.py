# 5 - Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/sH87m)

def fib(n:int):
    if n == 0:
        return 0
    elif n in [-1, 1, 2]:
        return 1
    elif n == -2:
        return (-1)
    elif n > 2:
        return fib(n-1) + fib(n-2)
    else:
        return fib(n+2) - fib(n+1)

n = int(8)
result_lst = []
for i in range(-abs(n),n+1):
    result_lst.append(fib(i))
print(result_lst)
        
    

