import turtle

t = turtle.Turtle()
t.shape("turtle")

user_input = int(input("몇각형을 그리시겠어요?: "))

for i in range(user_input):
    t.forward(100)
    t.left(360/user_input)
