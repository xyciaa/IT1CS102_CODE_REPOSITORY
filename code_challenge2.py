money = int(input('Enter money to deposit-->'))

print('================ PH PESO DENOMINATION BREAK DOWN ====================')
print('Money to deposit ---->',money,'php')

thousan= money // 1000
thousan_rem = money % 1000

fivehund = thousan_rem // 500
fivehund_rem = thousan_rem % 500
twohund = fivehund_rem // 200
twohund_rem = fivehund_rem % 200
onehund = twohund_rem // 100
onehund_rem = twohund_rem %100
fift = onehund_rem // 50
fift_rem = onehund_rem % 50
twent= fift_rem // 20
twent_rem = fift_rem % 20
ten= twent_rem // 10
ten_rem = twent_rem % 10
five = ten_rem // 5
ten_rem = ten_rem % 5
one = ten_rem // 1
one_rem = ten_rem % 1

print('1000 --->', thousan)
print('500 --->', fivehund)
print('200 --->', twohund)
print('100 --->', onehund)
print('50 --->', fift)
print('20 --->', twent)
print('10 --->', ten)
print('5 --->', five)
print('1 --->', one)

print('=====================================================================')

