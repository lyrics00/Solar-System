import turtle
import math
import time
import tkinter



#turtle.seth(45)
#turtle.tilt(45)
def ellipse(width,length,tilt, delay, rotations, turtle):
    turtle.speed(0)
    time.sleep(delay)
    for i in range(405 * rotations):
        t = i * (math.pi / 180)
        x = width * math.sin(t)
        y = length * math.cos(t) - length
        #turtle.goto(x,y)
        angle = tilt * (math.pi / 180)
        x1 = x * math.cos(angle) + y * math.sin(angle)
        y1 = x*math.sin(angle) - y*math.cos(angle)
        turtle.goto(x1,y1)
        

def main():
    screen = turtle.Screen()
    screen.addshape('space background.gif')
    screen.addshape('earth.gif')
    screen.addshape('venus.gif')
    screen.addshape('mars.gif')
    screen.addshape('sun.gif')
    screen.bgpic('space background.gif')

    sun_image = 'sun.gif'
    earth_image = 'earth.gif'
    venus_image = 'venus.gif'
    mars_image = 'mars.gif'

    sun = turtle.Turtle()
    sun.shape(sun_image)
    earth = turtle.Turtle()
    earth.shape(earth_image)
    venus = turtle.Turtle()
    venus.shape(venus_image)
    mars = turtle.Turtle()
    mars.shape(mars_image)
    ellipse(300,300,60, 0.1, 5, sun)
    ellipse()

if __name__ == "__main__":
    main()