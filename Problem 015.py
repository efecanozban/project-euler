def main():
    grid = [[0] * 21 for i in range(21)]
    for i in range(21):
        grid[i][20] = 1
        grid[20][i] = 1

    for i in range(20):
        for j in range(20):
            grid[20-1-i][20-1-j] = grid[20-1-i][20-j] + grid[20-i][20-1-j]

    print(grid[0][0])
main()

# answer: 137846528820
# 17.04.2020