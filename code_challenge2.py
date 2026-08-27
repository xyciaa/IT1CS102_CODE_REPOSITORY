money = 11147

print("Money to deposit: ", money)

thousand = money//1000
money = money - thousand*1000
fivehund = money//500
money = money - fivehund*500
twohund = money//200
money = money - twohund*200
onehund = money//100
money = money-onehund*100
fifty = money//50
money = money - fifty*50
twenty = money//20
money = money - twenty*20
ten= money//10
money = money - ten*10
five = money//5
money = money- five*5
one = money//1
money = money - one


print("you have ", thousand,"quantity of 1000")
print("you have ", fivehund,"quantity of 500")
print("you have ", twohund,"quantity of 200")
print("you have ", onehund,"quantity of 100")
print("you have ", fifty,"quantity of 50")
print("you have ", twenty,"quantity of 20")
print("you have ", ten,"quantity of 10")
print("you have ", five,"quantity of 5")
print("you have ", one,"quantity of 1")

