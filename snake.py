from turtle import Turtle, Screen
import time
#screen = Screen()

POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:


    def __init__(self):
        self.game_snakes_list = []
        self.create_snake()
        self.head = self.game_snakes_list[0]
        self.move()
        self.up()
        self.down()
        self.left()
        self.right()

    def create_snake(self):

        for position in POSITIONS:
            self.add_segment(position)



    def add_segment(self,position):
        game_snakes = Turtle('square')
        game_snakes.color('white')
        #game_snakes.shapesize()
        game_snakes.penup()
        game_snakes.goto(position)
        self.game_snakes_list.append(game_snakes)

    def extend(self):
        self.add_segment(self.game_snakes_list[-1].position())


    def move(self):
        global game_snakes_list
        for object in range(len(self.game_snakes_list)-1, 0, -1):
            new_x = self.game_snakes_list[object - 1].xcor()   #get the x co-ordinate of the second to last object
            new_y = self.game_snakes_list[object - 1].ycor()   #get the y co-ordinate of the second to last object
            self.game_snakes_list[object].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(MOVE_DISTANCE)
