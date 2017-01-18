# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(1000)

# list of colors:
colors = ["blue", "green", "purple" "pink", "teal", "orange", "aqua", "black", "gray" "aqua", "brown" "red" "violet"]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


def triangle(size):
    color_tina()
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)


def chris(size):
    color_tina()
    tina.forward(25)
    tina.left(50)
    tina.right(75)
    tina.forward(60)
    tina.right(90)
    tina.forward(20)
    tina.forward(100)


polygon = turtle.Turtle()

num_sides = 10
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()

# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)


def super_circles(size):
    for x in range(1, 11):
        color_tina()
        tina.circle(size * x)


# let's make tina draw that square
# she'll fill in the spot of "some_turtle"
square(tina)

# let's draw a circle in the middle
tina.goto(25, 0)
tina.circle(25)

# Call my fancy new functions
super_circles(5)
triangle(50)

# at the end of my app i will use a conditional
# a conditional is another word for "if statement"
answer = input("what next?")
print("You just said " + answer)

if answer == "golden state":
    print("warriors blew a 3-1 lead in the NBA Finals")
elif answer == "triangle":
    print("Oh I know that one!")
    triangle(10)
elif answer == "super cirlces":
    super_circles(4)
elif answer == "chris":
    chris(1)