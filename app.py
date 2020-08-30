import turtle as t
from random import randint, choice

color_list = ["pink", "red", "yellow", "light blue", "blue", "purple"]
rainbow_color_list = ["red", "orange", "yellow", "green", "blue", "purple"]


class Rainbow:
    def __init__(self, width, x, y, quality):
        self.width = width
        self.x = x
        self.y = y
        self.quality = quality
        self.pensize = 50

    def draw(self):
        for color in rainbow_color_list:
            numColors = len(rainbow_color_list)
            scale = (numColors-rainbow_color_list.index(color))/2
            self.drawRay(color, scale)

    def drawRay(self, color, ray_size):
        """Draws a rainbow"""
        drawSteps = 180/self.quality
        xSpeed = (self.quality*ray_size)
        xOffset = ((drawSteps/3)*xSpeed)

        # move and ready turtle
        t.goto(self.x-xOffset, self.y)
        t.pensize(self.pensize)
        t.pencolor(color)
        t.setheading(90)
        t.pendown()

        # draw ray
        widthAdjust = self.width/drawSteps
        for _ in range(int(drawSteps)-1):
            t.right(self.quality)
            t.forward(xSpeed+widthAdjust)

        # draw cloud puffs
        self.drawCloudPuff()
        t.goto(self.x-((drawSteps/3)*xSpeed), self.y)
        self.drawCloudPuff()

        t.penup()
        t.setheading(0)

    def drawCloudPuff(self):
        """Draws a randomly sized cloud puff at the current location"""
        t.pensize(self.pensize+randint(10, 40))
        t.pencolor("white")
        t.pendown()
        t.forward(0)
        t.penup()


class FlowerPatch:
    def __init__(self, width, x, y):
        self.width = width
        self.x = x
        self.y = y
        self.flowers = []
        self.pensize = self.width / 15

    def add_flowers(self):
        """Adds five flower objects to the patch"""

        petal_length = self.pensize
        petal_size = self.pensize
        offset = 5

        for num in range(5):

            num_petals = randint(6, 10)
            color = choice(color_list)

            new_flower = Flower(
                num_petals,
                color,
                petal_length,
                petal_size,
                self.x + num * ((self.width / 4) - offset) + (offset * 2),
                self.y + petal_length * 2,
            )

            self.flowers.append(new_flower)

    def draw_flower_patch(self):
        """Draws the flower patch on the screen using turtlen graphics"""

        t.goto(self.x, self.y)
        t.pensize(self.pensize + 30)
        t.pencolor("#694508")

        t.pendown()
        t.forward(self.width)
        t.setheading(0)
        t.penup()

        for flower in self.flowers:
            flower.draw()


class Flower:
    def __init__(self, num_petals, color, petal_length, petal_size, x, y):
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size
        self.x = x
        self.y = y
        self.turn_amount = self.get_turn_degrees()

    def draw(self):
        """This function draws a flower and its stem using turtle graphics"""

        t.goto(self.x, self.y)
        t.pensize(self.petal_size)
        t.pencolor("green")
        t.pendown()

        # draw stem
        t.right(90)
        t.forward(self.petal_length * 2)
        t.backward(self.petal_length * 2)

        t.pencolor(self.color)
        t.right(self.turn_amount / 2)

        # draw petals
        for _ in range(self.num_petals):
            t.forward(self.petal_length)
            t.backward(self.petal_length)
            t.right(self.turn_amount)

        # draw center
        t.pencolor("orange")
        t.dot(self.petal_size)

        # reset heading for next flower
        t.setheading(0)
        t.penup()

    def get_turn_degrees(self):
        """this function gets how many degrees to turn before each petal"""
        return 360 / self.num_petals


t.bgcolor("#34b4eb")
t.speed("fastest")
t.hideturtle()
t.penup()

rainbow1 = Rainbow(850, -270, 100, 10)
rainbow1.draw()

box1 = FlowerPatch(230, -250, -300)
box1.add_flowers()
box1.draw_flower_patch()

box1 = FlowerPatch(430, -100, -130)
box1.add_flowers()
box1.draw_flower_patch()

t.done()
