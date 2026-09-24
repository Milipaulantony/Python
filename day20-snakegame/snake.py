from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position_add):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position_add)
        self.segments.append(new_segment)

    def extend(self):
        last_seg_pos = self.segments[-1].position()
        self.add_segment(last_seg_pos)
    def move(self):
        for curr_index in range(len(self.segments) - 1, 0, -1):
            prev_seg = self.segments[curr_index - 1]
            new_x = prev_seg.xcor()
            new_y = prev_seg.ycor()
            curr_seg = self.segments[curr_index]
            curr_seg.goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        #self.segments[0].setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
