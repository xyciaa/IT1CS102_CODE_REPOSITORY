#JEEPNEY SIMULATOR
route = ['Terminal', 'Perez Park', 'Pacific Mall']
passen = []
seats = 6
fare = 13
total = 0

while True:
    print()
    print('Sakay: ', passen)
    print(len(passen), 'of', seats, 'seats')
    print('1 - Sakay 2 - Priority seat 3 - Para po!')
    print('4 - Baba sa pinto 5 - Baba sa harap')
    print('6 - Seat check  7 - Balikan 8 - Exit')
    choice = input('Choice: ')

    if choice == '1':
        if len(passen) == seats:
            print('Puno na!')
        else:
            name = input('NAME: ')
            passen.append(name)
            total = total + fare
            print(name, 'boarded at the back.')

    elif choice == '2':
        if len(passen) == seats:
            print('Puno na!')
        else:
            name = input('Name: ')
            passen.insert(0, name)
            total = total + fare
            print(name, 'took the priority seat.')       

    elif choice == '3':
        name = input('Who is getting off? ')
        if name in passen:
            passen.remove(name)
            print(name, 'Got off. Ingat!')
        else:
            print(name, "is not on this jeep.")

    elif choice == '4':
        if len(passen) == 0:
            print('The jeep is empty')
        else:
            left = passen.pop()
            print(left, "got off the door.")

    elif choice == '5':
        if len(passen) == 0:
            print("The jeep is empty")
        else:
            front = passen.pop(0)
            print(front, 'got off at the front.')

    elif choice == '6':
        for i in range(len(passen)):
            print('Seat',i + 1, passen[i])

    elif choice == '7':
        route.reverse()
        print('Route: ', route)

    elif choice == '8':
        print('Total fare today: ', total)
        break

    else:
        print('Invalid choice.')