"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
numbers = input("Please enter few numbers separated with space: ")
listing = list(numbers.split())
result = [int(i) for i in listing] # Turning strings into integers
print(f'The list of numbers you entered looks this way {result}. The sum of its numbers results is {sum(result)}.')

while True:
    result = result[:]
    extra_numbers = input("If you'd like to add some extra numbers please enter them separated with space. Otherwise type '%' to quit : ")
    if extra_numbers != '%':
        extra_listing = list(extra_numbers.split())
        extra_result = [int(i) for i in extra_listing] # Turning strings into integers
        result = result + extra_result # Concatenation of lists
        print(f'The total list of numbers you entered looks this way {result}. The sum of its numbers results is {sum(result)}.')
        continue
    else:
        break






