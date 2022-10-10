import turtle

t = turtle.Turtle()
t.shape('turtle')
s = turtle.textinput(",", "Angels: ")  # in order to use textinput we need to use turtle not t variable!!!
s = int(s)  # and after getting input important thing is to make it integer!!!

for _ in range(s):
    t.forward(100)
    t.left(360 / s)
