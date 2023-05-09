# Задача 32: Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint as R
lst = []
n = int(input('Введите длину массива: '))
for i in range (n):
    l = R(1,10)
    lst.append(l)
print(f'Мы получаем следующий массив из натуральных чисел: {lst}')
left=int(input('Введите левую границу интервала: '))
right=int(input('Введите правую границу интервала: '))
index=[]
for i in range(len(lst)):
    if lst[i] >= left and lst[i] <= right:
        index.append(i)
print(index)
