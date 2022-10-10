import turtle

t = turtle.Turtle()
t.shape('turtle')

for _ in range(5):
    t.forward(200)
    t.right(144)

count = 1
while count < 6:
    t.forward(100)
    t.right(144)
    count += 1