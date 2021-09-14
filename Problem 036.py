def isPalindrome(number):
    if type(number) == int:
        number = str(number)
    else:
        number = "".join(number[2:])
    return all([True if number[i] == number[-1 - i] else False for i in range(len(number) // 2)])


def main():
    print(sum(i for i in range(1, 1000001) if isPalindrome(i) and isPalindrome(bin(i))))


main()

# answer: 872187
# 01.04.2020
