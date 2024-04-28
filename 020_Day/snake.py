from turtle import Turtle

class Snake:
    def __init__(self, initial_length=3):
        self.seg_list=[]
        self.length=3
        for i in range(initial_length):
            self.add_segment([-20*i,0])
        self.head=self.seg_list[0]

    def extend(self):
        self.add_segment(self.seg_list[-1].pos())

    def add_segment(self,position):
        new_seg=Turtle(visible=False)
        new_seg.speed(0)
        new_seg.pu()
        new_seg.setpos(position)
        new_seg.shape('square')
        new_seg.color('white')
        new_seg.speed(5)
        new_seg.showturtle()
        self.seg_list.append(new_seg)

    def move(self):
        replace_pos=self.seg_list[0].pos()
        self.seg_list[0].forward(20)
        for seg in range(1,len(self.seg_list)):
            tmp=self.seg_list[seg].pos()
            self.seg_list[seg].setpos(replace_pos)
            replace_pos=tmp
    
    def up(self):
        if self.seg_list[0].heading() !=270:
            self.seg_list[0].setheading(90)

    def left(self):
        if self.seg_list[0].heading() !=0:
            self.seg_list[0].setheading(180)
    
    def down(self):
        if self.seg_list[0].heading() !=90:
            self.seg_list[0].setheading(270)

    def right(self):
        if self.seg_list[0].heading() !=180:
            self.seg_list[0].setheading(0)

    def out_of_bounds(self):
        head_coords=self.head.pos()
        if head_coords[0] > 280 or head_coords[0] < -280:
            return True
        if head_coords[1] > 280 or head_coords[1] < -280:
            return True

