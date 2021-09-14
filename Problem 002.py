def main():
    fibonacci_sqpuence = [1, 2]

    while True:
        fibonacci_sqpuence.append(fibonacci_sqpuence[-1] + fibonacci_sqpuence[-2])
        if fibonacci_sqpuence[-1] >= 4000000:
            fibonacci_sqpuence.pop()
            break

    print(sum([i for i in fibonacci_sqpuence if i % 2 == 0]))

main()

# answer: 233168
# 30.03.2020
