"""class Bouncing_self(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
     
    def move_self(self):
       
        while True:
            new_x = random.randint(-980,980)
            new_y = random.randint(-600,600)
            if (new_x <= -495 or new_x >=495):
                new_x = new_x
                break
            else:
                pass
        self.speed(1)
        self.goto(new_x,new_y)


"""
import pong_game_paddle
from turtle import Turtle,Screen
screen = Screen()

class Bouncing_ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        
        self.color("white")
        self.dx = 2  # Topun x ekseni üzerindeki hızı
        self.dy = 2  # Topun y ekseni üzerindeki hızı
    
    def move_ball(self):
        
        self.goto(0, 0)

    def bouncing(self):
        while True:
            
            self.update_position()

            if self.xcor() > 495.0 or self.xcor() < -495.0 :
                break

            # Duvarlara çarpma kontrolü
            if self.ycor() > 245 or self.ycor() < -245:
                self.dy *= -1  # Y hızını tersine çevirerek yönü değiştirir
                
           
            # Paddle'lara çarpma kontrolü
            if (self.distance(pong_game_paddle.paddles[0]) < 50 and self.xcor() < -440) or (self.distance(pong_game_paddle.paddles[1]) < 50 and self.xcor() > 440):
                self.dx *= -1  # X hızını tersine çevirerek yönü değiştirir
                print("b")
                
    def update_position(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)