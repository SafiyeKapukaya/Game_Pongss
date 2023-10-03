from turtle import Turtle
paddles = []
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
    
        
    def create_paddle1(self):
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1,stretch_len=6)
        self.setheading(90)
        self.goto(-460,0)
        paddles.append(self)
    
    def create_paddle2(self):
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1,stretch_len=6)
        self.setheading(90)
        self.setposition(460,0)
        paddles.append(self)
    
    def moveup_paddle(self):
        self.forward(20)
    
    def movedown_paddle(self):
        self.backward(20)
    
            
            
        
        
        
       