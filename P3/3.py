#3.2
s = "abcdefgabcd"
count = len(set(s))
print("Количество различных символов:", count)

#3.3
s = "hello world"
reversed_s = s[::-1]
print("Обращенная строка:", reversed_s)

#3.4
s = "hello world"
x = 'o'
indices = [i for i in range(len(s)) if s[i] == x]
print("Индексы элемента", x, ":", indices)

#3.5
s = [1, 2, 3, 4, 5, 6]
sum_even_indices = sum(s[i] for i in range(0, len(s), 2))
print("Сумма элементов с четными индексами:", sum_even_indices)


#3.6
s = ["apple", "banana", "cherry", "date"]
max_length_string = max(s, key=len)
print("Строка максимальной длины:", max_length_string)

#3.7
n = 18
is_harshad = n % sum(int(digit) for digit in str(n)) == 0
print("Число", n, "является числом Харшад:", is_harshad)

#3.8
from itertools import groupby

s = "aaaggcdddde"
compressed =  [(k, len(list(g))) for k, g in groupby(s)]
print("Сжатая строка:", compressed)

