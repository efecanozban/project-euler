def fileReader(path):
    with open(path, "r") as raw_input:
        return raw_input.read()


def main():
    grid = [list(map(int,i.split(" "))) for i in fileReader("Problem 018.txt").split("\n")]

    for i in range(14):
        for j in range(14-i):
            grid[14-1-i][j] += max(grid[14-i][j], grid[14-i][j+1])

    print(grid[0][0])

main()

# answer: 1074
# 17.04.2020