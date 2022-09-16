import turtle

t = turtle.Turtle()
t.shape("turtle")

width = int(input("집의 크기를 얼마로 할까요?: "))

def square():
    t.forward(width)    
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(width)
    
def triangle():
    t.right(30)
    t.forward(width)
    t.right(120)
    t.forward(width)
    t.right(120)
    t.forward(width)

square()
triangle()
t.right(180)
