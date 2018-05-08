import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        # branch forward; specify color and thickness
        t.width(width = branchLen/10)
        if branchLen < 20: t.color('green')
        else: t.color('brown')
        t.forward(branchLen)

        theta = random.randint(15, 45+1)
        distance = random.randint(10, 20+1)

        t.right(theta)
        tree(branchLen-distance,t)
        t.left(theta*2)
        tree(branchLen-distance,t)
        t.right(theta)

        # branch backward; specify color and thickness
        t.width(width = branchLen/10)
        if branchLen < 20: t.color('green')
        else: t.color('brown')
        t.backward(branchLen)

t = turtle.Turtle()
myWin = turtle.Screen()

t.left(90) # head pointing to the north
t.up() # tail up: no drawing
t.backward(100)
t.down() # tail down: start to draw
t.color("green")

tree(75,t)

myWin.exitonclick()
