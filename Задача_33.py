# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


# def change_rating(input_list): # (*args) - кортеж, ** - словарь
#     maxx = max(input_list)
#     minn = min(input_list)

#     for i in range(len(input_list)):
#         if input_list[i] == maxx:
#             input_list[i] = minn

#     return input_list

import functions

list_rating = [1, 3, 3, 3, 4]
list_1 = functions.change_rating(list_rating)
print(list_1)


# Более подробный способ
# def find_max(new_list):
#     max_num = new_list[0]
#     for i in new_list:
#         if i > max_num:
#             max_num = i
#     return max_num

# def find_min(new_list):
#     min_num = new_list[0]
#     for i in new_list:
#         if i < min_num:
#             min_num = i
#     return min_num

# def worst_list(new_list):
#     max = find_max(new_list)
#     min = find_min(new_list)
#     for i in range(len(new_list)):
#         if new_list[i] == max:
#             new_list[i] = min
#     return new_list

# list_rating = [1, 3, 3, 3, 4]
# print(worst_list(list_rating))

