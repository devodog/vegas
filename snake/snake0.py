# import package
import turtle
import time
import random

# write text
t = turtle.Turtle()
t.shapesize(1)
t.shape("square")

delta = 10
x = 0
y = 0
previousDir = 4
span = 200

def fire(fx, fy):
    if -10 < (x - fx) < 10 and -10 < (y - fy) < 10:
        print("hit")
        print(x,y, " ", fx,fy)
    else:
        print("missed")
        print(x,y, " ", fx,fy)

t.onclick(fire, 1, None)

while 1:
    testRange = random.randint(1, 20)
    
    while 1:
        direction = random.randint(1, 4) 
        if previousDir < 3 and direction > 2:
            previousDir = direction
            break
        if previousDir > 2 and direction < 3:
            previousDir = direction
            break

    for i in range(testRange):
        if direction == 1:
            #north = True
            y = y + delta
            
            if y > span:
                y = y - delta
            
            t.goto(x,y)
            t.shape("square")

        if direction == 2:
            #south = True
            y = y - delta
            if y < (span*-1):
                y = y + delta
            t.goto(x,y)
            t.shape("square")

        if direction == 3:
            #West = True
            x = x - delta
            if x < (span*-1):
                x = x + delta    
            t.goto(x,y)
            t.shape("square")

        if direction == 4:
            #East = True
            x = x + delta
            if x > span:
                x = x - delta
            t.goto(x,y)
            t.shape("square")
        
    time.sleep(1)