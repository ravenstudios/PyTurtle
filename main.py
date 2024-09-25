import turtle
import random

t = turtle.Turtle()

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
        

def heart1():
    t.speed(0)
    t.fillcolor('pink')
    t.begin_fill()

    t.left(140)
    t.forward(113)

    curve()
    t.left(120)

    curve()

    t.forward(112)



    t.end_fill()




def txt():
    t.up()

    t.setpos(-29, 80)
    t.down()
    t.color('red')

    t.write("Lana", font=("Audrey", 20, "bold"))

    





heart1()
txt()
t.ht()


t.screen.mainloop()

