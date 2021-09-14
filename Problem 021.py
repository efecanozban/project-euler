def sumOfDividors(int):
    sum = 0
    for i in range(1, int // 2 + 1):
        if int % i == 0:
            sum += i

    return sum


def main():
    sum = 0
    sums_of_dividors = {}
    for i in range(1,10000):
        sums_of_dividors[i] = sumOfDividors(i)
        if sumOfDividors(sums_of_dividors[i]) == i and i != sumOfDividors(i):
            sum += i

    print(sum)

main()

# answer: 31626
# 31.03.2020