def fileReader(path):
    with open(path, "r") as raw_input:
        return raw_input.read()


def main():
    names = sorted(fileReader("Problem 022.txt").split(","))
    letters = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
               'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22,
               'y': 25, 'x': 24, 'z': 26, 'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8,
               'K': 11, 'J': 10, 'M': 13,
               'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22,
               'Y': 25, 'X': 24, 'Z': 26}
    sum = 0
    for i in range(1, len(names) + 1):
        score = 0
        for letter in names[i - 1]:
            if letter != "\"":
                score += letters[letter]
        sum += score * i

    print(sum)


main()

# answer: 871198282
# 31.03.2020
