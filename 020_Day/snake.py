from turtle import Turtle

class Snake:
    def __init__(self, initial_length=3, init_y=0, init_x=0):
        self.seg_list=[]
        for i in range(initial_length):
            new_seg=Turtle(visible=False)
            new_seg.speed(0)
            new_seg.pu()
            new_seg.setpos(init_x - i*20,init_y)
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
        self.seg_list[0].setheading(90)

    def left(self):
        self.seg_list[0].setheading(180)
    
    def down(self):
        self.seg_list[0].setheading(270)

    def right(self):
        self.seg_list[0].setheading(0)


