def main():
    coins = [0] * 201
    coins[0] = 1
    for i in range(1, len(coins)):
        if i < 2:
            coins[i] = max(coins[i - 1])
        elif i < 5:
            coins[i] = max(coins[i - 1], coins[i - 2])
        elif i < 10:
            coins[i] = max(coins[i - 1], coins[i - 2], coins[i - 5])
        elif i < 20:
            coins[i] = max(coins[i - 1], coins[i - 2], coins[i - 5], coins[i - 10])
        elif i < 50:
            coins[i] = max(coins[i - 1], coins[i - 2], coins[i - 5], coins[i - 10], coins[i - 20])
        elif i < 100:
            coins[i] = max(coins[i - 1], coins[i - 2], coins[i - 5], coins[i - 10], coins[i - 20], coins[i - 50])
        elif i < 200:
            coins[i] = max(coins[i - 1], coins[i - 2], coins[i - 5], coins[i - 10], coins[i - 20], coins[i - 50],
                           coins[i - 100])
        else:
            coins[i] = max(coins[i - 1], coins[i - 2], coins[i - 5], coins[i - 10], coins[i - 20], coins[i - 50],
                           coins[i - 100],coins[i-200])

    print(coins[201])