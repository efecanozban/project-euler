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


def main():
    counter = 1
    for i in primeGenerator():
        if counter == 10001:
            print(i)
            break
        counter += 1


main()

# answer 104743
# 30.03.2020

