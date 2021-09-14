def isAbundant(int):
    sum = 0
    for i in range(1, int // 2 + 1):
        if int % i == 0:
            sum += i

    return sum > int


def main():
    ans = 0
    sums = set()
    abundants = []
    for i in range(1,28123):
        if isAbundant(i):
            abundants.append(i)

    for i in range(len(abundants)):
        for j in range(i,len(abundants)):
            sums.add(abundants[i]+abundants[j])

    for i in range(1,28124):
        if i not in sums:
            ans += i

    print(ans)

main()

# answer: 4179871
# 31.03.2020
