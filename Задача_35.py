# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def prostoe_proverka(num):
    if num in (0, 1): 
        return False

    for i in range(2, (num//2)+1): # // - целочисленное деление, плюс единица - чтобы подвинуть границу ренджа (в качестве примера 4, 4 / 2 = 2, 2 - граница, которая не попадает, поэтому добавляем 1)
        if(num%i == 0):
            return False
    return True

N = int(input("Введите число: "))
print(prostoe_proverka(N))

# Другой способ

# def is_it_simple_or_not(number):
#     flag = 0
#     for i in range(2, number):
#         if  number % i == 0:
#             flag = 1
#     return "No" if flag else "Yes"
# print(is_it_simple_or_not(13))

# Более оптимальная запись предыдущего решения
# def is_it_simple_or_not(number):
#     for i in range(2, number):
#         if  number % i == 0:
#             return "No"
#     return "Yes"
# print(is_it_simple_or_not(13))