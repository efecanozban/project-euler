def main():
    print(sum([i for i in range(9**5 *5) if sum([int(i)**5 for i in str(i)]) == i]))

main()

# answer: 443840
# 17.04.2020