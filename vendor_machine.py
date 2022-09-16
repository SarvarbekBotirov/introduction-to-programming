money = int(input("투입한 돈: "))
price = int(input("물건 값: "))

change = money - price
print("거스름 돈: ",change)
coin500s = change//500
change = change%500
coin100s = change // 100
change = change%100
coin50s = change//50
change = change %50
coin10s = change//10

print("500 동전의 개수: ",coin500s)
print("100 동전의 개수: ",coin100s)
print("50 동전의 개수: ",coin50s)
print("10 동전의 개수: ",coin10s)
