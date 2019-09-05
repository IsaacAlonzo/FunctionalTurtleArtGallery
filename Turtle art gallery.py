import turtle
bob=turtle
bob.speed(20)
bob.penup()
bob.goto(100, 100)
bob.pendown()
def square():
    for i in range(4):
        bob.forward(50)
        bob.right(90)

square()
bob.color("red")
for i in range(75):
    square()
    bob.right(5)

bob.penup()
bob.goto(-200, -200)
bob.pendown()

def star():
    for i in  range(5):
        bob.forward(side)
        bob.left(144)

bob.color("blue")
side=20
for i in range(40):
    star()
    bob.right(5)
    side+=4

bob.penup()
bob.goto(-100, 100)
bob.pendown()
def triangle():
    for i in range(3):
        bob.forward(50)
        bob.right(120)





bob.exitonclick()