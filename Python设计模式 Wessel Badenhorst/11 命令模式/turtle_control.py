# encoding=utf-8
"""
实际上,我们在做的是创建一个用来控制小乌龟的接口.
实际上,我们是在将命令从系统的一个部分发送到另一个部分.
"""

import turtle

turtle.setup(400, 400)

screen = turtle.Screen()

screen.title("Keyboard drawing")

t = turtle.Turtle()
distance = 10
angle = 90

def advance():
	t.forward(distance)


def turn_left():
	t.left(angle)


def turn_right():
	t.right(angle)


# 回退
def retreat():
	t.back(distance)


def quit():
	screen.bye()


screen.onkey(advance, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(retreat, "s")
screen.onkey(quit, "Escape")

screen.listen()
screen.mainloop()
