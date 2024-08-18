import random
import turtle
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.score=0
        self.goto(0,280)
        self.penup()
        self.color("white")
        self.write(arg=f"score: {self.score}",align="center",font=("calibri",14,"normal"))
        self.refresh()

    def refresh(self):
        new_x=random.randint(-280,280)
        new_y=random.randint(-280,280)
        print(f"x:{new_x} and y:{new_y}")
        self.goto(new_x,new_y)

    def scoreBoard(self):
        self.score+=1
        self.goto(0,280)
        self.penup()
        self.clear()
        self.color("white")
        self.write(arg=f"score: {self.score}",align="center",font=("calibri",14,"normal"))

    def end_ScoreBoard(self):
        self.clear()
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.write(arg=f"Game Over !!! Final score: {self.score}",align="center",font=("calibri",14,"normal"))