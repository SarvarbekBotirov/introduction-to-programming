import random
print("Find the number between 1 and 100")
num = 0
tries = 10
rand_num = random.randint(1, 100)

while num != rand_num:
    num = int(input("Enter a number: "))
    tries -= 1
    if tries >= 0:
        print(f"시도횟수가 {tries} 남았다")
        if tries == 0:
            break

    if num < rand_num:
        print("낮음")
    elif num > rand_num:
        print("높음")
    else:
        print(f"축하한다. {tries}에 맞췄닼ㅋㅋㅋ")



