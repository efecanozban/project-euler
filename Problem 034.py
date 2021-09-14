from math import factorial as fct


def main():
    print(sum([i for i in range(3, 999999) if sum(list(map(lambda i: fct(int(i)), str(i)))) == i]))


main()

# 40730
# 01.04.2020