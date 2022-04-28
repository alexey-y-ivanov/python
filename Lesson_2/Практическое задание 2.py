"""
2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""
a = []
c = []

while True:
    b = input('Please input an entry one after another. Please type "end" to quit the input :')
    if b != 'end':
        a.append(b)
        continue
    else:
        break
print(a)
print(a[0])
print(a[1])

for i in range(len(a), 2):
    a[i], a[i+1] = a[i+1], a[i]
    c.append(a[i])

print(c)






