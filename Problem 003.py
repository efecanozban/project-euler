def primeFactors(int):
    primes = []
    iter = 2

    while True:
        if int != 1:
            if int % iter == 0:
                primes.append(iter)
                int //= iter
            else:
                iter += 1
        else:
            return primes


def main():
    print(max(primeFactors(600851475143)))

main()

# answer: 6857
# 30.03.2020
