class grid:
    def __init__(self, size):
        self.nodes = [None] * size ** 2
        self.current_dir = "west"
        self.current_pos = size - 1
        self.current_number = size ** 2
        self.size = size
        while self.current_number > 1:
            self.appendNode()
        self.nodes[size ** 2 // 2] = 1

    def appendNode(self):
        if self.current_dir == "west":
            self.nodes[self.current_pos] = self.current_number
            if self.current_pos - 1 >= 0 and self.nodes[self.current_pos - 1] == None:
                self.current_number -= 1
                self.current_pos -= 1
            else:
                self.current_dir = "south"
        elif self.current_dir == "south":
            self.nodes[self.current_pos] = self.current_number
            if self.current_pos + self.size < self.size ** 2 and self.nodes[self.current_pos + self.size] == None:
                self.current_number -= 1
                self.current_pos += self.size
            else:
                self.current_dir = "east"
        elif self.current_dir == "east":
            self.nodes[self.current_pos] = self.current_number
            if self.current_pos + 1 < self.size ** 2 and self.nodes[self.current_pos + 1] == None:
                self.current_number -= 1
                self.current_pos += 1
            else:
                self.current_dir = "north"
        elif self.current_dir == "north":
            self.nodes[self.current_pos] = self.current_number
            if self.current_pos - self.size > 0 and self.nodes[self.current_pos - self.size] == None:
                self.current_number -= 1
                self.current_pos -= self.size
            else:
                self.current_dir = "west"


def main():
    new_grid = grid(1001)
    total = 0
    for i in range(1001):
        total += new_grid.nodes[i * 1001 + i]
        total += new_grid.nodes[i * 1001 + 1001 - 1 - i]

    print(total - 1)


main()

# answer: 669171001
# 31.03.2020
