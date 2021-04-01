import turtle
sample = turtle.Turtle()
#making circle face of our emoji
sample.up()
sample.goto(0,-100)
sample.down()
#yellow color giving
sample.begin_fill()
sample.pendown()
sample.fillcolor('yellow')
sample.circle(100)
sample.end_fill()

#smile part in emoji
sample.up()
sample.goto(-67, -40)
sample.setheading(-60)
sample.width(5)
sample.down()
sample.circle(80, 120)
sample.fillcolor('black')

#eye part
for i in range(-35, 105, 70):
    sample.up()
    sample.goto(i,35)
    sample.setheading(0)
    sample.down()
    sample.begin_fill()
    sample.circle(10)
    sample.end_fill()
sample.penup()
sample.goto(0, -150) #moving cursor positive upside negative downside

turtle.mainloop()