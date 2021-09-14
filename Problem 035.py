from math import ceil, sqrt


def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


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
        if a > 1000000:
            break


def main():
    rotateNumber = lambda number: [int((str(number) * 2)[i:len(str(number)) + i]) for i in range(len(str(number)))]
    print(sum([1 for i in primeGenerator() if all(list(map(isPrime, rotateNumber(i))))]))


main()

# answer : 55
# 01.04.2020
