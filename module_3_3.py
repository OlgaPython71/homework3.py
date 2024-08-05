def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [1, 2, 'Day']
values_dict = {'a':3, 'b':3.14, 'c':'Pi'}
values_list_2 = [54.32, 'Строка' ]

print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
