# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
print("\ntask 1: ")

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print("\ntask 2: ")
n = int(input("Введите N: "))
rez = 1
myList = []
for i in range(1, n  + 1):
    rez *= i
    myList.append(rez)
print(myList)



# 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
print("\ntask 3: ")
n = int(input("Введите N: "))
myDict = dict()
sum = 0
for i in range (1, n + 1):
    sum += (1 + (1/n))**n
    myDict[i] = round(sum, 2)
print(myDict) 
    


# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random
print("\ntask 4: ")
n = int(input("Введите количество элементов: "))
a = []
for i in range(n):
    a.append(random.randint(-n, n))
print(a)
mult = 1
with open('file.txt', 'r') as f:
    for pos in f.read():
        if pos != '\n':
            mult *= a[int(pos)]
print(f"Произведение выбранных элементов: {mult}")


# 5 Реализуйте алгоритм перемешивания списка
print("\ntask 5: ")
myList = [5, 9, 6, 33, -9]
print(f"Исходный массив: {myList}")
random.shuffle(myList)
print(f"Перемешанный массив: {myList}")
