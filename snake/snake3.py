import turtle
from turtle import Turtle, Screen
from random import randrange
#from playsound import playsound

'''Window'''
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=1000, height=700)
wn.tracer(0)

#booleans
up_ = False
down_ = False
left_ = False
right_ = True

left_right_value = 0
up_down = 0
n = 40

'''SPEED_ of the snake'''
SPEED_ = 0.2

score = 0

class turtle_object(Turtle):
    def __init__(self, position, shape, color):
        global SPEED_
        super().__init__(shape=shape, visible=False, )
        self.color(color)
        self.penup()
        self.setposition(position)
        self.speed(0)
        self.showturtle()
        self.dy = SPEED_
        self.dx = SPEED_

food = turtle_object((-500,500), "circle", "yellow")

'''These three squares make up the starting snake'''
square = turtle_object((0,0), "square", "red")
square2 = turtle_object((0,-20), "square", "white")
square3 = turtle_object((0,-40), "square", "white")


squares = [square2, square3]
new_squares = []

'''Makes the snake automatically move in one direction
until a key is pressed and the snake switches direction'''
def play():
    if right_:
        right()
    if left_:
        left()
    if up_:
        up()
    if down_:
        down()

'''Moves the snake upwards'''
def up():
    x, y = square.pos()
    global up_
    up_ = True
    global down_
    down_ = False
    global right_
    right_ = False
    global left_
    left_ = False
    global left_right_value
    global up_down
    global SPEED_
    first_pos = square.xcor()

    if left_right_value <= 0:
        #first
        square.sety(square.ycor() + SPEED_)

        for cube in squares:
            if cube.xcor() >= first_pos:
                cube.sety(cube.ycor() + SPEED_)
            else:
                cube.setx(cube.xcor() + SPEED_)
    else:
        #first
        first_pos = square.xcor()
        square.sety(square.ycor() + SPEED_)
        for cube in squares:
            if cube.xcor() <= first_pos:
                cube.sety(cube.ycor() + SPEED_)
            else:
                cube.setx(cube.xcor() - SPEED_)

    x1, y1 = square.pos()
    up_down = y-y1

'''Moves the snake downwards'''
def down():
    x, y = square.pos()
    global up_
    up_ = False
    global down_
    down_ = True
    global right_
    right_ = False
    global left_
    left_ = False
    global left_right_value
    global up_down
    global SPEED_

    if left_right_value <= 0:
        # first
        first_pos = square.xcor()
        square.sety(square.ycor() - SPEED_)

        for cube in squares:
            if cube.xcor() >= first_pos:
                cube.sety(cube.ycor() - SPEED_)
            else:
                cube.setx(cube.xcor() + SPEED_)

    else:
        # first
        first_pos = square.xcor()
        square.sety(square.ycor() - SPEED_)

        for cube in squares:
            if cube.xcor() <= first_pos:
                cube.sety(cube.ycor() - SPEED_)
            else:
                cube.setx(cube.xcor() - SPEED_)

    x1, y1 = square.pos()
    up_down = y-y1

'''Moves the snake left'''
def left():
    x, y = square.pos()
    global up_
    up_ = False
    global down_
    down_ = False
    global right_
    right_ = False
    global left_
    left_ = True
    global left_right_value
    global up_down
    global SPEED_

    if up_down <= 0:
        # first
        first_pos = square.ycor()
        square.setx(square.xcor() - SPEED_)
        for cube in squares:
            if cube.ycor() >= first_pos:
                cube.setx(cube.xcor() - SPEED_)
            else:
                cube.sety(cube.ycor() + SPEED_)
    else:
        # first
        first_pos = square.ycor()
        square.setx(square.xcor() - SPEED_)

        for cube in squares:
            if cube.ycor() <= first_pos:
                cube.setx(cube.xcor() - SPEED_)
            else:
                cube.sety(cube.ycor() - SPEED_)

    x1, y1 = square.pos()
    left_right_value = x - x1

