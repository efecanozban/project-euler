def main():
    the_century = []
    for i in range(1901, 2001):
        for j in range(1, 13):
            if j in (1, 3, 5, 7, 8, 10, 12):
                the_century.extend([k for k in range(1, 32)])
            elif j in (4, 6, 9, 11):
                the_century.extend([k for k in range(1, 31)])
            else:
                if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                    the_century.extend([k for k in range(1, 30)])
                else:
                    the_century.extend([k for k in range(1, 29)])

    counter = 0

    for i in range(len(the_century)):
        if i % 7 == 5 and the_century[i] == 1:
            counter += 1

    print(counter)


main()

# answer: 171
# 31.03.2021
