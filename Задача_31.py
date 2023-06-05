# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где 
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n <= 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# number = int(input("Введите число n: "))
# print(fib(number))

def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n-1) + fib(n-2)
number = int(input("Введите число n: "))
print(fib(number))


# def fibonacci(n):
#     # Если n равно 0 или 1, то возвращаем n
#     if n < 2:
#         return n
#     # Если n больше или равно 2, то вычисляем n-е число Фибоначчи
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Введите номер числа Фибоначчи: "))

# print("Число Фибоначчи под номером", n, "равно", fibonacci(n))