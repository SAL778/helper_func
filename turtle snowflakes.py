import turtle

def snowflake(t, lengthSide, levels):
    if levels == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(t, lengthSide, levels-1)
    t.left(60)
    snowflake(t, lengthSide, levels-1)
    t.right(120)
    snowflake(t, lengthSide, levels-1)
    t.left(60)
    snowflake(t, lengthSide, levels-1)

anms = turtle.Turtle()
anms.shape("circle")
anms.color("#6AA5E1", "#6AA5E1")
anms.speed(20000)
length = 300.0
anms.penup()
anms.fd(-150)
anms.pendown()

for i in range(3):
    snowflake(anms, length, 4)
    anms.right(120)

turtle.mainloop()
