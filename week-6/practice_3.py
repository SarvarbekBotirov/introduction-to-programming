import turtle
import random

t = turtle.Turtle()
t.shape('turtle')
ang = [90, 180, 360]

for _ in range(30):
    length = random.randint(1, 100)
    t.forward(length)
    angle = random.choice(ang)
    t.left(angle)
