"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods = {}
item = input('Please enter an item : ')
goods['item'] = item
price = int(input('Please enter a price of the item : '))
goods['price'] = price
quantity = int(input('Please enter available quantity of items: '))
goods['pieces'] = quantity

tuple = (1,goods)

result = []
result.append(tuple)
print(result)


n = 1
while True:
    choice = input('If you would like to continue please type "yes" :')
    if choice == 'yes':
        item = input('Please enter an item : ')
        goods['item'] = item
        price = int(input('Please enter a price of the item : '))
        goods['price'] = price
        quantity= int(input('Please enter available quantity of items: '))
        goods['pieces'] = quantity
        n = n + 1
        tuple_n = (n,goods)
        result.append(tuple_n)
        continue
    else:
        break

print(f'Here are your items:\n {result}')

#print(result[0][1].get('price'))