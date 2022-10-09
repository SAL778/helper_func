
import turtle
import math

anms = turtle.Turtle()
turtle.Screen().bgcolor("black")
anms.color("blue", "red")
anms.speed(2000)
anms.shape("circle")

anms.begin_fill()
for i in range(2200):
    anms.forward(math.sqrt(i))
    anms.left(i%180)
anms.end_fill()

turtle.mainloop()
