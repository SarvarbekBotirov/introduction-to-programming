import turtle

t = turtle.Turtle()
t.shape("turtle")
radius = 50
t.goto(0,0)

t.circle(radius)
t.up()

radius = radius + 20
t.goto(100,0)
t.down()
t.circle(radius)

t.up()
radius = radius + 20
t.goto(200,0)
t.down()
t.circle(radius)
