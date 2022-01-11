import random
import turtle as t
# import colorgram

leo = t.Turtle()
t.colormode(255)
leo.color('red')
leo.hideturtle()
leo.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_dash(reps=1):
    for i in range(reps):
        leo.fd(10)
        leo.penup()
        leo.fd(10)
        leo.pendown()


colors = [
    'red', 'OrangeRed', 'blue', 'black', 'chocolate', 'DeepPink', 'orchid', 'NavajoWhite4',
    'LawnGreen', 'firebrick', 'CornflowerBlue', 'CadetBlue', 'PaleTurquoise', 'plum', 'peru',
    'DarkSlateBlue', 'DarkGreen', 'DarkOrange', 'DarkSalmon', 'DarkViolet', 'DarkOrchid',
    'DarkGoldenrod', 'DarkSlateGrey', 'DarkSlateBlue', 'DarkOliveGreen',
    'LightBlue', 'LightCyan', 'LightSeaGreen', 'LightPink', 'LightCoral',
    'LightGoldenrod', 'LightSkyBlue', 'LightSlateBlue', 'LightSteelBlue',
    'MistyRose4', 'RoyalBlue', 'thistle3', 'yellow4', 'yellow3', 'RosyBrown'
]


# create a function to draw the following shapes:
#   triangle, square, pentagon, hexagon,
#   heptagon, octagon, nonagon, decagon.
# the angles for each shape can be determined as a fraction of 360 degrees,
# depending on the number of sides.

def draw_shape(color, num_sides=3):
    """3 sided shape, angle = 360 / 3"""
    side_length = 70
    angle = 360 / num_sides
    leo.color(color)
    for i in range(num_sides):
        leo.forward(side_length)
        leo.right(angle)


# Draw a Random Walk


def random_walk(num_steps):
    direction = [90, -90, 180, 0]
    step_length = 20
    leo.pensize(10)

    for i in range(num_steps):
        leo.color(random_color())
        leo.setheading(random.choice(direction))
        leo.forward(step_length)


# Draw a Spirograph


def spirograph(span):
    for i in range(int(360 / span)):
        leo.left(span)
        leo.color(random_color())
        leo.circle(55.0)


# Create a grid of colored dots from the image


# colors_from_image = colorgram.extract('image.jpg', 10)
# rgb_colors = []
# for color in colors_from_image:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)

color_list = [
    (198, 12, 32), (250, 237, 17), (39, 77, 189),
    (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158)
]


def draw_dot_painting():
    """draw a 10x10 dot painting, the dots should be size 20, and separated by 50 in both directions"""
    # the height and width should each be 10x50 (=500)
    # update the starting point so that there is enough room to draw the entire square
    leo.penup()  # make sure the turtle does not draw any lines (only dots)
    leo.sety(-250)  # move the starting y-position (half of the 500-size square)
    # draw each row of dots
    for row in range(10):
        leo.setx(-250)
        # draw each of the 10 dots
        for col in range(10):
            leo.dot(20, random.choice(color_list))
            leo.forward(50)
        leo.left(90)
        leo.forward(50)
        leo.right(90)


# for shape_side_n in range(3, 11):
#     draw_shape(random.choice(colors), shape_side_n)

# random_walk(300)

# spirograph(5)

draw_dot_painting()

screen = t.Screen()
screen.exitonclick()
# make sure the screen stays open until the user clicks
# (once the turtle has completed the instructions)
