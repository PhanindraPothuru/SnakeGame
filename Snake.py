import turtle
class SnakeGame:
    def create_Snake(self):
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for start in starting_position:
            self.add_segment(start)
    def move_Snake(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def move_Snake_UP(self):
        if self.segments[0].heading()!="Down":
            self.segments[0].setheading(90)
    def move_Snake_Down(self):
        if self.segments[0].heading() != "Up":
            self.segments[0].setheading(270)
    def move_Snake_Right(self):
        if self.segments[0].heading() != "Left":
            self.segments[0].setheading(0)
    def move_Snake_Left(self):
        if self.segments[0].heading() != "Right":
            self.segments[0].setheading(180)

    def add_segment(self,start):
        new_tr = turtle.Turtle("square")
        new_tr.penup()
        new_tr.goto(start)
        new_tr.color("white")
        self.segments.append(new_tr)

    def extend(self):
        self.add_segment(self.segments[-1].position())