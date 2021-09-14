from math import sqrt, ceil


def primeGenerator():
    yield 2
    a = 3
    while True:
        i = 3
        while ceil(sqrt(a)) >= i:
            if a % i == 0:
                break
            else:
                i += 2
        else:
            yield a
        a += 2


total = 0

for i in primeGenerator():
    if i >= 2000000:
        break
    total += i

print(total)

# answer: 142913828922
# 30.03.2020
