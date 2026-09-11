#input

sender = input('Enter sender name ---> ')
type = input('What type of item is it? ---> ')
weight = float(input('How heavy? ---> '))
distance = float(input('How far? ---> '))
is_Fragile = bool(eval(input('Is the item fragile? ---> ')))
is_Express = bool(eval(input('Is it rush? ---> ')))
is_International = bool(eval(input(' Is the shippping international? ---> ')))

#prints

print('=================================================================')
print('Sender name: ',sender)
print('Item: ',type)
print('Weight: ',weight,'kg')
print('Distance: ',distance,'km')

#basecost
x = weight * 2.50
y = distance * 0.15
base_cost = x+y

if weight <=2.0 and distance <=100 and is_Express == False and is_International == False :
	print('You have free shipping')
	total = 0.00

elif is_International == True and is_Express == True :
	print('Your package is International Express')
	total = (base_cost * 1.40) + 50 

elif is_Express == True or is_International == True and weight > 20:
	print('Your package is Express/Heavy International')
	total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000 :
	print('Your package is Oversized')
	total =  base_cost + 30
else:
	print('Package is Standard Rate')
	total = base_cost

print('Your total is = $', total)
