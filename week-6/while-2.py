count = 1
sum = 0
while count <= 10:
    sum += count
    count += 1
print("합계는", sum)

#-------------------------------------------------------------------------------

num = int(input("Enter a number: "))
count = 1
while count <= 9:
    print(f"{num} x {count} = {num*count}")
    count += 1
