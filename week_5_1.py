# ------------------------First practice------------------------------
# score = int(input('성적을 입력하시오: '))

# if score >= 60:
#     print("합격입니다")
# else:
#     print('불합격입니다')


# ------------------------Second Practice------------------------------
# import turtle
# num = int(input('정수를 입력하시오: '))
# if num % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# ------------------------Third Practice------------------------------
import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("Positive number")
t.goto(100, 0)
t.write("Equal to 0")
t.goto(100, -100)
t.write("Negative number")

t.goto(0, 0)
t.pendown()

text = turtle.textinput("", 'Enter a number: ')
n = int(text)

if (n > 0):
    t.goto(100, 100)
if (n == 0):
    t.goto(100, 0)
if (n < 0):
    t.goto(100, -100)
