import turtle,Snake
import time
import SnakeFood
scr=turtle.Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title(titlestring="Snake Game")
scr.tracer(0)
gameIsOn=True
sn=Snake.SnakeGame()
food=SnakeFood.Food()
sn.create_Snake()
scr.listen()
scr.onkey(fun=sn.move_Snake_UP,key="Up")
scr.onkey(fun=sn.move_Snake_Down,key="Down")
scr.onkey(fun=sn.move_Snake_Right,key="Right")
scr.onkey(fun=sn.move_Snake_Left,key="Left")
while gameIsOn:
    scr.update()
    time.sleep(0.1)
    sn.move_Snake()
    if sn.segments[0].distance(food)<15:
        food.scoreBoard()
        food.refresh()
        sn.extend()
    if sn.segments[0].xcor()>=299 or sn.segments[0].xcor()<=-299 or sn.segments[0].ycor()<=-299 or sn.segments[0].ycor()>=299:
        food.end_ScoreBoard()
        gameIsOn=False
    for snake_seg in sn.segments[1:]:
        if sn.segments[0].distance(snake_seg)<10:
            food.end_ScoreBoard()
            gameIsOn=False



scr.exitonclick()