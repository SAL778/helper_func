
import turtle

anms = turtle.Turtle()
turtle.Screen().bgcolor("black")
anms.speed(5)
anms.shape("turtle")
anms.color("white")


#8 edges
for i in range(8):
    anms.forward(200)
    anms.left(135)

turtle.mainloop()
