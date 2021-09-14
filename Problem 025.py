def fibonacciGenerator():
    a, b = 1, 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b


def main():
    counter = 1
    for i in fibonacciGenerator():
        if len(str(i)) > 999:
            print(counter)
            break
        counter +=1

main()

# answer: 4782
# 31.03.2020