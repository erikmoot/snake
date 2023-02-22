'''Snake.py
Simple snake game in Python 3

Erik M.'''
import sys, random, time

import sys, random, time

class controller:
    'this is the controller class'
    def __init__(self, snake):
        self.snake = snake
        self.directions = ['w', 's', 'a', 'd']
        self.last_direction = 'w'
        self.current_direction = 'w'

    def get_direction(self):
        'get the direction from the user'
        self.last_direction = self.current_direction
        self.current_direction = input('Enter a direction: ')
        if self.current_direction not in self.directions:
            print('Invalid direction')
            self.current_direction = self.last_direction
        elif self.current_direction == 'w' and self.last_direction == 's':
            print('Invalid direction')
            self.current_direction = self.last_direction
        elif self.current_direction == 's' and self.last_direction == 'w':
            print('Invalid direction')
            self.current_direction = self.last_direction
        elif self.current_direction == 'a' and self.last_direction == 'd':
            print('Invalid direction')
            self.current_direction = self.last_direction
        elif self.current_direction == 'd' and self.last_direction == 'a':
            print('Invalid direction')
            self.current_direction = self.last_direction
        else:
            self.snake.direction = self.current_direction
class board:
    'this is the board class'
    def __init__(self):
        self.board = [['clear' for x in range(8)] for y in range(8)]

    def draw(self):
        'draw the board'
        for y in range(8):
            for x in range(8):
                if self.board[x][y] == 'clear':
                    sys.stdout.write('.')
                elif self.board[x][y] == 'snake':
                    sys.stdout.write('X')
                elif self.board[x][y] == 'food':
                    sys.stdout.write('O')
            sys.stdout.write('\n')

    def clear(self):
        'clear the board'
        self.board = [['clear' for x in range(8)] for y in range(8)]


class snake:
    'this is the snake class'
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.length = 1
        self.body = [[x,y]]
        self.alive = True
        self.score = 0

    def move(self):
        'move the snake'
        if self.direction == 'w':
            self.y -= 1
        elif self.direction == 's':
            self.y += 1
        elif self.direction == 'a':
            self.x -= 1
        elif self.direction == 'd':
            self.x += 1
        self.body.insert(0, [self.x, self.y])
        self.body.pop()
        self.check_collision()
    
    def check_collision(self):
        'check for collision with wall or self'
        if self.x < 0 or self.x >= 8 or self.y < 0 or self.y >= 8:  # Use '>=' instead of '>' for boundary checking.
            self.alive = False
        elif [self.x, self.y] in self.body[1:]:
            self.alive = False

    def grow(self):
        'grow the snake'
        self.length += 1
        self.score += 1
        self.body.append([self.x, self.y])

    def draw(self, board):
        'draw the snake'
        for i in range(self.length):
            board[self.body[i][0]][self.body[i][1]] = 'snake'  # Set the board to 'snake' instead of 1.


class food:
    'this is the food class'
    def __init__(self):
        self.x = random.randint(0, 7)
        self.y = random.randint(0, 7)
        self.eaten = False

    def draw(self, board):
        'draw the food'
        board[self.x][self.y] = 'food'

    def check_eaten(self, snake):
        'check if the food has been eaten'
        if snake.x == self.x and snake.y == self.y:
            self.eaten = True
            snake.grow()
            self.x, self.y = self.generate_position(snake)
    
    def generate_position(self, snake):
        'generate a new position for the food'
        while True:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if [x, y] not in snake.body:
                return x, y
def print_spiral(board, start_row, start_col):
    # Determine the starting point of the spiral


    # Define the initial direction of the spiral
    direction = "right"

    # Define the boundaries of the spiral
    min_row, max_row = start_row, start_row
    min_col, max_col = start_col, start_col

    # Print the elements in the spiral
    while min_row >= 0 and max_row < 8 and min_col >= 0 and max_col < 8:
        # Print the current element
        print(board[start_row][start_col])

        # Update the current position and the boundaries
        if direction == "right":
            start_col += 1
            if start_col > max_col:
                direction = "down"
                max_col = start_col
        elif direction == "down":
            start_row += 1
            if start_row > max_row:
                direction = "left"
                max_row = start_row
        elif direction == "left":
            start_col -= 1
            if start_col < min_col:
                direction = "up"
                min_col = start_col
        elif direction == "up":
            start_row -= 1
            if start_row < min_row:
                direction = "right"
                min_row = start_row

    
def main():
    'main function'
    #create the board
    game_board = board()
    #create the snake
    game_snake = snake(4,4,'w')

    game_controller = controller(game_snake)
    #create the food
    game_food = food()
    #main loop
    game_board.draw()
    game_snake.draw(game_board.board)
        #draw the food
    game_food.draw(game_board.board)
    while game_snake.alive:
        game_controller.get_direction()
        #move the snake
        game_snake.move()
       
        #check if food has been eaten
        game_food.check_eaten(game_snake)
        game_board.clear()
        #draw the snake
        game_snake.draw(game_board.board)
        #draw the food
        game_food.draw(game_board.board)
        #draw the board
        game_board.draw()


     
    #print score
    print_spiral(game_board, game_snake.x, game_snake.y)
    print('Game Over! Score: ' + str(game_snake.score))
    


main()