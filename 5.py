"""
Функция расчитывает среднюю температуру
Находит среднее арифметическое значений списка температур, исключая 'None'
"""
def avarage(t):
    sum = 0
    num = 0

    for value in t:
        if (value != None):
            num += 1
            sum += value

    return sum / num

t = [10, None, 20, 18, 12, None, 15]

print('Средняя температура: ', round(avarage(t), 2) )

"""
Функция разделяет положительные и отрицательные значения в 2 разных списка,
сортирует списки и возвращает кортеж из полученых списков
"""
def numbers(*nums):
    positive = []
    negative = []

    for n in nums:
        if n >= 0:
            positive.append(n)
        else:
            negative.append(n)

    positive.sort()
    negative.sort(reverse=True)

    return (positive, negative)

print(numbers(-4, 7, 49, 5.5, -200, -7))

"""
Функция возводит число в степень (итерационно)
"""
def stp1(x, n):
    y = 1

    for i in range(n):
        y *= x

    return y

"""
Функция возводит число в степень (рекурскивно)
"""
def stp2(x, n):
    if n == 0:
        return 1
    else:
        return x * stp2(x, n-1)

x = 4
n = 5
print(x, '**', n, '=', stp1(x, n))
print(x, '**', n, '=', stp2(x, n))