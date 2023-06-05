def change_rating(input_list): # (*args) - кортеж, ** - словарь
    maxx = max(input_list)
    minn = min(input_list)

    for i in range(len(input_list)):
        if input_list[i] == maxx:
            input_list[i] = minn
            
    return input_list