from turtle import Screen,Turtle
import time
STARTING_POSITIONS=[(20,0),(0,0),(-20,0)]
MOVE_DISTANCE = 20
class Snake:
    
    
    def __init__(self):
        self.segments=[]
        for position in STARTING_POSITIONS:
            
            segment= Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        self.head=self.segments[0]

    def move(self):
        self.x=self.segments[len(self.segments)-1].xcor()
        self.y=self.segments[len(self.segments)-1].ycor()
        for seg_num in range( len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
            
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.__init__()

    
    def up(self):
        if(self.head.heading()!=270):
            self.head.seth(90)
    def down(self):
        if(self.head.heading()!=90):
            self.head.seth(270)
    def left(self):
        if(self.head.heading()!=0):
            self.head.seth(180)
    def right(self):
        if(self.head.heading()!=180):
            self.head.seth(0)