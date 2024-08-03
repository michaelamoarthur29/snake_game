from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.goto(0, 270)
        #self.write(f'Score ={self.score}', False, 'center', ("Times New Roman", 24, 'normal'))
        self.hideturtle()
        self.goto(0,270)

    def update_score(self):
        self.write(f'Score ={self.score}', False,'center', ("Times New Roman", 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write ("GAME OVER", align='center',font=8)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()