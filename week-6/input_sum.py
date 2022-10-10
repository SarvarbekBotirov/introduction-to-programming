ask = "".lower()
total = 0
while ask != 'no':
    num = int(input("Enter a num: "))
    total += num

    ask = input("yes/no: ")

print(total)