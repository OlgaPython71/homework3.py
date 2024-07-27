my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
value_list = 0
while value_list < len(my_list):
    if my_list[value_list] > 0:
        print(my_list[value_list])
    if my_list[value_list] < 0: break
    value_list += 1
