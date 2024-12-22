import random

class SnakeGame:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = [[height//2, width//2], [height//2, width//2-1], [height//2, width//2-2]]
        self.food = [height//2, width//2]
        self.key = 'r'

    def print_board(self):
        for y in range(self.height):
            for x in range(self.width):
                if [y, x] in self.snake:
                    print('O', end='')
                elif [y, x] == self.food:
                    print('F', end='')
                else:
                    print(' ', end='')
            print()

    def move_snake(self):
        new_head = self.snake[0].copy()
        if self.key == 'u':
            new_head[0] -= 1
        elif self.key == 'd':
            new_head[0] += 1
        elif self.key == 'l':
            new_head[1] -= 1
        elif self.key == 'r':
            new_head[1] += 1
        self.snake.insert(0, new_head)
        if self.snake[0] == self.food:
            self.food = None
            while self.food is None:
                nf = [random.randint(0, self.height-1), random.randint(0, self.width-1)]
                self.food = nf if nf not in self.snake else None
        else:
            self.snake.pop()

    def game_over(self):
        if (self.snake[0][0] < 0 or self.snake[0][0] >= self.height or
            self.snake[0][1] < 0 or self.snake[0][1] >= self.width or
            self.snake[0] in self.snake[1:]):
            return True
        return False

    def play(self):
        while True:
            self.print_board()
            command = input("Enter direction (u/d/l/r): ")
            if command == 'u' or command == 'd' or command == 'l' or command == 'r':
                self.key = command
            self.move_snake()
            if self.game_over():
                print("Game Over!")
                break

game = SnakeGame(20, 20)
game.play()