def calculate_structure_sum(*data_structure):
    itog = 0
    for i in data_structure:
        if isinstance(i, (list, tuple, set)):
            itog += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            itog += calculate_structure_sum(*i.items())
        elif isinstance(i, int):
            itog += i
        elif isinstance(i, str):
            itog += len(i)
    return itog

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
