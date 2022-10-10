# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "Enter the shape: ").lower()
# if s == "사각형":
#     s = turtle.textinput("", "width: ")
#     w = int(s)
#     s = turtle.textinput("", "height: ")
#     h = int(s)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
#     t.left(90)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
# elif s == "삼각형":
#     s = turtle.textinput("", "width: ")
#     w = int(s)
#     for i in range(3):
#         t.forward(w)
#         t.left(120)
# elif s == "원":
#     s = turtle.textinput("", "width: ")
#     w = int(s)
#     t.circle(w)

# --------------------------------------
# import random

# x = random.randint(1, 100)
# y = random.randint(1, 100)

# cal = x - y
# ans = int(input(str(x) + "-"+str(y)+"="))

# if ans == cal:
#     print("맞았습니다")
# else:
#     print("틀렀습니다")


# -------------------------------------------------
import random

lottery = random.randint(0, 99)
digit1 = lottery // 10
digit = lottery % 10

user = int(input('복권번호를 입력하시오 (0에서 99사이): '))
print(f"당첨번호는 {lottery}")
if lottery == user:
    print("100억 당첨입니다!!!")
elif digit1 == user // 10 or digit1 % 10 or digit // 10 or digit % 10:
    print("50원 당첨입니다")
else:
    print("낙첨됐습니다")
