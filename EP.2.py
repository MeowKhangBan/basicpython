
import turtle
omg = turtle.Pen()
omg.shape('turtle')

def re(w='left',n=1):
    if w == 'left':
        for i in range(n):
            omg.forward(50)
            omg.left(37)
    elif w == 'right':
        for i in range(n):
            omg.forward(40)
            omg.right(35)

def go(x,y):
    omg.penup()
    omg.goto(x,y)
    omg.pendown()

re('left',50)
re('right',50)
re('right',25)
re('left',50)



go(200,500)
