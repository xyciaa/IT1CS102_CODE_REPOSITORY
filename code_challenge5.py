size = int(input('Input size of x ---> '))
for x in range(size):
    for y in range(size):
        if x + y == size - 1 or x - y == 0:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')    
    print()

