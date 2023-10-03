from turtle import Turtle,Screen
listee = []
class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        listee.append(self)
        
    def increase_score(self):
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(0,270)
        self.score += 1
        self.print_score()
    def print_score(self):
        self.color("white")
        self.write(f"Score : {self.score}",font = ('Arial',40,'normal'),align ='center',move=True)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=('Arial', 40, 'normal'), align='center')
        

        
