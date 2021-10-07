from turtle import Turtle,Screen
from p import Paddle
s=Screen()
s.bgcolor("black")
s.setup(width=800,height=600)
s.title("Ping Pong")
s.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down") 
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s") 

game_on=True

while(game_on):
  s.update()
s.exitonclick()