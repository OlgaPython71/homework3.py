numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    divider = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divider += 1
    if divider == 2:
        primes.append(i)
    if divider > 2:
        not_primes.append(i)
print(primes)
print(not_primes)
