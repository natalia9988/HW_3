# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Введите количество элементов в массиве: ")) 
print("Элементы массива:")
A = [int(input()) for i in range(N)]
X = int(input("Число x: "))
number=0
for i in range(len(A)):
    if (X-A[i])<X-number and X-A[i]>0:
        number=i
print(f'Число {A[number]} в списке A наиболее близко по величине к числу {X}')