#https://pythondex.com/make-pacman-game-in-python

from turtle import *
path = Turtle(visible=False)
 
#Funcao setup pertence a biblioteca turtle.py. Apenas desenha a tela.
setup(600, 620, 370, 0)

def square(x, y):
    """Draw square using path at (x, y)."""
#    path.up()
    path.goto(x, y)
#    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

#    path.end_fill()
square(1, 1)
square(20, 20)