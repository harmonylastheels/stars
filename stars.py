import turtle
import random

# set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# create turtle object
star = turtle.Turtle()
star.speed(0)


# function to draw a star
def draw_star(x, y, size):
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(random.choice(["yellow", "white"]))
    for _ in range(5):
        star.forward(size)
        star.right(144)


for _ in range(100):
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    size = random.randint(10, 25)
    draw_star(x, y, size)


star.hideturtle()
screen.mainloop()
