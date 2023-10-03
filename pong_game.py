from turtle import Turtle,Screen
from pong_game_paddle import Paddle
from pong_game_ball import Bouncing_ball
from pong_game_scorboard import Scorboard
import time
screen = Screen()
#screen.tracer(0)
continue_game = True
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width= 1200,height=600)
lines = Turtle()
lines.hideturtle()
lines.speed(0)
lines.color("white")
lines.pensize(15)
lines.penup()
lines.goto(-495,245)
lines.pendown()
lines.forward(990)
lines.right(90)
lines.forward(490)
lines.right(90)
lines.forward(990)
lines.right(90)
lines.forward(490)
lines.penup()
lines.goto(0,250)
lines.setheading(0)
lines.right(90)
lines.pendown()
for _ in range(16):
    lines.pensize(5)
    lines.color("white")
    lines.forward(15)
    lines.color("black")
    lines.forward(15)
    
paddle1 = Paddle()   
paddle2 = Paddle()
ball = Bouncing_ball()
scor = Scorboard()
paddle1.create_paddle1()
paddle2.create_paddle2()

screen.listen()
screen.onkey(key="Up",fun=paddle2.moveup_paddle)
screen.onkey(key="Down",fun=paddle2.movedown_paddle)
screen.onkey(key="w",fun=paddle1.moveup_paddle)
screen.onkey(key="s",fun=paddle1.movedown_paddle)
while True:
    #screen.update()
    #ball.move_ball()
    print("c")
    ball.bouncing()
    print("d")
    if ball.xcor() > 495.0 or ball.xcor() < -495.0 :
        scor.clear()
        scor.print_score()
        scor.game_over()
        break
    if (ball.distance(paddle1) < 50 and ball.xcor() < -440) or (ball.distance(paddle2) < 50 and ball.xcor() > 440):
        scor.clear()
        print("a")
        scor.increase_score()
        

screen.exitonclick()

