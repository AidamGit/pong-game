from modules import *
import turtle as t
import time

# display
display = t.Screen()
display.bgcolor("black")
display.title("Aidam's Python Pong")
display.setup(height=600, width=1000)
display.tracer(False)
display.listen()

# net
net = Turtle()
net.hideturtle()
net.pencolor("white")
net.penup()
net.setposition(0, -310)
net.setheading(90)
net.pensize(5)
for i in range(25):
    net.pendown()
    net.forward(20)
    net.penup()
    net.forward(20)

# rackets / paddles
player1 = Racket((-450, 0))
player2 = Racket((450, 0))

# ball
ball = Ball()
ball.x_increase = random.choice([12, -12])
ball.y_increase = random.choice([12, -12])
ball.start()

# controls
display.onkeypress(key="w", fun=player1.move_up)
display.onkeypress(key="s", fun=player1.move_down)
display.onkeypress(key="i", fun=player2.move_up)
display.onkeypress(key="k", fun=player2.move_down)
display.update()

# scoreboard
scoreboard_player1 = Scoreboard((200, 250))
scoreboard_player1.update_score(player1.score)
scoreboard_player2 = Scoreboard((-200, 250))
scoreboard_player2.update_score(player2.score)

time.sleep(2)

playing = True
while playing:

    time.sleep(0.05)
    ball.move(ball.x_increase, ball.y_increase)

    # check if ball collided with wall
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce("wall")

    # check if ball collided with racket
    if ball.distance(player1) <= 50 or ball.distance(player2) <= 40:
        ball.bounce("racket")

    # check if ball scored
    if ball.xcor() <= -700 or ball.xcor() >= 700:

        if ball.xcor() < 0:
            player1.score += 1
            scoreboard_player1.update_score(player1.score)

        elif ball.xcor() > 0:
            player2.score += 1
            scoreboard_player2.update_score(player2.score)

        ball.start()
        display.update()
        time.sleep(1)

    display.update()

t.done()
