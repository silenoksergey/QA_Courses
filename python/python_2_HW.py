# Создать 2 переменных типа String с разными значениями
string_1 = 'Привет'
string_2 = 'Мир'
# Создать 4 переменных типа Integer с разными значениями
integer_1 = 5
integer_2 = 18
integer_3 = 8
integer_4 = 58
# Создать 3 переменных типа Float с разными значениями
float_1 = 8.2
float_2 = 9.3
float_3 = 95.8
# Реализовать 15 вариантов сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
int_1 = ((integer_2 > integer_1 < integer_4) != (integer_3 <= integer_4) >= (integer_2 < integer_1))
int_2 = integer_1 > integer_2
int_3 = integer_3 < integer_4
int_4 = integer_4 >= integer_1
int_5 = integer_2 <= integer_4
int_6 = integer_4 != integer_2
int_7 = integer_1 > (integer_2 + integer_4)
int_8 = integer_4 >= (integer_4 - integer_1)
int_9 = integer_3 < (integer_4 - integer_2)
int_10 = integer_1 + integer_2 != integer_4
int_print_str = int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9, int_10
print('15 вариантов сравнения int переменых >, <, >=, <=, !=.', int_print_str)
# Реализовать 9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
fl_1 = float_1 > float_2
fl_2 = float_1 < float_2
fl_3 = float_3 >= float_2
fl_4 = float_3 <= float_2
fl_5 = float_1 != float_3
fl_6 = float_1 > float_3 < float_2
fl_7 = float_1 > float_2 > float_3
fl_8 = (float_1 > float_2) < float_3
fl_9 = (float_1 > float_2) >= float_3
float_print_str = fl_1, fl_2, fl_3, fl_4, fl_5, fl_6, fl_7, fl_8, fl_9
print('9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=.', float_print_str)
# Реализовать 10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (and, or, not). Pезультаты весвести в консоль.
int_11 = not integer_1 > 2
int_12 = integer_2 > integer_1 and integer_4 < 2
int_13 = not 1028 > integer_3
int_14 = integer_4 > integer_3 or integer_4 < integer_1
int_15 = integer_1 > integer_2 and integer_4 != integer_2
int_16 = not (integer_1 > integer_2 and integer_4 != integer_2)
int_17 = integer_2 != integer_1 or integer_4 > integer_2
int_18 = integer_2 != integer_1 and integer_4 > integer_2
int_19 = not(integer_2 != integer_1) < integer_4 > integer_2
int_20 = (integer_4 < integer_2 and integer_3 > integer_1) or (integer_2 != integer_1 and integer_4 > integer_2)
int_print_str_2 = int_11, int_12, int_13, int_14, int_15, int_16, int_17, int_18, int_19, int_20
print('10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (and, or, not).', int_print_str_2)
# Сделать скрипт используя функцию input().
    # 1. Функция должна на вход принимать целое число.
    # 2. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно) 30"
# input_1 = int(input('Введите целое число:'))
# if input_1 < 30:
#     print('Вы ввели число = ' + str(input_1) + ' которое меньше 30')
# elif input_1 > 30:
#     print('Вы ввели число = ' + str(input_1) + ' которое больше 30')
# elif input_1 == 30:
#     print('Вы ввели число = ' + str(input_1) + ' которое равно 30')
# Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомных 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
from random import randint
input_2 = int(input('Введите целое число: '))
random_1 = randint(0, 100)
random_2 = randint(0, 100)
if input_2 < random_1 and input_2 < random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое меньше ' + str(random_1) + ' и меньше ' + str(random_2))
elif input_2 < random_1 and input_2 > random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое меньше ' + str(random_1) + ' и больше ' + str(random_2))
elif input_2 < random_1 and input_2 == random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое меньше ' + str(random_1) + ' и равно ' + str(random_2))
elif random_1 < input_2 < random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое больше ' + str(random_1) + ' и меньше ' + str(random_2))
elif input_2 > random_1 and input_2 > random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое больше ' + str(random_1) + ' и больше ' + str(random_2))
elif input_2 > random_1 and input_2 == random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое больше ' + str(random_1) + ' и равно ' + str(random_2))
elif input_2 == random_1 and input_2 < random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое равно ' + str(random_1) + ' и меньше ' + str(random_2))
elif input_2 == random_1 and input_2 > random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое равно ' + str(random_1) + ' и больше ' + str(random_2))
elif input_2 == random_1 and input_2 == random_2:
    print('Вы ввели число = ' + str(input_2) + ' которое равно ' + str(random_1) + ' и равно ' + str(random_2))


