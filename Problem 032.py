def isPandigital(i, j):
    numbers = list(range(1, 10))
    try:
        for letter in str(i) + str(j) + str(i * j):
            numbers.remove(int(letter))
    except:
        return False
    if numbers == []:
        return True


def main():
    ans = set()
    for i in range(10, 100):
        for j in range(100, 1000):
            if isPandigital(i, j):
                ans.add(i*j)

    for i in range(2, 10):
        for j in range(1000, 10000):
            if isPandigital(i,j):
                ans.add(i*j)

    print(sum(ans))


main()

# answer: 45228
# 31.03.2020