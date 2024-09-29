# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (1, 3, 5, 7, 9, 11)
my_tuple3 = (-2, -1, 0, 1, 2, 3)

result = tuple(x for x in my_tuple1 if x in my_tuple2 and x in my_tuple3)
print(result)



# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.
my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (3, 4, 5, 6, 7)
my_tuple3 = (5, 6, 7, 8, 9)

unique_in_tuple1 = tuple(x for x in my_tuple1 if x not in my_tuple2 and x not in my_tuple3)
unique_in_tuple2 = tuple(x for x in my_tuple2 if x not in my_tuple1 and x not in my_tuple3)
unique_in_tuple3 = tuple(x for x in my_tuple3 if x not in my_tuple1 and x not in my_tuple2)

print("tuple1:", unique_in_tuple1)
print("tuple2:", unique_in_tuple2)
print("tuple3:", unique_in_tuple3)



# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.
my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (1, 4, 3, 8, 5)
my_tuple3 = (1, 6, 3, 10, 5)

result = []

for i in range(min(len(my_tuple1), len(my_tuple2), len(my_tuple3))):
    if my_tuple1[i] == my_tuple2[i] == my_tuple3[i]:
        result.append(my_tuple1[i])

result = tuple(result)

print("Элементы, общие для всех кортежей и на одинаковых позициях:", result)