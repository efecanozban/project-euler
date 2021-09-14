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
    max_divider_count = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}

    for i in range(2, 21):
        divider_count = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0}
        for j in primeFactors(i):
            divider_count[j] += 1
        for k in divider_count.keys():
            if divider_count[k] > max_divider_count[k]:
                max_divider_count[k] = divider_count[k]

    ans = 1
    for i,j in max_divider_count.items():
        ans*=i**j

    print(ans)

main()

# answer: 232792560
# 30.03.2020