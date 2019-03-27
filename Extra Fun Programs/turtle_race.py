

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    for line in range(7):
        pendown()
        forward(20)
        penup()
        forward(10)
    backward(220)
    left(90)
    forward(20)

ada = Turtle()
ada.shape('turtle')
ada.color('red')
ada.penup()
ada.goto(-160, 120)
ada.pendown()

bob = Turtle()
bob.shape('turtle')
bob.color('blue')
bob.penup()
bob.goto(-160, 80)
bob.pendown()

nan = Turtle()
nan.shape('turtle')
nan.color('orange')
nan.penup()
nan.goto(-160, 40)
nan.pendown()

sam = Turtle()
sam.shape('turtle')
sam.color('green')
sam.penup()
sam.goto(-160, 0)
sam.pendown()

pam = Turtle()
pam.shape('turtle')
pam.color('purple')
pam.penup()
pam.goto(-160, -40)
pam.pendown()


for turn in range(108):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    nan.forward(randint(1, 5))
    sam.forward(randint(1, 5))
    pam.forward(randint(1, 5))
