def fileReader(path):
    with open(path, "r") as raw_input:
        return raw_input.read()

def main():
    print(sum([i for i in map(int,fileReader("Problem 013.txt").split("\n"))]))

main()

# answer: 5537376230
# 30.03.2020