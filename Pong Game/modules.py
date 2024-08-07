from turtle import Turtle
import random


class Racket(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(1, 5, 0)
        self.setheading(90)
        self.setposition(coordinates)
        self.score = 0

    def move_up(self):
        self.setheading(90)
        self.forward(20) if self.ycor() < 300 else False

    def move_down(self):
        self.setheading(270)
        self.forward(20) if self.ycor() > -300 else False


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1, 0)
        self.color("white")
        self.penup()
        self.x_increase = random.choice([10, -10])
        self.y_increase = random.choice([10, -10])

    def start(self):
        self.setposition(0, 0)
        random_starting_direction = random.choice([random.randint(110, 250), random.randint(290, 430)])
        self.setheading(random_starting_direction)

    def move(self, x_increase, y_increase):
        self.setposition(self.xcor() + self.x_increase, self.ycor() + self.y_increase)

    def bounce(self, bouncing_from):
        if bouncing_from == "wall":
            self.y_increase *= -1
        elif bouncing_from == "racket":
            self.x_increase *= -1


class Scoreboard(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(coordinates)
        self.pendown()

    def update_score(self, player_score):
        self.clear()
        self.write(arg=player_score, align="center", font=("retro", 30, "bold"))

