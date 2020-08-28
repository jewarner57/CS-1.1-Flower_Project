import turtle as t
from random import randint, choice

color_list = ["red", "light blue", "yellow", "blue", "purple", "pink"]


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


t.speed("fastest")
t.hideturtle()
t.penup()

box1 = FlowerPatch(530, -250, 100)
box1.add_flowers()
box1.draw_flower_patch()

box1 = FlowerPatch(530, -250, -100)
box1.add_flowers()
box1.draw_flower_patch()

t.done()
