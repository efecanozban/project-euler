def divisorCounter(int):
    primes = {}
    iter = 2

    while True:
        if int != 1:
            if int % iter == 0:
                if iter in primes:
                    primes[iter] += 1
                else:
                    primes[iter] = 1

                int //= iter
            else:
                iter += 1
        else:
            iter += 1
            return primes


def triangularNumberGenerator():
    last_sum = 0
    iter = 1
    while True:
        yield last_sum + iter
        last_sum += iter
        iter += 1


def main():
    for i in triangularNumberGenerator():
        counter = 1
        for j in divisorCounter(i).values():
            counter *= j+1
        if counter > 500:
            print(i)
            break

main()

# answer: 76576500
# 30.03.2020