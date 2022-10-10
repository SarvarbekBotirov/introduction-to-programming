num = int(input("Enter a num: "))
fac = 1
# n!=n x n-1
for i in range(1, num + 1):  # range(1,6)
    fac = fac * i
print(fac)