'''Moves the snake right'''
def right():
    x, y = square.pos()
    global up_
    up_ = False
    global down_
    down_ = False
    global right_
    right_ = True
    global left_
    left_ = False
    global left_right_value
    global up_down
    global SPEED_

    if up_down <= 0:
        # first
        first_pos = square.ycor()
        square.setx(square.xcor() + SPEED_)

        for cube in squares:
            # second
            if cube.ycor() >= first_pos:
                cube.setx(cube.xcor() + SPEED_)
            else:
                cube.sety(cube.ycor() + SPEED_)
    else:
        # first
        first_pos = square.ycor()
        square.setx(square.xcor() + SPEED_)

        for cube in squares:
            # second
            if cube.ycor() <= first_pos:
                cube.setx(cube.xcor() + SPEED_)
            else:
                cube.sety(cube.ycor() - SPEED_)

    x1, y1 = square.pos()
    left_right_value = x - x1

'''BETA: SPEED_s up the SPEED_'''
def SPEED__up():
    global SPEED_
    SPEED_ += 0.01
'''BETA: Slows down the SPEED_'''
def SPEED__down():
    global SPEED_
    SPEED_ -= 0.01

'''Functions that makes the snake reappear 
on the opposite side when going through the wall'''
def upper_border():
    global n
    if square.ycor() > 370+n:
        new_ypos_upper = -350
        square.sety(new_ypos_upper)
        test_list = squares
        for cube in test_list:
            new_ypos_upper -= 20
            cube.sety(new_ypos_upper)
def lower_border():
    global n
    if square.ycor() < -350-n:
        new_ypos_lower = 350
        square.sety(350)
        test_list = squares
        for cube in test_list:
            new_ypos_lower += 20
            cube.sety(new_ypos_lower)
def left_border():
    global n
    if square.xcor() < -550-n:
        new_xpos_left = 530
        square.setx(530)
        test_list = squares
        for cube in test_list:
            new_xpos_left += 20
            cube.setx(new_xpos_left)
def right_border():
    global n
    if square.xcor() > 550+n:
        new_xpos_right = -530
        square.setx(-530)
        test_list = squares
        for cube in test_list:
            new_xpos_right -= 20
            cube.setx(new_xpos_right)

'''Position of the food'''
positions = [(randrange(-300, 300, 10), randrange(-300, 300, 10))]


'''Keybinds for the player'''
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")
wn.onkeypress(SPEED__up, "c")
wn.onkeypress(SPEED__down, "v")


'''Score system'''
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write("Score: 0", align="center", font=("Courier", 26, "normal"))

while True:

    play()

    #Border control
    right_border()
    left_border()
    lower_border()
    upper_border()

    for position in positions:
        food.goto(position)  # placing food at random location on the screen

        '''Checks if the snake hits the x,y-coordinates of the food'''
        if square.xcor()-12 < food.xcor() < 12+square.xcor() and square.ycor()-12 < food.ycor() < 12+square.ycor():
            pen.clear()  # clearing the score before adding new score
            n += 20  # for smoother reappearing (check border control functions)
            try:
                positions.remove(position)
            except:
                print("no elements in list")
                continue
            new_squares.append(turtle_object((-500, -500), "square", "white"))  # Adding a new tail to the snake
            positions.append((randrange(-300, 300, 10), randrange(-300, 300, 10)))  # adding new food

            '''Depending on the location of the previous tail on 
            the snake (squares[-1]), the next square is placed behind that'''
            for rectangle in new_squares:
                if left_right_value < 0:
                    rectangle.goto(squares[-1].xcor() - 20, squares[-1].ycor())
                if left_right_value > 0:
                    rectangle.goto(squares[-1].xcor() + 20, squares[-1].ycor())
                if up_down > 0:
                    rectangle.goto(squares[-1].xcor(), squares[-1].ycor() + 20)
                if up_down < 0:
                    rectangle.goto(squares[-1].xcor(), squares[-1].ycor() - 20)
                squares.append(new_squares.pop())  # appending the newly added tail to the list 'squares' which is used in the 'direction functions
            score += 1
            #playsound('eat.mp3', block=False)
            pen.write(f"Score: {score}", align="center", font=("Courier", 26, "normal"))
    wn.update()