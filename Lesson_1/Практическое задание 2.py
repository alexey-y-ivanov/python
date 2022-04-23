"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
s = int(input('Please input a number of seconds :'))

h = s//3600 # integer devision to extract hours
m = (s - h*3600)//60 # the rest of seconds integerly devided by 60 stands for minutes
rest_of_seconds = s - h*3600 - m*60

print(f'The inserted number of seconds is the equivalent of {h}h:{m}m:{rest_of_seconds}s')
# print('The inserted number of seconds is the equivalent of {}h:{}m:{}s'.format(h,m,rest_of_seconds))
