import turtle
import math
import time
import tkinter
screen = turtle.Screen()
sun_image = 'sun.gif'
earth_image = 'earth.gif'
venus_image = 'venus (1).gif'
mars_image = 'mars.gif'
jupiter_image = "jupiter.gif"
saturn_image = "saturn.gif"
uranus_image = "uranus.gif"


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
    screen.addshape('space background.gif')
    screen.addshape('earth.gif')
    screen.addshape('venus (1).gif')
    screen.addshape('mars.gif')
    screen.addshape('sun.gif')
    screen.addshape('jupiter.gif')
    screen.addshape('saturn.gif')
    screen.addshape('uranus.gif')
    screen.bgpic('space background.gif')

    sun = turtle.Turtle()
    sun.shape(sun_image)
    earth = turtle.Turtle()
    earth.shape(earth_image)
    venus = turtle.Turtle()
    venus.shape(venus_image)
    mars = turtle.Turtle()
    mars.shape(mars_image)
    jupiter = turtle.Turtle()
    jupiter.shape(jupiter_image)
    saturn = turtle.Turtle()
    saturn.shape(saturn_image)
    uranus = turtle.Turtle()
    uranus.shape(uranus_image)
    earth.goto(0,100)
    ellipse(300, 300, 60, 0.1, 5, sun)
    sun.addshape(ellipse(400, 400, 60, 0.0, 5, jupiter))
    sun.pu

if __name__ == "__main__":
    main()
screen.mainloop()