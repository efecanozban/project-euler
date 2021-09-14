def isPalindrome(int):
    int = str(int)
    for i in range(len(int)//2):
        if int[i] != int[-i-1]:
            return False
    return True

def main():
    max = 0

    for i in range(900, 1000):
        for j in range(900, 1000):
            if isPalindrome(i*j) and i*j > max:
                max = i*j
    print(max)

main()

# answer: 906609
# 30.03.2020
