def fileReader(path):
    with open(path, "r") as raw_input:
        return raw_input.read()


def main():
    grid = []
    for i in fileReader("Problem 011.txt").split("\n"):
        grid.append([i for i in map(int, i.split(" "))])

    max = 1

    for i in range(20):
        for j in range(20):
            if j < 17:
                candidate = 1
                for k in range(4):
                    candidate *= grid[i][j + k]
                if candidate > max:
                    max = candidate
            if j < 17:
                candidate = 1
                for l in range(4):
                    candidate *= grid[j+l][i]
                if candidate > max:
                    max = candidate
            if i < 17 and j < 17:
                candidate = 1
                for n in range(4):
                    candidate *= grid[i + n][j + n]
                if candidate > max:
                    max = candidate
            if i < 17 and j > 2:
                candidate = 1
                for m in range(4):
                    candidate *= grid[i + m][j - m]
                if candidate > max:
                    max = candidate

    print(max)


main()

# answer: 70600674
# 30.03.2021