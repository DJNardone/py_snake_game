from turtle import Turtle

# CONSTANTS
SNAKE_START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.snake_head = self.snake_parts[0]

    # create the parts of the snake.
    def create_snake(self):
        for s in SNAKE_START:
            self.add_segment(s)

    def add_segment(self, s):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(s)
        self.snake_parts.append(new_square)

    def extend_snake(self):
        self.add_segment(self.snake_parts[-1].position())

    # get the snake parts to move smoothly together.
    def move(self):
        for s in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[s - 1].xcor()
            new_y = self.snake_parts[s - 1].ycor()
            self.snake_parts[s].goto(new_x, new_y)
        self.snake_head.forward(MOVE_FORWARD)

    # directional keys so snake can change directions
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

