from activity25 import taga_triangle
from activity25 import sum
from activity25 import box
from activity25 import my_factorial
import os 

while True:
    print(' MINI MENU ')
    print(' Select an option: ')
    print(' 1 - Triangle ')
    print(' 2 - Sum ')
    print(' 3 - Box ')
    print(' 4 - Factorial ')
    print(' 5 - EXIT ')
    choose = int(input(" Which one ---> "))

    if choose == 1:
        print('Triangle')
        size = int(input(' Enter size of the triangle '))
        taga_triangle(size)
        continue

    elif choose == 2:
        print('Sum')
        n1 = int(input(' number 1 --> '))
        n2 = int(input(' number 2 --> '))
        print( ' The sum of {n1} and {n2} is {sum(n1, n2)}')
        sum(size)
        continue

    elif choose == 3:
        print('box')
        size = int(input(' Enter size of the box '))
        box(size)
        continue

    elif choose == 4:
        print('Factorial')
        n = int(input(' Input any number ---> '))
        print(f'The Factorial of {n} is {my_factorial(n)}')
        continue

    elif choose == 5:
        print (' SYSTEM EXIT ')
        break
    else:
        print(' INVALID CHOISE')
        continue