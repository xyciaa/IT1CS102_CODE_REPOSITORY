sum = 0

t = True

while t == True:
    x = int(input('ENTER A NUMBER --> '))

    if x == 0:
        print('Loop Terminated')
        print(' Total of all numbers is ', sum)
        break

    else:
        print('Continue Loop')
        sum += x 
        print('Current total is ', sum)
        continue
