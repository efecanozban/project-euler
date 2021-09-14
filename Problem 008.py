def fileReader(path):
    with open(path, "r") as raw_input:
        return raw_input.read()


def main():
    long_int = "".join(fileReader("Problem 008.txt").split("\n"))
    max = 1
    for i in range(988):
        candidate = 1
        for j in range(13):
            candidate *= int(long_int[i + j])

        if candidate > max:
            max = candidate

    print(max)


main()

# answer: 23514624000
# 30.03.2020

