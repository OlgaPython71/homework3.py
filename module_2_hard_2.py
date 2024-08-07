import random

n = random.randint(3, 20)
print(n)
result = []
for k in range(1, n):
    if n % k == 0:
        for r in range(1, k // 2 + 1):
            for v in range(1, k):
                if k == r + v and r != v:
                    result.append(r)
                    result.append(v)
for i in range(1, n // 2 + 1):
    for j in range(1, n):
        if n == i + j and i != j:
            result.append(i)
            result.append(j)
print(result)
