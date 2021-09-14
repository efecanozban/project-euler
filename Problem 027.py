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


def main():
    longest_chain = 0
    ans = 0
    for a in range(-999, 1000):
        for b in range(1, 1000, 2):
            i = 0
            while True:
                if isPrime(i ** 2 + i * a + b):
                    i += 1
                    continue
                else:
                    if i > longest_chain:
                        longest_chain = i
                        ans = a * b
                    break

    print(ans)


main()

# answer: -59231
# 31.03.2020